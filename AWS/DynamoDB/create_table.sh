aws dynamodb create-table \
    --table-name MyTable \
    --attribute-definitions AttributeName=MyAttribute,AttributeType=S \
    --key-schema AttributeName=MyAttribute,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST
