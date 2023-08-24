## # **Lambda**
The core building block for serverless applications.

- integrates natively with different services like SQS or SNS

- can run on x86 or ARM/Graviton2 architectures

- compute-resources (vCPU) are sized based on memory settings

- dynamic configuration with [environment variables](https://blog.awsfundamentals.com/aws-lambda-environment-variables-best-practices-and-common-use-cases "environment variables")

- AWS abstracts away all your infrastructure and runs your functions in micro-containers

- can be attached to VPCs - due to the Hyperplane integration in 2019, this doesn't come with restrictions like ENI bootstrap or private IP consumption anymore

- can be triggered via notifications from other services like SQS or S3

- destinations: on successful or failed executions you can invoke other services to handle those events

- exposure of your functions to the internet either via API Gateway or Function URLs

- dependencies can be extracted into Layers that can be attached to one or several functions

- usage based [pricing](https://blog.awsfundamentals.com/aws-lambda-pricing-a-complete-guide-to-understanding-the-cost-of-the-serverless-service "pricing")