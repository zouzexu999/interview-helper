# Resume Diagnosis

Use this reference when the user wants to improve interview readiness from a resume or project paragraph.

## Diagnosis Output

Produce:

```text
项目可信度
亮点
薄弱点
可包装但不能编造的地方
面试官最可能追问
建议补充到简历/口述里的信息
```

## What To Extract

- role target: Java, Go, C++, backend, frontend, AI, data, full-stack, product-tech hybrid
- project type: course, personal, lab, internship, competition, open source
- project problem: who uses it, what problem it solves
- candidate ownership: independently built, module owner, team collaborator, learner
- stack: language, framework, database, cache, queue, deployment, data/model tools
- engineering details: auth, permission, validation, exception, logging, tests, deployment, performance
- measurable facts: time, scale, users, data volume, latency, accuracy, throughput
- unverified claims: any impressive claim unsupported by evidence

## Scoring Heuristic

Use a 1-5 score only when helpful:

- `1`: only tech stack list, no project story
- `2`: has feature description but weak personal contribution
- `3`: clear module and implementation, limited engineering depth
- `4`: has difficulty, tradeoff, and quality practices
- `5`: has real users/business context, metrics, tradeoffs, and strong ownership

## Upgrade Weak Lines

Weak:

```text
使用 Gin 实现后端接口。
```

Stronger:

```text
围绕业务流程拆分 REST 接口，处理参数校验、错误码、数据库读写和接口边界。面试里可以展开讲路由设计、上下文传递、超时控制、日志和部署。
```

Weak:

```text
使用 C++ 完成服务器。
```

Stronger:

```text
把项目讲成服务端链路：网络连接、请求解析、并发模型、内存管理、异常处理、日志排查和性能瓶颈。不要只说用了 C++，要讲为什么 C++ 在这个场景下有价值。
```

Weak:

```text
使用 Spring Boot 完成系统。
```

Stronger:

```text
围绕接口、业务层、数据层和权限边界讲清楚模块职责。可以展开事务、参数校验、统一异常、数据库索引、缓存和接口文档。
```

## Safe Enhancement

Allowed:

- suggest "如果你确实做过，可以补充..."
- convert feature descriptions into engineering concerns
- propose questions the candidate should prepare
- mark unsupported details as confirmation items

Not allowed:

- write fake metrics
- pretend course projects are production systems
- claim team leadership without evidence
- imply the candidate solved high concurrency if no scale is provided
