# Role Playbooks

Use this reference to adapt answers by technical direction.

## 通用后端

Emphasize:

- interface boundaries
- data modeling
- transaction and consistency
- cache, async, idempotency, rate limiting when actually relevant
- logging, observability, and debugging
- deployment and maintainability

Good sentence:

```text
我会先把接口边界和数据一致性想清楚，再考虑性能优化，因为后端系统最怕的是功能能跑但边界不清、问题不好排查。
```

## Java 后端

Emphasize:

- Spring Boot layering
- Controller-Service-Mapper/Repository responsibilities
- MyBatis/JPA SQL and index awareness
- transaction propagation and rollback boundaries
- unified exception handling and response format
- Redis/MQ only if present
- permission, login, token, session, or security if present

Useful deep-dive angles:

- "为什么事务放在 Service 层"
- "接口幂等怎么做"
- "缓存和数据库不一致怎么办"
- "MyBatis 查询慢怎么排查"
- "统一异常处理有什么价值"

## Go 后端

Emphasize:

- simplicity and explicit error handling
- Gin/Echo/Fiber route organization if present
- `context.Context` for timeout and cancellation
- goroutine lifecycle and avoiding leaks
- channel use only where it clarifies ownership
- RPC, microservice, Docker, Kubernetes only if actually used
- graceful shutdown and logging

Useful deep-dive angles:

- "为什么 Go 适合这个服务"
- "goroutine 出问题怎么排查"
- "context 超时怎么传递"
- "Go 里错误处理怎么设计"
- "接口层、业务层、数据层怎么拆"

## C++ 后端 / 基础架构

Emphasize:

- Linux and network programming
- concurrency model
- memory ownership and RAII
- performance measurement, not vague "高性能"
- thread safety and lock granularity
- build, deployment, logging, and debugging
- robustness under malformed input or connection failure

Useful deep-dive angles:

- "epoll/reactor/thread pool 为什么这么设计"
- "怎么避免内存泄漏和悬垂指针"
- "锁竞争怎么优化"
- "如何定位性能瓶颈"
- "服务异常退出怎么排查"

## Frontend

Emphasize:

- component boundaries
- state management
- routing and permission
- form/table complexity
- API loading, empty, error, and retry states
- maintainability and collaboration with backend

Useful sentence:

```text
我不会只把页面做出来，还会关注状态流、组件边界和异常态，因为这些决定后续需求变化时维护成本高不高。
```

## AI 应用 / 算法工程

Emphasize:

- data source and quality
- baseline and metric
- model or LLM choice
- error analysis
- inference cost and latency
- deployment and monitoring if present
- business use of model output

Avoid claiming model originality if the project mainly integrates existing models.

## 数据开发 / 数据分析

Emphasize:

- data source and schema understanding
- cleaning and transformation
- SQL quality and performance
- metric definition
- pipeline reliability
- dashboard or business decision value
- anomaly handling

Useful sentence:

```text
我会先确认指标口径，再写查询或看板，因为数据方向最怕的是结果能跑出来但业务含义不一致。
```
