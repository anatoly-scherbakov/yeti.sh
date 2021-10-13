---
title: Stop All Executions
source: https://stackoverflow.com/a/64845077/1245471
---

```shell
export AWS_PROFILE=...
export STATE_MACHINE_ARN=...
aws stepfunctions list-executions \
  --state-machine-arn $STATE_MACHINE_ARN \
  --status-filter RUNNING \
  --query "executions[*].{executionArn:executionArn}" \
  --output text | \
xargs -I {} aws stepfunctions stop-execution \
  --execution-arn {} 
```
