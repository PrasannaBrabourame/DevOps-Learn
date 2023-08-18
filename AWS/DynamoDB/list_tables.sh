# querying for our tables
# you can specify the region via `--region`
# else the default will be used
aws dynamodb list-tables --region eu-central-1

# the response will include a list of all tables
{
    "TableNames": [
        "TableA",
        "TableB",
        "TableC"
    ]
}
