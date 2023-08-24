## # **S3 (Simple Storage Service)**

Durable object storage that is easy to use and almost doesn't have any limitations.

- S3 **asynchronously replicates** your data to all availability zones of your bucket region

- has **no cap** for the number of files within a bucket

- **Server Side Encryption (SSE)**

- **SSE-S3** (Server Side Encryption managed by S3) — S3 manages the data and the encryption keys

- **SSE-C **(Server Side Encryption managed by the Customer) — you’re responsible for your encryption keys

- you can use different encryption keys for different versions of a file in an s3 bucket

- Amazon recommends regular rotation of keys by the customer itself

- **SSE-KMS** (Server Side Encryption managed by AWS, KMS, and the customer) — AWS manages the data key but you're responsible for the customer master key kept in KMS (Key Management Service)