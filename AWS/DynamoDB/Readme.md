## # **DynamoDB**
A fully managed NoSQL database service.

- a non-relational database, based on Casandra

- comes with two different capacity modes

- on-demand: scales based on the number of requests and you only pay per consumed read or write capacity unit

- provisioned: define how many read/write capacity units are needed and pay a fixed price per month - you can use auto-scaling policies together with CloudWatch alarms to scale based on work loads

- a (unique) primary key is either built via the hash key or the hash key and range key

- Global (can be created any time) and Local (only when your table is created) Secondary Indexes help you to allow additional access patterns

- can use [streams](https://blog.awsfundamentals.com/aws-dynamodb-streams "streams") to trigger other services like Lambda on create/update/delete events

- Time-to-Live (TTL) attribute allows for automatic expiry of items

- global tables can span multiple regions and automatically sync data between them

- [encryption](https://blog.awsfundamentals.com/a-short-but-extensive-guide-for-securing-your-dynamodb-data-ebceb4ee9bd8 "encryption") of tables by default: either via KMS keys managed by AWS or the customer itself

- a set of different [data types](https://blog.awsfundamentals.com/aws-dynamodb-data-types "data types") (scalar, document, set)