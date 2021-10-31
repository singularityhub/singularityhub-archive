---
id: 11553
name: "MPIB/singularity-fsl"
branch: "master"
tag: "6.0.2-cuda8"
commit: "7a87bab388149e68ab0bdb6cd8b11dbdcae12102"
version: "b72f3524fff53f08c3cf54ab29ff51efaf7bcd0fbdff3e4fbc3501bec9005f56"
build_date: "2021-03-18T09:26:16.831Z"
size_mb: 6775.03125
size: 7104135168
sif: "https://datasets.datalad.org/shub/MPIB/singularity-fsl/6.0.2-cuda8/2021-03-18-7a87bab3-b72f3524/b72f3524fff53f08c3cf54ab29ff51efaf7bcd0fbdff3e4fbc3501bec9005f56.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/MPIB/singularity-fsl/6.0.2-cuda8/2021-03-18-7a87bab3-b72f3524/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-fsl/6.0.2-cuda8/2021-03-18-7a87bab3-b72f3524/Singularity
collection: MPIB/singularity-fsl
---

# MPIB/singularity-fsl:6.0.2-cuda8

```bash
$ singularity pull shub://MPIB/singularity-fsl:6.0.2-cuda8
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:9

%labels
    AUTHOR krause@mpib-berlin.mpg.de

%post
    apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install \
            wget python-minimal libgomp1 ca-certificates \
            libglu1-mesa libgl1-mesa-glx libsm6 libice6 libxt6 \
            libjpeg62-turbo libpng16-16 libxrender1 libxcursor1 \
            libxinerama1 libfreetype6 libxft2 libxrandr2 libmng1 \
            libgtk2.0-0 libpulse0 libasound2 libcaca0 libopenblas-base \
            unzip bzip2 dc bc
    wget https://fsl.fmrib.ox.ac.uk/fsldownloads/fslinstaller.py
    python2 fslinstaller.py -d /usr/local/fsl -V 6.0.2
    #cat /tmp/fslpython*/fslpython_miniconda_installer.log
    echo '/usr/local/fsl/lib' > /etc/ld.so.conf.d/fsl.conf
    ldconfig
    wget http://users.fmrib.ox.ac.uk/~moisesf/Probtrackx_GPU/FSL_6/CUDA_8.0/probtrackx2_gpu.zip
    unzip -o probtrackx2_gpu.zip -d /usr/local/fsl/bin/
    wget http://users.fmrib.ox.ac.uk/~moisesf/Bedpostx_GPU/FSL_6/CUDA_8.0/bedpostx_gpu.zip
    unzip -o bedpostx_gpu.zip -d /usr/local/fsl/bin/
    echo 'deb http://deb.debian.org/debian stretch main contrib non-free'          > /etc/apt/sources.list
    echo 'deb http://deb.debian.org/debian stretch-updates main contrib non-free' >> /etc/apt/sources.list
    echo 'deb http://security.debian.org stretch/updates main contrib non-free'   >> /etc/apt/sources.list
    apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install \
        nvidia-cuda-toolkit libcupti-dev nvidia-driver nvidia-smi
    apt-get clean && apt-get autoremove -y
    rm -f fslinstaller.py bedpostx_gpu.zip probtrackx_gpu.zip

%environment
    FSLDIR=/usr/local/fsl
    . ${FSLDIR}/etc/fslconf/fsl.sh
    PATH=${FSLDIR}/bin:${PATH}
    export FSLDIR PATH
```

## Collection

 - Name: [MPIB/singularity-fsl](https://github.com/MPIB/singularity-fsl)
 - License: None

