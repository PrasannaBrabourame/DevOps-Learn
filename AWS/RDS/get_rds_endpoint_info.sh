aws rds describe-db-instances --query "DBInstances[*].{DBName:DBName, Endpoint:Endpoint.Address, Port:Endpoint.Port}"
