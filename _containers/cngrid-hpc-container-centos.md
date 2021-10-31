---
id: 3111
name: "cngrid/hpc-container"
branch: "master"
tag: "centos"
commit: "d7cdd47c6ba904afb3ce7e01203c46456aed37d8"
version: "b47b3c457b0b1194bf66bef46d4580de"
build_date: "2018-06-08T16:24:59.637Z"
size_mb: 330
size: 103370783
sif: "https://datasets.datalad.org/shub/cngrid/hpc-container/centos/2018-06-08-d7cdd47c-b47b3c45/b47b3c457b0b1194bf66bef46d4580de.simg"
url: https://datasets.datalad.org/shub/cngrid/hpc-container/centos/2018-06-08-d7cdd47c-b47b3c45/
recipe: https://datasets.datalad.org/shub/cngrid/hpc-container/centos/2018-06-08-d7cdd47c-b47b3c45/Singularity
collection: cngrid/hpc-container
---

# cngrid/hpc-container:centos

```bash
$ singularity pull shub://cngrid/hpc-container:centos
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

UpdateURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/updates/$basearch/


%runscript
    echo "This is what happens when you run the container..."


%post
    echo "Hello from inside the container"
    yum -y install vim-minimal
```

## Collection

 - Name: [cngrid/hpc-container](https://github.com/cngrid/hpc-container)
 - License: None

