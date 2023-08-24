## # **CloudFormation**
The fundamental infrastructure-as-code tool at AWS.

- templates are the definition of the infrastructure resources that should be created by CloudFormation and how they are composed

- for each template, CloudFormation will create a stack which is a deployable unit and contains all your resources

- CloudFormation detects change sets for your stacks at deployment time to calculate what create/update/delete command it needs to run

- via outputs, you can reference other resources dynamically that may not exist yet

