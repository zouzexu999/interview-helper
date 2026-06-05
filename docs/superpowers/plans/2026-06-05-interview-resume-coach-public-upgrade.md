# Interview Resume Coach Public Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade `interview-resume-coach` into a public GitHub-ready Chinese technical interview skill for new graduates.

**Architecture:** Keep `SKILL.md` concise as the orchestration layer. Move detailed reusable knowledge into focused reference files: resume diagnosis, project ammo, answer patterns, role playbooks, interview control, and company adaptation. Add repository-level README and examples so external users can understand and try the skill quickly.

**Tech Stack:** Codex skill markdown, YAML frontmatter, examples in Markdown, skill-creator validation.

---

### Task 1: Core Skill Workflow

**Files:**
- Modify: `interview-resume-coach/SKILL.md`

- [ ] **Step 1: Replace the current workflow with a public-ready Chinese technical interview workflow**

Include: Chinese-first output, supported roles, input discovery, resume fact discipline, answer mode selection, follow-up control, and references to one-level resource files.

### Task 2: Reference Library

**Files:**
- Modify: `interview-resume-coach/references/answer-patterns.md`
- Modify: `interview-resume-coach/references/resume-analysis.md`
- Modify: `interview-resume-coach/references/company-role-adaptation.md`
- Create: `interview-resume-coach/references/resume-diagnosis.md`
- Create: `interview-resume-coach/references/project-ammo.md`
- Create: `interview-resume-coach/references/role-playbooks.md`
- Create: `interview-resume-coach/references/interview-control.md`

- [ ] **Step 1: Expand answer modes**

Cover concise answers, project chant, deep dives, unknown-question recovery, eight-part essay to project bridging, and interviewer rhythm control.

- [ ] **Step 2: Add backend language playbooks**

Cover Java, Go, C++, and language-neutral backend engineering.

- [ ] **Step 3: Add resume diagnosis and project ammo generation**

Define how to turn a resume project into strengths, weak spots, safe upgrades, and prepared deep-dive material.

### Task 3: Public Repository Materials

**Files:**
- Create: `README.md`
- Create: `examples/sample-resume-cn.md`
- Create: `examples/sample-prompts.md`
- Create: `examples/sample-output.md`

- [ ] **Step 1: Add README**

Explain positioning, installation/copying, usage prompts, safety boundary, and file structure.

- [ ] **Step 2: Add examples**

Provide an anonymized backend resume snippet, prompt examples, and a representative output.

### Task 4: Validation

**Files:**
- Validate: `interview-resume-coach`

- [ ] **Step 1: Run skill validation**

Run:

```powershell
$env:PYTHONUTF8='1'; python C:/Users/Administrator/.codex/skills/.system/skill-creator/scripts/quick_validate.py e:/skills/interview-resume-coach
```

Expected: `Skill is valid!`

- [ ] **Step 2: Scan for placeholders**

Run:

```powershell
Select-String -Path 'e:/skills/interview-resume-coach/**/*.md','e:/skills/README.md','e:/skills/examples/*.md' -Pattern 'TODO|TBD|placeholder'
```

Expected: no unresolved placeholder text.
