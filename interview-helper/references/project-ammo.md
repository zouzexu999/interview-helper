# Project Ammo

Use this reference to generate a "项目弹药库" for each resume project.

## Ammo Pack Format

```text
项目一句话定位
业务/用户背景
我的职责
核心链路
三个可讲亮点
两个可深挖技术点
一个方案对比
一个踩坑/风险点
一个后续优化方向
危险问题与避坑回答
```

## Three-Layer Project Story

Layer 1: User-visible value

- what problem the project solves
- who benefits
- what workflow becomes easier

Layer 2: Engineering implementation

- modules and boundaries
- data flow
- API or component design
- storage, cache, async, concurrency, deployment, or model/data pipeline

Layer 3: Engineering maturity

- tradeoffs
- reliability
- observability
- testing
- maintainability
- security and permissions
- future scaling path

## Good Ammo Types

- Boundary: "这个模块和其他模块的边界是什么"
- Tradeoff: "为什么不用另一个方案"
- Failure: "如果请求失败、数据异常、并发冲突怎么办"
- Verification: "怎么证明它是对的"
- Scale-up: "数据量/并发量上来后怎么改"
- Maintenance: "后续需求变化时怎么扩展"

## Dangerous Ammo

Avoid hooks that lead to unsupported depth:

- high concurrency without numbers
- distributed transactions without implementation
- Kubernetes/cloud-native without deployment facts
- model deployment without inference details
- Redis/MQ without actual use
- "微服务" when the project is a monolith

When a dangerous topic is tempting, convert it to:

```text
这个项目里我没有真正落到[复杂主题]，但如果规模上来，我会优先从[可解释的第一步]做起。
```

## Backend Project Ammo

For backend projects, look for:

- API contract and error codes
- database schema and indexes
- transaction boundaries
- authentication and authorization
- cache use and consistency
- async processing and retry
- idempotency and duplicate submission
- logging and traceability
- deployment config and environment separation
- pressure testing or bottleneck analysis

## C++ Project Ammo

For C++ backend or systems projects, look for:

- network model: blocking, non-blocking, epoll, reactor, thread pool
- memory ownership: RAII, smart pointers, object lifetime, buffer management
- concurrency: locks, atomics, queues, thread safety
- performance: copies, allocation, cache locality, profiling
- Linux: sockets, file IO, process/thread model, build tools
- failure handling: connection close, timeout, malformed requests

## Go Project Ammo

For Go backend projects, look for:

- handler-service-repository layering
- `context.Context` for timeout and cancellation
- goroutine lifecycle and leak prevention
- channel use and when not to use channels
- error wrapping and logging
- database connection pool
- graceful shutdown
- Docker/cloud deployment

## Java Project Ammo

For Java backend projects, look for:

- Controller-Service-Mapper layering
- Spring Boot configuration
- transaction annotation boundaries
- MyBatis/JPA query design
- Redis cache and invalidation if used
- MQ retry/idempotency if used
- unified response and exception handling
- authentication and permission checks

