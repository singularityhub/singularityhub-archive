---
id: 7837
name: "ZhifangYe/dpabi_build"
branch: "master"
tag: "latest"
commit: "d529e84efd7d8860ea2bd06388e5035d2980f2b6"
version: "3c65f07c7339092e9623c8c51f4d9157"
build_date: "2019-03-19T15:52:04.792Z"
size_mb: 17642
size: 7304433695
sif: "https://datasets.datalad.org/shub/ZhifangYe/dpabi_build/latest/2019-03-19-d529e84e-3c65f07c/3c65f07c7339092e9623c8c51f4d9157.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ZhifangYe/dpabi_build/latest/2019-03-19-d529e84e-3c65f07c/
recipe: https://datasets.datalad.org/shub/ZhifangYe/dpabi_build/latest/2019-03-19-d529e84e-3c65f07c/Singularity
collection: ZhifangYe/dpabi_build
---

# ZhifangYe/dpabi_build:latest

```bash
$ singularity pull shub://ZhifangYe/dpabi_build:latest
```

## Singularity Recipe

```singularity
# DPABI: a toolbox for Data Processing & Analysis of Brain Imaging
# URL: http://rfmri.org/DPABI

BootStrap: docker
From: cgyan/dpabi:4.0

%labels
MAINTAINER Chao-Gan Yan <ycg.yan@gmail.com>
SpecificationAuthor zhifang.ye.fghm@gmail.com
BuildDate 03/19/2019
Vendor Ubuntu:Xenial
Version 4.0

%runscript
    exec /opt/DPABI/DPABI_StandAlone/run_DPABI_StandAlone.sh ${MCRPath} "$@"

%environment
    export FS_LICENSE=/opt/freesurfer/license.txt

%post
    #------------------------------------------------------------------------------
    # Change timezone to Shanghai
    #------------------------------------------------------------------------------
    ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
    dpkg-reconfigure --frontend noninteractive tzdata
    #------------------------------------------------------------------------------
    # Add license
    #------------------------------------------------------------------------------
    echo "cHJpbnRmICJ6aGlmYW5nLnllLmZnaG1AZ21haWwuY29tXG4zMDgyN1xuICpDQWp0eWJDWTQwck1cbiBGUzl2ZU14OGdudXFRXG4iID4gL29wdC9mcmVlc3VyZmVyL2xpY2Vuc2UudHh0" | base64 -d | bash
    #------------------------------------------------------------------------------
    # Create local binding point for our HPC
    #------------------------------------------------------------------------------
    mkdir /seastor
    mkdir /brain
    mkdir /lustre
```

## Collection

 - Name: [ZhifangYe/dpabi_build](https://github.com/ZhifangYe/dpabi_build)
 - License: None

