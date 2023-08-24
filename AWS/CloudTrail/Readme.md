## # **CloudTrail**
Monitor and record account activity across your AWS infrastructure (check this article for the differences with CloudWatch)

- records events in your AWS account as JSON

- you can decide which events are tracked by creating trails

- a trail will forward your events to an S3 bucket and/or CloudWatch log group

- CloudTrail records different types of audit events

- Management events: infrastructure management operations, e.g. IAM policy adjustments or VPC subnet creations

- Data Events: events that retrieve, delete or modify data within your AWS account, e.g. CRUD operations on DynamoDB or a GET for an object in S3

- Insight Events: records anomalies in your API usage of your account based on historical usage patterns

- you can additionally define filter rules to not track all events of a certain type, but only a subset. Maybe you're interested in tracking modifications and deletions in DynamoDB, but not reads.