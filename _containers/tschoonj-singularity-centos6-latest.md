---
id: 9249
name: "tschoonj/singularity-centos6"
branch: "master"
tag: "latest"
commit: "95df90bb644138d5a415fde4fe27b910b77df8c3"
version: "c967e016fa4c63c4c332474376f5dfa7"
build_date: "2020-08-12T03:02:58.302Z"
size_mb: 682
size: 215437343
sif: "https://datasets.datalad.org/shub/tschoonj/singularity-centos6/latest/2020-08-12-95df90bb-c967e016/c967e016fa4c63c4c332474376f5dfa7.simg"
url: https://datasets.datalad.org/shub/tschoonj/singularity-centos6/latest/2020-08-12-95df90bb-c967e016/
recipe: https://datasets.datalad.org/shub/tschoonj/singularity-centos6/latest/2020-08-12-95df90bb-c967e016/Singularity
collection: tschoonj/singularity-centos6
---

# tschoonj/singularity-centos6:latest

```bash
$ singularity pull shub://tschoonj/singularity-centos6:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:6

%post

# Deps
yum groupinstall -y 'Development Tools'
yum install -y wget glibc-devel.i686 libgcc.i686 libstdc++.i686 texinfo pcre-devel
yum clean all -y
```

## Collection

 - Name: [tschoonj/singularity-centos6](https://github.com/tschoonj/singularity-centos6)
 - License: None

