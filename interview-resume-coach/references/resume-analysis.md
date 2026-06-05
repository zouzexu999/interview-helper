# Resume Analysis

Use this reference for quickly reading resume or project files.

## File Reading Priorities

Prefer:

- resume or CV files
- project descriptions
- target JD files
- notes written by the candidate

Look for Chinese and English file names:

- `简历`
- `项目`
- `resume`
- `cv`
- `project`
- `jd`

## Extraction Table

For each project, build this mental table:

```text
项目名:
目标岗位:
项目类型:
业务背景:
技术栈:
个人职责:
核心链路:
最能讲的难点:
可比较的方案:
工程化细节:
真实结果:
缺失信息:
风险表述:
```

## Evidence Discipline

Treat the resume as evidence, not as a prompt to invent.

Strong evidence:

- named module ownership
- concrete implementation details
- real metrics
- real deployment or user scope
- clear team role

Weak evidence:

- only listing frameworks
- "参与开发" without scope
- "优化性能" without before/after or method
- "高并发" without traffic or pressure test
- "负责项目" without concrete responsibility

When evidence is weak, answer with:

```text
这部分简历里没有写得很细，我建议你先确认[信息]。在不编造的前提下，可以把它讲成[安全表达]。
```

## Interview Readiness Checklist

For each main project, the candidate should be able to answer:

- Why does this project exist?
- What exactly did you do?
- What was the hardest part?
- Why did you choose this方案?
- What would break if scale increases?
- How did you verify it worked?
- What would you improve next?
- Which part was not done by you?

If the candidate cannot answer three or more, generate preparation questions before drafting a long answer.
