#!/usr/bin/env python3
"""Extract resume text from user-resumes files.

Supports txt/md directly, docx via OOXML, doc/pdf via optional Windows Word COM,
and PDF via optional libraries or a lightweight ToUnicode fallback.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import zlib
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


TEXT_EXTS = {".txt", ".md"}
DOCX_EXTS = {".docx"}
PDF_EXTS = {".pdf"}
WORD_EXTS = {".doc"}


def read_text_file(path: Path) -> str:
    for encoding in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def extract_docx(path: Path) -> str:
    chunks: list[str] = []
    with zipfile.ZipFile(path) as zf:
        names = [
            "word/document.xml",
            *sorted(n for n in zf.namelist() if n.startswith("word/header")),
            *sorted(n for n in zf.namelist() if n.startswith("word/footer")),
        ]
        for name in names:
            if name not in zf.namelist():
                continue
            root = ET.fromstring(zf.read(name))
            ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
            for para in root.findall(".//w:p", ns):
                text = "".join(t.text or "" for t in para.findall(".//w:t", ns)).strip()
                if text:
                    chunks.append(text)
    return "\n".join(chunks)


def try_word_com(path: Path) -> str:
    try:
        import win32com.client  # type: ignore
    except Exception:
        return ""

    word_input = path
    if any(ord(ch) > 127 for ch in str(path)):
        word_input = path.parent / f"__resume_extract_input{path.suffix.lower()}"
        shutil.copy2(path, word_input)

    out = path.with_suffix(path.suffix + ".word-extracted.txt")
    word_out = out
    if word_input != path:
        word_out = path.parent / "__resume_extract_output.txt"
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    try:
        doc = word.Documents.Open(str(word_input), ConfirmConversions=False, ReadOnly=True, OpenAndRepair=True)
        doc.SaveAs(str(word_out), FileFormat=2)
        doc.Close(False)
        text = read_text_file(word_out)
        try:
            out.write_text(text, encoding="utf-8")
        except Exception:
            pass
        return text
    except Exception:
        return ""
    finally:
        word.Quit()


def try_pdf_libraries(path: Path) -> str:
    try:
        from pypdf import PdfReader  # type: ignore

        reader = PdfReader(str(path))
        return "\n".join((page.extract_text() or "") for page in reader.pages)
    except Exception:
        pass

    try:
        import PyPDF2  # type: ignore

        reader = PyPDF2.PdfReader(str(path))
        return "\n".join((page.extract_text() or "") for page in reader.pages)
    except Exception:
        pass

    try:
        import pdfplumber  # type: ignore

        with pdfplumber.open(str(path)) as pdf:
            return "\n".join((page.extract_text() or "") for page in pdf.pages)
    except Exception:
        return ""


def pdf_objects(data: bytes) -> dict[int, bytes]:
    objects: dict[int, bytes] = {}
    for match in re.finditer(rb"(\d+)\s+0\s+obj(.*?)endobj", data, re.S):
        objects[int(match.group(1))] = match.group(2)
    return objects


def stream_data(obj: bytes) -> bytes:
    match = re.search(rb"stream\r?\n(.*?)\r?\nendstream", obj, re.S)
    if not match:
        return b""
    raw = match.group(1)
    try:
        return zlib.decompress(raw)
    except Exception:
        return raw


def parse_cmap(cmap: bytes) -> dict[str, str]:
    mapping: dict[str, str] = {}

    for src, dst in re.findall(rb"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", cmap):
        try:
            chars = bytes.fromhex(dst.decode()).decode("utf-16-be")
            mapping[src.decode().upper()] = chars
        except Exception:
            continue

    for start, end, dst in re.findall(
        rb"<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>", cmap
    ):
        try:
            s = int(start, 16)
            e = int(end, 16)
            d = int(dst, 16)
        except Exception:
            continue
        if e - s > 500:
            continue
        width = len(start)
        for offset, code in enumerate(range(s, e + 1)):
            try:
                mapping[f"{code:0{width}X}"] = chr(d + offset)
            except Exception:
                pass

    return mapping


def decode_hex_text(hex_text: str, cmap: dict[str, str]) -> str:
    hex_text = re.sub(r"\s+", "", hex_text).upper()
    if not hex_text:
        return ""

    chars: list[str] = []
    step = 4 if len(hex_text) >= 4 else 2
    for i in range(0, len(hex_text), step):
        code = hex_text[i : i + step]
        if not code:
            continue
        if code in cmap:
            chars.append(cmap[code])
            continue
        try:
            chars.append(bytes.fromhex(code).decode("utf-16-be" if len(code) == 4 else "latin1"))
        except Exception:
            pass
    return "".join(chars)


def fallback_pdf_tounicode(path: Path) -> str:
    data = path.read_bytes()
    objects = pdf_objects(data)

    font_to_cmap: dict[str, dict[str, str]] = {}
    for page in objects.values():
        font_refs = re.findall(rb"/(FT\d+)\s+(\d+)\s+0\s+R", page)
        for font_name, font_obj_id in font_refs:
            font_obj = objects.get(int(font_obj_id), b"")
            match = re.search(rb"/ToUnicode\s+(\d+)\s+0\s+R", font_obj)
            if not match:
                continue
            cmap_obj = objects.get(int(match.group(1)), b"")
            font_to_cmap[font_name.decode()] = parse_cmap(stream_data(cmap_obj))

    items: list[tuple[float, float, str]] = []
    content_streams = [
        stream_data(obj)
        for obj in objects.values()
        if b" BT" in stream_data(obj) or b"\nBT" in stream_data(obj) or b"\rBT" in stream_data(obj)
    ]

    token_re = re.compile(
        rb"/(FT\d+)\s+[-\d.]+\s+Tf|"
        rb"([-+]?\d*\.?\d+)\s+([-+]?\d*\.?\d+)\s+[-+]?\d*\.?\d+\s+[-+]?\d*\.?\d+\s+([-+]?\d*\.?\d+)\s+([-+]?\d*\.?\d+)\s+Tm|"
        rb"([-+]?\d*\.?\d+)\s+([-+]?\d*\.?\d+)\s+TD|"
        rb"<([0-9A-Fa-f\s]+)>\s*Tj|"
        rb"\[(.*?)\]\s*TJ",
        re.S,
    )

    for content in content_streams:
        font = ""
        x = 0.0
        y = 0.0
        for match in token_re.finditer(content):
            if match.group(1):
                font = match.group(1).decode()
            elif match.group(4) and match.group(5):
                x = float(match.group(4))
                y = float(match.group(5))
            elif match.group(6) and match.group(7):
                x += float(match.group(6))
                y += float(match.group(7))
            elif match.group(8):
                text = decode_hex_text(match.group(8).decode(), font_to_cmap.get(font, {}))
                if text:
                    items.append((y, x, text))
            elif match.group(9):
                cmap = font_to_cmap.get(font, {})
                text = "".join(
                    decode_hex_text(h.decode(), cmap)
                    for h in re.findall(rb"<([0-9A-Fa-f\s]+)>", match.group(9))
                )
                if text:
                    items.append((y, x, text))

    if not items:
        return ""

    items.sort(key=lambda item: (round(item[0] / 3) * 3, item[1]))
    lines: list[str] = []
    current_y: float | None = None
    current: list[str] = []
    for y, _x, text in items:
        if current_y is None or abs(y - current_y) <= 3:
            current.append(text)
            current_y = y if current_y is None else current_y
        else:
            line = "".join(current).strip()
            if line:
                lines.append(line)
            current = [text]
            current_y = y
    if current:
        line = "".join(current).strip()
        if line:
            lines.append(line)

    return "\n".join(lines)


def extract(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in TEXT_EXTS:
        return read_text_file(path)
    if suffix in DOCX_EXTS:
        return extract_docx(path)
    if suffix in WORD_EXTS:
        return try_word_com(path)
    if suffix in PDF_EXTS:
        text = try_pdf_libraries(path).strip()
        if text:
            return text
        text = try_word_com(path).strip()
        if text:
            return text
        return fallback_pdf_tounicode(path)
    return ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="interview-helper/user-resumes")
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    target = Path(args.input)
    files = [target] if target.is_file() else [
        p for p in sorted(target.iterdir()) if p.is_file() and p.name != ".gitkeep"
    ]
    generated_names = {"combined-resume-extracted.txt"}
    supported = [
        p
        for p in files
        if p.suffix.lower() in TEXT_EXTS | DOCX_EXTS | PDF_EXTS | WORD_EXTS
        and not p.name.startswith("resume-temp")
        and not p.name.startswith("__resume_extract_")
        and not p.name.endswith(".extracted.txt")
        and not p.name.endswith(".word-extracted.txt")
        and p.name not in generated_names
    ]
    if not supported:
        print("No supported resume files found.", file=sys.stderr)
        return 2

    outputs: list[str] = []
    for path in supported:
        text = extract(path).strip()
        if not text:
            outputs.append(f"# {path.name}\n\n[未能提取文本，请另存为 docx/txt/md 或使用可复制文字的 PDF。]")
        else:
            outputs.append(f"# {path.name}\n\n{text}")
            extracted = path.with_suffix(path.suffix + ".extracted.txt")
            extracted.write_text(text, encoding="utf-8")

    combined = "\n\n---\n\n".join(outputs)
    out = Path(args.out) if args.out else (target if target.is_dir() else target.parent) / "combined-resume-extracted.txt"
    out.write_text(combined, encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

