## # **[CloudWatch](https://blog.awsfundamentals.com/aws-cloudwatch-monitoring "CloudWatch")**
- An observability platform that is integrated with almost every AWS service.

- log events: messages that are collected by CloudWatch from other services, always containing a timestamp

- [log groups](https://blog.awsfundamentals.com/aws-cloudwatch-logs-the-comprehensive-guide-for-log-analysis-and-insights "log groups"): a cluster of log messages, related to a service

- log streams: further drill down of messages, e.g. for a specific Lambda micro-container instance or Fargate task

- CloudWatch collects metrics by default from a lot of services, including Lambda, EC2, or ECS

- Default metrics do not come with costs

- X-Ray allows for distributed tracing to understand how a single request interacted with different services

- Alarms can be used to send emails or SMS messages via SNS on certain events or to trigger actions like auto-scaling policies

|Name    |Explanation |
| ------------ | ------------ |
| Logs   | 	The central logging place. Each service logs to CloudWatch. You can also add agents to your custom services to log into CloudWatch.  |
|  Metrics  |  Each service collects metrics. For example, AWS Lambda collects the number of innovations, errors, and timeouts. These can be really helpful for understanding how your system behaves. |
|  Alarms  | Alarms notify you in case of outages or problems. Alarms are based on metrics.  |
| X-Ray  |	X-Ray helps you trace requests across your different services.   |
|  Synthetics  |  	Synthetics are custom scripts or browser-based scripts that check your application's health regularly. |
|  Evidently  | 	Evidently allows you to try out different configurations for different customers.  |