# Interview Resume Coach

中文技术岗应届生面试作战 skill。

它帮助候选人基于真实简历和项目，生成可以直接在面试中说的中文回答：项目介绍、项目难点、方案对比、工程化思考、不会的问题如何稳住，以及如何把面试官引导到自己准备好的深挖点。

重点覆盖：

- Java 后端
- Go 后端
- C++ 后端 / 基础架构
- 通用后端工程
- 前端
- AI 应用
- 数据开发 / 数据分析

## 这个 skill 解决什么问题

很多应届生的项目并不差，但面试表达容易变成：

- 只背技术栈
- 只说做了什么功能
- 讲不出为什么这么设计
- 被问到细节就散
- 不知道怎么把八股题拉回项目
- 为了显得厉害而不小心说过头

这个 skill 的目标不是帮你编经历，而是把真实经历讲得更像工程实践：有背景、有职责、有链路、有取舍、有风险意识，也有后续优化思考。

## 安装

把 `interview-resume-coach` 文件夹放到你的 Codex skills 目录中。

常见位置：

```text
~/.codex/skills/interview-resume-coach
```

或者在当前仓库里直接使用这个 skill 文件夹。

## 上传 GitHub 前注意

不要把真实简历、真实 JD、个人联系方式、学校证件、面试记录或公司内部材料提交到公开仓库。

仓库已经提供 `.gitignore`，默认忽略常见简历和求职材料文件名，但你仍然应该在提交前运行：

```bash
git status
```

确认没有个人文件被加入版本控制。公开示例请放在 `examples/`，并使用匿名内容。

## 使用方式

把你的简历、项目说明或目标 JD 放到：

```text
interview-resume-coach/user-resumes/
```

这个目录是给本地使用者放私人材料的。里面的真实简历文件会被 `.gitignore` 忽略，不应该上传到 GitHub。

支持格式：

- PDF
- DOCX
- DOC（Windows + Microsoft Word 环境下）
- TXT
- Markdown

skill 会优先尝试自动提取文本。也可以手动运行：

```bash
python interview-resume-coach/scripts/extract_resume_text.py interview-resume-coach/user-resumes
```

提取结果会生成在：

```text
interview-resume-coach/user-resumes/combined-resume-extracted.txt
```

文件名建议包含：

```text
简历
resume
cv
项目
project
jd
```

然后用类似 prompt：

```text
使用 $interview-resume-coach，基于我的简历，帮我准备 Java 后端项目面试。
```

```text
面试官问：你这个项目最大的难点是什么？请给我一个 2 分钟项目吟唱版。
```

```text
我投的是 Go 后端岗位，把这个回答改得更偏 context、goroutine、接口设计和服务稳定性。
```

```text
我投的是 C++ 后端，面试官问为什么用线程池，帮我基于项目回答。
```

```text
这个问题我不会，帮我生成一个诚实但不露怯的回答，并引导回我的项目。
```

## 输出示例

典型输出会包含：

```text
可直接说的版本
如果面试官深挖，可以补充
你可以主动引导到
不要说太满 / 使用前确认
```

项目准备模式会输出：

```text
项目定位
核心卖点
项目吟唱版
可深挖技术点
危险追问
补强建议
```

## 真实性边界

这个 skill 会尽量增强表达，但不会主动编造：

- 真实用户
- 生产流量
- 线上事故
- 性能指标
- 公司经历
- 技术栈使用
- 项目所有权

如果答案需要信息支撑，它会用 `[需要你确认: ...]` 标记。

## 仓库结构

```text
interview-resume-coach/
  SKILL.md
  agents/openai.yaml
  references/
    answer-patterns.md
    company-role-adaptation.md
    interview-control.md
    project-ammo.md
    resume-analysis.md
    resume-diagnosis.md
    role-playbooks.md
examples/
  sample-resume-cn.md
  sample-prompts.md
  sample-output.md
```

## 适合谁

- 中文互联网技术岗应届生
- 准备校招、实习、社招初级岗位的候选人
- 项目经历有内容，但表达不够工程化的人
- 想练习 Java / Go / C++ 后端项目深挖的人

## 不适合什么

- 编造不存在的项目经历
- 替代真实技术学习
- 伪装生产经验
- 在不了解项目的情况下硬背长稿

面试里真正稳的是：你知道自己做了什么，也知道自己没做什么；能讲清取舍，比堆名词更有说服力。
