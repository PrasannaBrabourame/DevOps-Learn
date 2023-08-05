aws athena start-query-execution --query-string "SELECT * FROM your_table_name WHERE column1_name = 'some_value'" --result-configuration OutputLocation=s3://your-bucket-name/path-for-query-results/
