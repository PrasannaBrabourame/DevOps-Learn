## # **Simple Notification Service (SNS)**
Managed messaging service to send notifications to customers or other services.

- consumers can subscribe to topics and then will receive all messages publish to this topic

- comes in two different types, equal to SQS: FIFO and Standard

- messages can be archived by sending them to Kinesis Data Firehose (and afterward to either S3 or Redshift)