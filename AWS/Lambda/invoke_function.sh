# This command will invoke the Lambda function and store the output in the output.json file.

aws lambda invoke --function-name MyLambdaFunction --payload "{}" output.json