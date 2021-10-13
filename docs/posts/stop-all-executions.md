---
title: Stop All Executions
source: https://stackoverflow.com/a/64845077/1245471
---

AWS_PROFILE=cbs-dev aws stepfunctions list-executions \
  --state-machine-arn arn:aws:states:us-west-2:517499888515:stateMachine:cbs-dev-builder-customer-types-distributor \
  --status-filter RUNNING \
  --query "executions[*].{executionArn:executionArn}" \
  --output text | \
AWS_PROFILE=cbs-dev xargs -I {} aws stepfunctions stop-execution \
  --execution-arn {} 
