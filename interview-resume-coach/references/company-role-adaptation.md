# Company And Role Adaptation

Use this reference when the user provides a target company, job description, or company type.

## Adaptation Output

```text
通用版本
面向该岗位的强调点
可以替换进回答里的句子
不要说太满的地方
建议准备的追问
```

## Large Internet Company

Emphasize:

- foundation knowledge
- code quality
- scalability thinking
- clear ownership
- debugging and observability
- data consistency and reliability
- collaboration and documentation

Tone: structured, calm, less exaggerated.

Avoid: fake high concurrency, fake microservices, vague "大规模".

## Startup

Emphasize:

- fast delivery
- ownership
- pragmatic tradeoffs
- ability to close the loop
- learning speed
- simple solution first, scalable path later

Tone: direct, outcome-oriented, less process-heavy.

## State-Owned / Bank / Traditional Enterprise

Emphasize:

- stability
- security
- process awareness
- documentation
- data correctness
- permission and audit
- maintainability

Tone: reliable, careful, risk-aware.

## Outsourcing / Delivery-Oriented Company

Emphasize:

- requirements understanding
- communication
- delivery predictability
- issue tracking
- interface alignment
- documentation and maintainability

Tone: practical, collaborative, deadline-aware.

## JD Keyword Mapping

Map JD keywords to answer emphasis:

- `高并发`: pressure testing, bottleneck analysis, caching, async, rate limiting, but only claim real experience if supported
- `微服务`: service boundaries, RPC, config, observability, deployment, only if supported
- `Redis`: cache scenario, key design, expiration, consistency, penetration/breakdown/avalanche only if relevant
- `消息队列`: async decoupling, retry, idempotency, ordering, dead-letter handling
- `MySQL`: schema, index, transaction, slow query, locking
- `Go`: context, goroutine, error handling, service simplicity
- `C++`: Linux, network, memory, concurrency, performance
- `Spring`: layering, transaction, configuration, exception handling
- `前端工程化`: components, state, build, routing, API states
- `AI/LLM`: data, prompt, evaluation, hallucination control, latency, cost

## Adaptation Rule

Do not change the underlying facts. Change:

- opening emphasis
- selected engineering detail
- tradeoff language
- follow-up hook
- risk disclaimer
