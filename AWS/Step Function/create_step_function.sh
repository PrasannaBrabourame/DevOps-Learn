aws stepfunctions create-state-machine --name HelloWorldStateMachine \
  --definition file://state_machine_definition.json \
  --role-arn arn:aws:iam::YOUR_ACCOUNT_ID:role/YourStepFunctionsRole
