---
title: How to remove multiple tables in Redshift by wildcard
date: 2021-05-24
---

You need to remove all tables in Redshift which contain the word `staging` in their name. How do you do that?

<!--more-->

## Method 1 (SQL only)

Run:

```sql
SELECT
    'DROP TABLE ' ||
    LISTAGG("table", ', ') ||
    ';'
FROM
    svv_table_info
WHERE
    "table" LIKE 'staging_%';
```

which will print, for example, this:

```sql
DROP TABLE staging_077815128468462e9de8ca6fec22f284, staging_abc, staging_123;
```

But, this will only display non-empty tables. More details in my [answer at StackOverflow](https://stackoverflow.com/a/67579151/1245471).

## Method 2 (Using AWS CLI & Redshift Data API)

```bash
aws redshift-data list-tables --cluster-identifier CLUSTER --database DATABASE --db-user USER | jq -r '.Tables | map(.name) | map(select(contains("staging"))) | "DROP TABLE " + join(", ") + ";"' | xclip -sel clip
```

Now go to Redshift Console SQL editor and hit `Ctrl` + `V`.