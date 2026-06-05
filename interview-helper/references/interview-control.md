# Interview Control

Use this reference to help candidates guide the interview without sounding rehearsed or evasive.

## Control Principle

Do not dodge the question. Answer first, then guide.

Good rhythm:

1. Give direct answer.
2. Anchor to project.
3. Add one engineering detail.
4. Mention a tradeoff.
5. End with a safe hook.

## Safe Hooks

Use hooks that the candidate can actually explain:

- "这里我做过一个方案对比，可以展开讲。"
- "这个点和我项目里的[模块]关系比较大。"
- "如果数据量更大，我会从[方向]优化。"
- "我当时踩过一个坑，后来是这样定位的。"
- "这里我没有上复杂方案，主要是因为项目阶段更适合先保证[目标]。"

## Unsafe Hooks

Avoid hooks that invite questions the candidate cannot answer:

- "这个项目支持高并发" without scale or pressure test
- "我们用了微服务" when there is no service boundary
- "做了分布式事务" without implementation
- "部署到了 Kubernetes" without deployment knowledge
- "模型效果很好" without metrics and evaluation

## Follow-Up Prediction

After drafting an answer, predict:

- interviewer may ask for implementation detail
- interviewer may ask why not another方案
- interviewer may ask scale or performance
- interviewer may ask candidate's exact contribution
- interviewer may ask what went wrong

Give the user short prepared responses.

## Dangerous Question Recovery

For "这是你自己做的吗":

```text
这个项目是[个人/团队]完成的。我本人主要负责[真实范围]，其他部分我有参与联调/理解整体链路，但不会把不是我主导的部分说成自己独立完成。
```

For "有真实用户/上线吗":

```text
这个项目目前更偏[课程/个人/实验/内部实践]，没有大规模真实线上用户。我会把它当成工程训练项目来讲，重点是完整链路、设计取舍和如果上线还需要补哪些能力。
```

For "高并发怎么做":

```text
这个项目没有真实高并发场景，所以我不会说自己已经解决了高并发。但如果规模上来，我会先做压测定位瓶颈，再从数据库索引、缓存、异步化、限流和部署扩容这些方向逐步处理。
```

For "你为什么不用某某技术":

```text
我当时没有直接引入它，主要是因为项目阶段的核心矛盾是[核心目标]。引入新技术会带来[成本]。如果后续出现[触发条件]，再引入会更合理。
```

## Mock Interview Mode

Ask one question at a time.

After the user answers, provide:

```text
反馈
更强版本
下一题
```

Feedback should focus on:

- whether the answer directly answered the question
- whether it used resume facts
- whether it overclaimed
- whether it exposed dangerous follow-up points
- how to make it more engineering-oriented

