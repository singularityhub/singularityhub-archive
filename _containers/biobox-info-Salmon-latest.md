---
id: 11336
name: "biobox-info/Salmon"
branch: "master"
tag: "latest"
commit: "2a94cc61c5b2194ccd6b8a0708552aea5ab43c41"
version: "47f7fd79ec7380d95d6a464a374d8f744edd54ae7079f21bea74d43f530c5430"
build_date: "2019-10-22T12:48:14.766Z"
size_mb: 367.80859375
size: 385675264
sif: "https://datasets.datalad.org/shub/biobox-info/Salmon/latest/2019-10-22-2a94cc61-47f7fd79/47f7fd79ec7380d95d6a464a374d8f744edd54ae7079f21bea74d43f530c5430.sif"
url: https://datasets.datalad.org/shub/biobox-info/Salmon/latest/2019-10-22-2a94cc61-47f7fd79/
recipe: https://datasets.datalad.org/shub/biobox-info/Salmon/latest/2019-10-22-2a94cc61-47f7fd79/Singularity
collection: biobox-info/Salmon
---

# biobox-info/Salmon:latest

```bash
$ singularity pull shub://biobox-info/Salmon:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: combinelab/salmon

%environment
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

%post

%labels
MAINTAINER BioBox
Version v1.0
```

## Collection

 - Name: [biobox-info/Salmon](https://github.com/biobox-info/Salmon)
 - License: None

