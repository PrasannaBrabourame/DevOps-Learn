aws secretsmanager create-secret --name MyExampleSecret \
  --description "My example secret" \
  --secret-string file://secret_values.json
