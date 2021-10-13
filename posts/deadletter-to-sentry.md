---
title: Deadletter queue to Sentry
---

When an AWS λ function tied to SQS queue fails multiple times, after certain number of retries the message which fails the queue is sent to deadletter queue. Let's alert Sentry if that happens.

```terraform
locals {
  sentry_dsn = "https://..."
}


module sqs_to_trigger_lambda {
  source  = "Recall-Masters/sqs-lambda-trigger/aws"
  version = "0.0.5"

  aws_sqs_queue_name = "${local.application_name}-badaboom"

  aws_lambda_function_name          = aws_lambda_function.badaboom.function_name
  aws_lambda_function_iam_role_name = aws_iam_role.badaboom.name

  batch_size                         = 1
  maximum_batching_window_in_seconds = 10

  alarm_actions = [module.dead_letter_notification.sns_topic.id]
}


module dead_letter_notification {
  source  = "Recall-Masters/sns-to-sentry/aws"
  version = "0.0.4"

  name        = "${local.application_name}-deadletter-notification"
  sentry_dsn  = local.sentry_dsn
  message     = "Nothing worked and we now have something in deadletter queue! AAAA!!!"
  environment = var.environment
}
```
