---
id: 5571
name: "ZhifangYe/cpac_build"
branch: "master"
tag: "latest"
commit: "c4a6f6c9de034343d37361ec26a00e688a5982b8"
version: "f9f5831ad36d0677b174399b4985f2d6"
build_date: "2019-03-19T05:26:48.146Z"
size_mb: 3941
size: 1553850399
sif: "https://datasets.datalad.org/shub/ZhifangYe/cpac_build/latest/2019-03-19-c4a6f6c9-f9f5831a/f9f5831ad36d0677b174399b4985f2d6.simg"
url: https://datasets.datalad.org/shub/ZhifangYe/cpac_build/latest/2019-03-19-c4a6f6c9-f9f5831a/
recipe: https://datasets.datalad.org/shub/ZhifangYe/cpac_build/latest/2019-03-19-c4a6f6c9-f9f5831a/Singularity
collection: ZhifangYe/cpac_build
---

# ZhifangYe/cpac_build:latest

```bash
$ singularity pull shub://ZhifangYe/cpac_build:latest
```

## Singularity Recipe

```singularity
# C-PAC: Configurable Pipeline for the Analysis of Connectomes
# URL: https://github.com/FCP-INDI/C-PAC

BootStrap: docker
From: fcpindi/c-pac:release-v1.4.1

%labels
Author zhifang.ye.fghm@gmail.com
Build-date 03/19/2019
Vendor Ubuntu:Xenial
Version 1.4.1

%runscript
    exec /code/run.py "$@"

%post
    #------------------------------------------------------------------------------
    # Change timezone to Shanghai
    #------------------------------------------------------------------------------
    ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
    dpkg-reconfigure --frontend noninteractive tzdata
    #------------------------------------------------------------------------------
    # Create local binding point for our HPC
    #------------------------------------------------------------------------------
    mkdir /seastor
    mkdir /brain
    mkdir /lustre
```

## Collection

 - Name: [ZhifangYe/cpac_build](https://github.com/ZhifangYe/cpac_build)
 - License: None

