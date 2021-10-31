---
id: 4180
name: "ZhifangYe/mriqc_build"
branch: "master"
tag: "latest"
commit: "5dab90e85f457027f2acba089d8476dec52227a2"
version: "80d63381280978d736b9b1a8ab087275"
build_date: "2019-07-29T08:17:07.350Z"
size_mb: 7589
size: 2928783391
sif: "https://datasets.datalad.org/shub/ZhifangYe/mriqc_build/latest/2019-07-29-5dab90e8-80d63381/80d63381280978d736b9b1a8ab087275.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ZhifangYe/mriqc_build/latest/2019-07-29-5dab90e8-80d63381/
recipe: https://datasets.datalad.org/shub/ZhifangYe/mriqc_build/latest/2019-07-29-5dab90e8-80d63381/Singularity
collection: ZhifangYe/mriqc_build
---

# ZhifangYe/mriqc_build:latest

```bash
$ singularity pull shub://ZhifangYe/mriqc_build:latest
```

## Singularity Recipe

```singularity
# MRIQC from poldracklab
# URL: https://github.com/poldracklab/mriqc

BootStrap: docker
From: poldracklab/mriqc:0.15.0

%runscript
    exec /usr/local/miniconda/bin/mriqc "$@"

%environment

%labels
    Recipe_Maintainer zhifang.ye.fghm@gmail.com
    Build_Date 04/06/2019
    Vendor Ubuntu
    Version 0.15.0

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

 - Name: [ZhifangYe/mriqc_build](https://github.com/ZhifangYe/mriqc_build)
 - License: None

