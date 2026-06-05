# Interview Resume Coach Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a reusable Codex skill that helps graduating candidates answer interview questions from their resume and projects.

**Architecture:** Create one skill folder with a concise `SKILL.md` as the trigger and workflow entry point, plus focused reference files for answer patterns, resume analysis, and company/role adaptation. Keep the skill prompt-oriented because the core work is structured reasoning and answer drafting, not deterministic scripting.

**Tech Stack:** Codex skill markdown, YAML frontmatter, `agents/openai.yaml`, skill-creator validation script.

---

### Task 1: Skill Scaffold

**Files:**
- Create: `interview-resume-coach/SKILL.md`
- Create: `interview-resume-coach/agents/openai.yaml`
- Create: `interview-resume-coach/references/answer-patterns.md`
- Create: `interview-resume-coach/references/resume-analysis.md`
- Create: `interview-resume-coach/references/company-role-adaptation.md`

- [ ] **Step 1: Initialize the skill**

Run:

```powershell
python C:/Users/Administrator/.codex/skills/.system/skill-creator/scripts/init_skill.py interview-resume-coach --path e:/skills --resources references --interface display_name="Interview Resume Coach" --interface short_description="Turn resumes and projects into strong interview answers." --interface default_prompt="Use $interview-resume-coach to answer this interviewer question from my resume and project experience."
```

Expected: a new `interview-resume-coach` folder with required skill files.

### Task 2: Core Skill Instructions

**Files:**
- Modify: `interview-resume-coach/SKILL.md`

- [ ] **Step 1: Replace scaffold text**

Write frontmatter with `name: interview-resume-coach` and a description covering resume-based interview answering, project storytelling, deep-dive guidance, role/company adaptation, and Chinese job-seeking contexts.

- [ ] **Step 2: Add workflow**

Define a workflow that extracts resume facts, identifies question intent, chooses answer depth, drafts a spoken answer, adds likely follow-up questions, and avoids fabricating experience.

### Task 3: Reference Files

**Files:**
- Modify: `interview-resume-coach/references/answer-patterns.md`
- Modify: `interview-resume-coach/references/resume-analysis.md`
- Modify: `interview-resume-coach/references/company-role-adaptation.md`

- [ ] **Step 1: Add answer patterns**

Include concise, project-chant, deep-dive, comparison, unknown-question, and interviewer-control patterns.

- [ ] **Step 2: Add resume analysis guidance**

Include extraction fields for projects, technical depth, business value, personal contribution, metrics, and safe assumptions.

- [ ] **Step 3: Add company and role adaptation guidance**

Include style changes for backend, frontend, data/AI, product-oriented, large company, startup, and role-specific interviews.

### Task 4: Validation

**Files:**
- Validate: `interview-resume-coach`

- [ ] **Step 1: Run quick validation**

Run:

```powershell
python C:/Users/Administrator/.codex/skills/.system/skill-creator/scripts/quick_validate.py e:/skills/interview-resume-coach
```

Expected: validation passes.
