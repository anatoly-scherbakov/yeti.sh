---
title: Python + λ - .dist-info = DistributionNotFound
date: "2020-12-29T19:06:47+07:00"
draft: false
---

Cleaning up things too much may cause problems.

<!--more-->

## Problem

I encountered the following error today trying to use AWS own Python [stepfunctions](https://pypi.org/project/stepfunctions/) library in AWS Lambda:

```python
[ERROR] DistributionNotFound: The 'packaging>=20.0' distribution was not found and is required by sagemaker
    
Traceback (most recent call last):
  File "/var/lang/lib/python3.8/imp.py", line 234, in load_module
    return load_source(name, filename, file)
  File "/var/lang/lib/python3.8/imp.py", line 171, in load_source
    module = _load(spec)
  File "<frozen importlib._bootstrap>", line 702, in _load
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 783, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/var/task/[DATA EXPUNGED].py", line 10, in <module>
  
  # [DATA EXPUNGED]
    
    from stepfunctions.steps import Chain
  File "/var/task/stepfunctions/__init__.py", line 19, in <module>
    __version__ = pkg_resources.require("stepfunctions")[0].version
  File "/var/lang/lib/python3.8/site-packages/pkg_resources/__init__.py", line 899, in require
    needed = self.resolve(parse_requirements(requirements))
  File "/var/lang/lib/python3.8/site-packages/pkg_resources/__init__.py", line 785, in resolve
    raise DistributionNotFound(req, requirers)
```

## Reason & Solution

In our self-cooked, GNU Make powered toolbox to deploy and manage AWS Lambda functions, we had the following:

```shell
rm -rf ./build/*.dist-info
```

We wanted to reduce the size of the deployment package. However, after removing this line, everything started working perfectly.

## Attribution

Idea belongs to [this GitHub comment](https://github.com/Julian/jsonschema/issues/584#issuecomment-668695019). It was hard to google though, which prompted me to write this post for my own future reference. Cheers.