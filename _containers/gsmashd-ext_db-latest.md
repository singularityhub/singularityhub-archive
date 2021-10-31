---
id: 2788
name: "gsmashd/ext_db"
branch: "master"
tag: "latest"
commit: "8d09acfb42a45429d696e1bcf343611bf8dbd5ff"
version: "1c9a3ae65a7063ff829029891ebf2a41"
build_date: "2018-05-22T12:50:45.174Z"
size_mb: 76
size: 27942943
sif: "https://datasets.datalad.org/shub/gsmashd/ext_db/latest/2018-05-22-8d09acfb-1c9a3ae6/1c9a3ae65a7063ff829029891ebf2a41.simg"
url: https://datasets.datalad.org/shub/gsmashd/ext_db/latest/2018-05-22-8d09acfb-1c9a3ae6/
recipe: https://datasets.datalad.org/shub/gsmashd/ext_db/latest/2018-05-22-8d09acfb-1c9a3ae6/Singularity
collection: gsmashd/ext_db
---

# gsmashd/ext_db:latest

```bash
$ singularity pull shub://gsmashd/ext_db:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%runscript
/bin/bash

%files

%environment
export TEST=test_var

%post
cat /etc/lsb-release
uname -a 
uname -r
```

## Collection

 - Name: [gsmashd/ext_db](https://github.com/gsmashd/ext_db)
 - License: None

