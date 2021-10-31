---
id: 2448
name: "ZhifangYe/mindboggle_build"
branch: "master"
tag: "latest"
commit: "1fee4614b8c3c05d47db8df9cc812d52e6c88d6f"
version: "14b15141384be7d98f10adcabe5381a5"
build_date: "2018-10-03T06:31:02.437Z"
size_mb: 5212
size: 1723727903
sif: "https://datasets.datalad.org/shub/ZhifangYe/mindboggle_build/latest/2018-10-03-1fee4614-14b15141/14b15141384be7d98f10adcabe5381a5.simg"
url: https://datasets.datalad.org/shub/ZhifangYe/mindboggle_build/latest/2018-10-03-1fee4614-14b15141/
recipe: https://datasets.datalad.org/shub/ZhifangYe/mindboggle_build/latest/2018-10-03-1fee4614-14b15141/Singularity
collection: ZhifangYe/mindboggle_build
---

# ZhifangYe/mindboggle_build:latest

```bash
$ singularity pull shub://ZhifangYe/mindboggle_build:latest
```

## Singularity Recipe

```singularity
# mindboggle

BootStrap: docker
From: nipy/mindboggle:latest

%labels
Author zhifang.ye.fghm@gmail.com
Build-date 10/02/2018
Vendor Ubuntu:Xenial
Version 1.3.0

%runscript
    #!/bin/bash
    source activate mb
    exec mindboggle "$@"

%environment
    export FSL_DIR=/opt/fsl \
           OS=Linux \
           FS_OVERRIDE=0 \
           FIX_VERTEX_AREA= \
           FSF_OUTPUT_FORMAT=nii.gz
    export SUBJECTS_DIR=${FREESURFER_HOME}/subjects \
           FUNCTIONALS_DIR=${FREESURFER_HOME}/sessions \
           MNI_DIR=${FREESURFER_HOME}/mni \
           LOCAL_DIR=${FREESURFER_HOME}/local \
           FSFAST_HOME=${FREESURFER_HOME}/fsfast \
           MINC_BIN_DIR=${FREESURFER_HOME}/mni/bin \
           MINC_LIB_DIR=${FREESURFER_HOME}/mni/lib \
           MNI_DATAPATH=${FREESURFER_HOME}/mni/data \
           FMRI_ANALYSIS_DIR=${FREESURFER_HOME}/fsfast
    export PERL5LIB=${MINC_LIB_DIR}/perl5/5.8.5 \
           MNI_PERL5LIB=${MINC_LIB_DIR}/perl5/5.8.5
    export PATH=${FREESURFER_HOME}/bin:${FSFAST_HOME}/bin:${FREESURFER_HOME}/tktools:${MINC_BIN_DIR}:${PATH}

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

 - Name: [ZhifangYe/mindboggle_build](https://github.com/ZhifangYe/mindboggle_build)
 - License: None

