---
id: 2074
name: "singularityhub/centos"
branch: "master"
tag: "latest"
commit: "b342d16be73529a963b934d6b2f98623a6fdc0ab"
version: "e2b7b812fc4c546ab3e904bce82c43ab"
build_date: "2019-07-26T21:13:44.271Z"
size_mb: 361
size: 115068959
sif: "https://datasets.datalad.org/shub/singularityhub/centos/latest/2019-07-26-b342d16b-e2b7b812/e2b7b812fc4c546ab3e904bce82c43ab.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/singularityhub/centos/latest/2019-07-26-b342d16b-e2b7b812/
recipe: https://datasets.datalad.org/shub/singularityhub/centos/latest/2019-07-26-b342d16b-e2b7b812/Singularity
collection: singularityhub/centos
---

# singularityhub/centos:latest

```bash
$ singularity pull shub://singularityhub/centos:latest
```

## Singularity Recipe

```singularity
# Copyright (c) 2015-2016, Gregory M. Kurtzer. All rights reserved.
# 
# "Singularity" Copyright (c) 2016, The Regents of the University of California,
# through Lawrence Berkeley National Laboratory (subject to receipt of any
# required approvals from the U.S. Dept. of Energy).  All rights reserved.


BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

# If you want the updates (available at the bootstrap date) to be installed
# inside the container during the bootstrap instead of the General Availability
# point release (7.x) then uncomment the following line
#UpdateURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/updates/$basearch/


%runscript
    echo "This is what happens when you run the container..."


%post
    echo "Hello from inside the container"
    yum -y install vim-minimal
```

## Collection

 - Name: [singularityhub/centos](https://github.com/singularityhub/centos)
 - License: [MIT License](https://api.github.com/licenses/mit)

