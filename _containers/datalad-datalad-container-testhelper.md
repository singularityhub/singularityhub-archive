---
id: 2837
name: "datalad/datalad-container"
branch: "master"
tag: "testhelper"
commit: "208665e1d1f286e453eebc9fff2849b57d9d96f1"
version: "4a24a5a578b6ea9cb93abed9699b4e93"
build_date: "2021-04-02T14:44:30.369Z"
size_mb: 62
size: 21512223
sif: "https://datasets.datalad.org/shub/datalad/datalad-container/testhelper/2021-04-02-208665e1-4a24a5a5/4a24a5a578b6ea9cb93abed9699b4e93.simg"
url: https://datasets.datalad.org/shub/datalad/datalad-container/testhelper/2021-04-02-208665e1-4a24a5a5/
recipe: https://datasets.datalad.org/shub/datalad/datalad-container/testhelper/2021-04-02-208665e1-4a24a5a5/Singularity
collection: datalad/datalad-container
---

# datalad/datalad-container:testhelper

```bash
$ singularity pull shub://datalad/datalad-container:testhelper
```

## Singularity Recipe

```singularity
#
# This produces a minimal image that can be used for testing the
# extension itself.
#

Bootstrap:docker
From:debian:stable-slim
```

## Collection

 - Name: [datalad/datalad-container](https://github.com/datalad/datalad-container)
 - License: [Other](None)

