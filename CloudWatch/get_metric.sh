aws cloudwatch get-metric-statistics --namespace "AWS/EC2" --metric-name "CPUUtilization" --start-time "2023-07-31T00:00:00Z" --end-time "2023-07-31T01:00:00Z" --period 300 --statistics Average --dimensions "Name=InstanceId,Value=i-1234567890abcdef0"