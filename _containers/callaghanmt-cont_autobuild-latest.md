---
id: 12354
name: "callaghanmt/cont_autobuild"
branch: "master"
tag: "latest"
commit: "e952ca42997ed8bac7779ed20f586a5158d5e3bf"
version: "8903d0b88e50537abcb9594a4dd12ff3"
build_date: "2020-02-25T12:54:41.951Z"
size_mb: 304.0
size: 112005151
sif: "https://datasets.datalad.org/shub/callaghanmt/cont_autobuild/latest/2020-02-25-e952ca42-8903d0b8/8903d0b88e50537abcb9594a4dd12ff3.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/callaghanmt/cont_autobuild/latest/2020-02-25-e952ca42-8903d0b8/
recipe: https://datasets.datalad.org/shub/callaghanmt/cont_autobuild/latest/2020-02-25-e952ca42-8903d0b8/Singularity
collection: callaghanmt/cont_autobuild
---

# callaghanmt/cont_autobuild:latest

```bash
$ singularity pull shub://callaghanmt/cont_autobuild:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:7
%post
    . /.singularity.d/env/10-docker*.sh

# GNU compiler
%post
    yum install -y \
        gcc \
        gcc-c++ \
        gcc-gfortran
    rm -rf /var/cache/yum/*
```

## Collection

 - Name: [callaghanmt/cont_autobuild](https://github.com/callaghanmt/cont_autobuild)
 - License: None

