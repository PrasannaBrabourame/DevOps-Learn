aws lambda create-function \
  --function-name <function-name> \
  --runtime <runtime> \
  --role <role-arn> \
  --handler <handler> \
  --code <code-location>


# <function-name>: Specify a name for your Lambda function.
# <runtime>: Specify the runtime environment for your function (e.g., python3.8, nodejs14.x).
# <role-arn>: Provide the ARN of the IAM role that the function will assume.
# <handler>: Specify the name of the function's handler (e.g., index.handler for Node.js, filename.lambda_handler for Python).
# <code-location>: Specify the location of the deployment package for the Lambda function code (e.g., S3Bucket=my-bucket,S3Key=my-code.zip).

# Example

# aws lambda create-function \
#   --function-name MyLambdaFunction \
#   --runtime python3.8 \
#   --role arn:aws:iam::123456789012:role/lambda-role \
#   --handler index.handler \
#   --code S3Bucket=my-lambda-bucket,S3Key=lambda-code.zip


