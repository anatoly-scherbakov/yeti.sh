---
title: "Precious Serverlessness"
date: 2020-12-25T18:53:07+07:00
draft: false
---

This article compares pricing for RDS, Aurora Provisioned, and Aurora Serverless database offerings for PostgreSQL at Amazon Web Services.

<!--more-->

I am trying to determine which model of PostgreSQL storage is optimal for us. Let us compare the pricing for different options AWS provides us with.

To do this, we need to compare the price.

### Aurora ACUs and instance sizes

For RDS and Aurora On Demand, the price per hour depends on the instance size. For Aurora Serverless, it depends on the number of ACUs we are using.

> Instead of provisioning and managing database servers, you specify Aurora capacity units (ACUs). Each ACU is a combination of approximately 2 gigabytes (GB) of memory, corresponding CPU, and networking. Database storage automatically scales from 10 gibibytes (GiB) to 128 tebibytes (TiB), the same as storage in a standard Aurora DB cluster.

[(Source.)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.how-it-works.html)

Here is a comparison (instance sizes are from [here](https://aws.amazon.com/rds/instance-types/)).

| Type         | vCPU count | RAM size, GB | Equivalent ACU count               |
| ------------ | ---------- | ------------ | ---------------------------------- |
| db.t3.micro  | 2          | 1            | 1 *(you can't get half of an ACU)* |
| db.t3.small  | 2          | 2            | 1                                  |
| db.t3.medium | 2          | 4            | 2                                  |
| db.t3.large  | 2          | 8            | 4                                  |
| db.t3.xlarge | 4          | 16           | 8                                  |

## The price comparison

Instance prices are for `us-west-2` (Oregon).

| Size         | [RDS](https://aws.amazon.com/rds/postgresql/pricing/) | [Aurora On-Demand](https://aws.amazon.com/rds/aurora/pricing/) | [Aurora Serverless](https://aws.amazon.com/rds/aurora/pricing/) |
| ------------ | ----------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| db.t3.micro  | $0.018                                                | —                                                            | $0.06                                                        |
| db.t3.small  | $0.036                                                | —                                                            | $0.06                                                        |
| db.t3.medium | $0.072                                                | $0.082                                                       | $0.12                                                        |
| db.t3.large  | $0.145                                                | $0.164                                                       | $0.24                                                        |

## When is Aurora worth the while?

The only reason where Serverless might be better than non-Serverless is scaling capability. If the database is unused, it may be paused. Let us do the following comparison. For every instance size listed above, we will compare:

- An RDS or Aurora On Demand instance running 24×7,
- and an Aurora Serverless database of comparable size running for only the *fraction* of the time.

What should the `fraction` value be in order to get a profit?

The formula will be:

```
instance_price / serverless_price × 100%
```

| Instance     | Serverless vs RDS | Serverless vs Aurora On Demand |
| ------------ | ----------------- | ------------------------------ |
| db.t3.micro  | 30%               | —                              |
| db.t3.small  | 60%               | —                              |
| db.t3.medium | 60%               | 68%                            |
| db.t3.large  | 60%               | 68%                            |

You can interpret this table like this: in order to get Aurora performance similar to RDS instance `db.t3.medium` for the same or lower price, you need to keep the Aurora DB online for 60% (or less) of the whole time.

## Caveats

- On production, when a user sends a request while Aurora cluster is paused, the cluster will require a few seconds to start, which means increased latency for the user.
- We have noticed issues with auto scaling Aurora databases which I might describe in another post in more detail.

## Conclusion

There are reasons why one could still prefer Aurora over RDS (because of better throughput on the same hardware, etc). I would suggest this as a takeout from this post in case your pattern of load is predictable and stable:

- On production, use Aurora Provisioned (or RDS if you want to save more) — to ensure minimum latency and optimal price;
- On dev/staging/preprod, use Aurora Serverless so that your databases are only spinned up when you are playing with them.