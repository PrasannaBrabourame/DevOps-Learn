provider "aws" {
  region = "us-east-1"  # Change this to your desired region
}

resource "aws_cloudwatch_log_group" "example" {
  name = "MyLogGroup"  # Change this to the desired log group name

  retention_in_days = 7  # Set the desired retention period in days
}