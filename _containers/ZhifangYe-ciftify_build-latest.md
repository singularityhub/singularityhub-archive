---
id: 5635
name: "ZhifangYe/ciftify_build"
branch: "master"
tag: "latest"
commit: "3109fdbc0c2870167846cd72b28929ea51d1540d"
version: "021395ed36c0d7b40e548ab398205fd9"
build_date: "2019-03-07T14:19:12.966Z"
size_mb: 12982
size: 5535989791
sif: "https://datasets.datalad.org/shub/ZhifangYe/ciftify_build/latest/2019-03-07-3109fdbc-021395ed/021395ed36c0d7b40e548ab398205fd9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ZhifangYe/ciftify_build/latest/2019-03-07-3109fdbc-021395ed/
recipe: https://datasets.datalad.org/shub/ZhifangYe/ciftify_build/latest/2019-03-07-3109fdbc-021395ed/Singularity
collection: ZhifangYe/ciftify_build
---

# ZhifangYe/ciftify_build:latest

```bash
$ singularity pull shub://ZhifangYe/ciftify_build:latest
```

## Singularity Recipe

```singularity
# Ciftify

BootStrap: docker
From: tigrlab/fmriprep_ciftify:1.3.0.post2-2.3.0

%labels
Author zhifang.ye.fghm@gmail.com
Build-date 03/07/2019
Vendor Ubuntu:Xenial
Version 1.3.0.post2-2.3.0

%runscript
    exec /home/code/ciftify/ciftify/bidsapp/run.py "$@"

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

 - Name: [ZhifangYe/ciftify_build](https://github.com/ZhifangYe/ciftify_build)
 - License: None

