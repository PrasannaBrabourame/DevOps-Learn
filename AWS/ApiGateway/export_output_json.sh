aws apigateway get-export \
    --rest-api-id "**** API GATEWAY ID" \
    --stage-name "***** STAGE NAME *****" \
    --export-type "swagger" \
    --accepts "application/json" \
    "output_file.json"