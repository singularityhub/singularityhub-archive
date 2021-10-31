---
id: 3108
name: "ZhifangYe/fmriprep_build"
branch: "master"
tag: "latest"
commit: "f5759422b5a2b452f74bed4546ecf5af331de2d8"
version: "c01174f7a2a77df5c47eff22ede72db8"
build_date: "2019-05-16T02:35:10.001Z"
size_mb: 12142
size: 4780552223
sif: "https://datasets.datalad.org/shub/ZhifangYe/fmriprep_build/latest/2019-05-16-f5759422-c01174f7/c01174f7a2a77df5c47eff22ede72db8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ZhifangYe/fmriprep_build/latest/2019-05-16-f5759422-c01174f7/
recipe: https://datasets.datalad.org/shub/ZhifangYe/fmriprep_build/latest/2019-05-16-f5759422-c01174f7/Singularity
collection: ZhifangYe/fmriprep_build
---

# ZhifangYe/fmriprep_build:latest

```bash
$ singularity pull shub://ZhifangYe/fmriprep_build:latest
```

## Singularity Recipe

```singularity
# fMRIPrep from poldracklab
# URL: https://github.com/poldracklab/fmriprep

BootStrap: docker
From: poldracklab/fmriprep:latest

%labels
Author zhifang.ye.fghm@gmail.com
Build-date 05/16/2019
Vendor Ubuntu:Xenial
Version 1.4.0

%runscript
    exec /usr/local/miniconda/bin/fmriprep "$@"

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

 - Name: [ZhifangYe/fmriprep_build](https://github.com/ZhifangYe/fmriprep_build)
 - License: None

