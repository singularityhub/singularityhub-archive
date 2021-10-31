---
id: 12106
name: "MPIB/singularity-fsl"
branch: "master"
tag: "5-cuda8"
commit: "7a87bab388149e68ab0bdb6cd8b11dbdcae12102"
version: "e12be7d00692a97ef62c545da16b6ca423827a8eecdfe897b17399b031dc4511"
build_date: "2020-09-21T12:23:58.839Z"
size_mb: 5096.68359375
size: 5344260096
sif: "https://datasets.datalad.org/shub/MPIB/singularity-fsl/5-cuda8/2020-09-21-7a87bab3-e12be7d0/e12be7d00692a97ef62c545da16b6ca423827a8eecdfe897b17399b031dc4511.sif"
url: https://datasets.datalad.org/shub/MPIB/singularity-fsl/5-cuda8/2020-09-21-7a87bab3-e12be7d0/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-fsl/5-cuda8/2020-09-21-7a87bab3-e12be7d0/Singularity
collection: MPIB/singularity-fsl
---

# MPIB/singularity-fsl:5-cuda8

```bash
$ singularity pull shub://MPIB/singularity-fsl:5-cuda8
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: gw000/debian-cuda:8.0_7.0

%labels
    AUTHOR krause@mpib-berlin.mpg.de
    CUDA 8.0

%post
    apt-get update
    apt-get -y install wget python-minimal libgomp1 nvidia-smi ca-certificates \
            libglu1-mesa libgl1-mesa-glx libsm6 libice6 libxt6 \
            libjpeg62-turbo libpng16-16 libxrender1 libxcursor1 \
            libxinerama1 libfreetype6 libxft2 libxrandr2 libmng1 \
            libgtk2.0-0 libpulse0 libasound2 libcaca0 bzip2 
    wget https://fsl.fmrib.ox.ac.uk/fsldownloads/fslinstaller.py
    python2 fslinstaller.py -d /usr/local/fsl -V 5.0.11
    wget -O- https://fsl.fmrib.ox.ac.uk/fsldownloads/patches/eddy-patch-fsl-5.0.11/centos6/eddy_cuda8.0  > /usr/local/fsl/bin/eddy_cuda
    wget -O- https://fsl.fmrib.ox.ac.uk/fsldownloads/patches/eddy-patch-fsl-5.0.11/centos6/eddy_openmp > /usr/local/fsl/bin/eddy_openmp

%environment
    FSLDIR=/usr/local/fsl
    . ${FSLDIR}/etc/fslconf/fsl.sh
    PATH=${FSLDIR}/bin:${PATH}
    export FSLDIR PATH
```

## Collection

 - Name: [MPIB/singularity-fsl](https://github.com/MPIB/singularity-fsl)
 - License: None

