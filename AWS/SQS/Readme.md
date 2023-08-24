## # **Simple Queue Service (SQS)**
A queuing service that allows you to build resilient, event-driven architectures.

- another core building block for serverless applications

- allows you to run tasks in the background

- offers different types of queues

- First-In-First-Out (FIFO): executes messages in the order SQS receives them

- Standard Queues: higher throughput but no guarantee of right ordering

- Dead-Letter-Queues (DLQs) allow you to handle failures and retries

- Retention periods define how long a messages stays in your queue until it's either dropped or redriven to a DLQ