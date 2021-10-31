---
id: 1575
name: "singularityhub/ubuntu"
branch: "master"
tag: "latest"
commit: "badc772f6365321ed9e384156e09cc5724b16c69"
version: "9b7990e50a78b519f45a5971a36024ad"
build_date: "2019-07-27T08:14:02.049Z"
size_mb: 208.0
size: 92880927
sif: "https://datasets.datalad.org/shub/singularityhub/ubuntu/latest/2019-07-27-badc772f-9b7990e5/9b7990e50a78b519f45a5971a36024ad.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/singularityhub/ubuntu/latest/2019-07-27-badc772f-9b7990e5/
recipe: https://datasets.datalad.org/shub/singularityhub/ubuntu/latest/2019-07-27-badc772f-9b7990e5/Singularity
collection: singularityhub/ubuntu
---

# singularityhub/ubuntu:latest

```bash
$ singularity pull shub://singularityhub/ubuntu:latest
```

## Singularity Recipe

```singularity
# Copyright (c) 2015-2016, Gregory M. Kurtzer. All rights reserved.
# 
# "Singularity" Copyright (c) 2016, The Regents of the University of California,
# through Lawrence Berkeley National Laboratory (subject to receipt of any
# required approvals from the U.S. Dept. of Energy).  All rights reserved.

BootStrap: debootstrap
OSVersion: trusty
MirrorURL: http://us.archive.ubuntu.com/ubuntu/


%runscript
    echo "This is what happens when you run the container..."


%post
    echo "Hello from inside the container"
    sed -i 's/$/ universe/' /etc/apt/sources.list
    apt-get -y install vim
```

## Collection

 - Name: [singularityhub/ubuntu](https://github.com/singularityhub/ubuntu)
 - License: [MIT License](https://api.github.com/licenses/mit)

