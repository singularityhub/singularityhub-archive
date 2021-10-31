---
id: 8529
name: "ZhifangYe/xcpengine_build"
branch: "master"
tag: "latest"
commit: "54b86745d44832b4d7a92e8333d4cb8a5d25f2c0"
version: "ef83ca7561c07d911a24c98ec7e13011"
build_date: "2019-04-21T09:06:21.132Z"
size_mb: 14838
size: 6634418207
sif: "https://datasets.datalad.org/shub/ZhifangYe/xcpengine_build/latest/2019-04-21-54b86745-ef83ca75/ef83ca7561c07d911a24c98ec7e13011.simg"
url: https://datasets.datalad.org/shub/ZhifangYe/xcpengine_build/latest/2019-04-21-54b86745-ef83ca75/
recipe: https://datasets.datalad.org/shub/ZhifangYe/xcpengine_build/latest/2019-04-21-54b86745-ef83ca75/Singularity
collection: ZhifangYe/xcpengine_build
---

# ZhifangYe/xcpengine_build:latest

```bash
$ singularity pull shub://ZhifangYe/xcpengine_build:latest
```

## Singularity Recipe

```singularity
# xcpEngine
# URL: https://github.com/PennBBL/xcpEngine

BootStrap: docker
From: pennbbl/xcpengine:1.0

%labels
Recipe maintainer zhifang.ye.fghm@gmail.com
Build-date 04/21/2019
Vendor Debian:Stretch
Version 1.0

%runscript
    exec /xcpEngine/xcpEngine "$@"

%environment

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

 - Name: [ZhifangYe/xcpengine_build](https://github.com/ZhifangYe/xcpengine_build)
 - License: None

