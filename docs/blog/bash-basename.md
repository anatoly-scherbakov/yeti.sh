---
title: Extract base name & extension in bash
source:
    $id: https://stackoverflow.com/a/14703709/1245471
    title: Extract filename and extension in Bash | Stack Overflow
---

```shell
bash-3.2$ FILENAME=somefile.tar.gz
bash-3.2$ echo "${FILENAME%%.*}"
somefile
bash-3.2$ echo "${FILENAME%.*}"
somefile.tar
```
