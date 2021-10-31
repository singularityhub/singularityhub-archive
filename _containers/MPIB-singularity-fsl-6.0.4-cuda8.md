---
id: 15746
name: "MPIB/singularity-fsl"
branch: "master"
tag: "6.0.4-cuda8"
commit: "ccb7cd8f3dbbea1edbcfb55934fca752585f8856"
version: "49e7a01f1a7d7366d85e545dbf8be07697138688dab7a9381d035fd7c29cdd55"
build_date: "2021-03-18T14:02:37.518Z"
size_mb: 7843.390625
size: 8224391168
sif: "https://datasets.datalad.org/shub/MPIB/singularity-fsl/6.0.4-cuda8/2021-03-18-ccb7cd8f-49e7a01f/49e7a01f1a7d7366d85e545dbf8be07697138688dab7a9381d035fd7c29cdd55.sif"
url: https://datasets.datalad.org/shub/MPIB/singularity-fsl/6.0.4-cuda8/2021-03-18-ccb7cd8f-49e7a01f/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-fsl/6.0.4-cuda8/2021-03-18-ccb7cd8f-49e7a01f/Singularity
collection: MPIB/singularity-fsl
---

# MPIB/singularity-fsl:6.0.4-cuda8

```bash
$ singularity pull shub://MPIB/singularity-fsl:6.0.4-cuda8
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:9-slim

%labels
    AUTHOR krause@mpib-berlin.mpg.de

%post
    mkdir -p /usr/share/man/man1 # https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=863199
    echo 'deb http://deb.debian.org/debian stretch main contrib non-free'            > /etc/apt/sources.list
    echo 'deb http://deb.debian.org/debian stretch-updates main contrib non-free'   >> /etc/apt/sources.list
    echo 'deb http://security.debian.org stretch/updates main contrib non-free'     >> /etc/apt/sources.list
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install \
            wget python-minimal libgomp1 ca-certificates \
            libglu1-mesa libgl1-mesa-glx libsm6 libice6 libxt6 \
            libjpeg62-turbo libpng16-16 libxrender1 libxcursor1 \
            libxinerama1 libfreetype6 libxft2 libxrandr2 libmng1 \
            libgtk2.0-0 libpulse0 libasound2 libcaca0 libopenblas-base \
            unzip bzip2 dc bc
    DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install \
        nvidia-cuda-toolkit libcupti-dev nvidia-driver nvidia-smi
    wget https://fsl.fmrib.ox.ac.uk/fsldownloads/fslinstaller.py
    python2 fslinstaller.py -d /usr/local/fsl -V 6.0.4
    echo '/usr/local/fsl/lib' > /etc/ld.so.conf.d/fsl.conf
    ldconfig
    wget http://users.fmrib.ox.ac.uk/~moisesf/Probtrackx_GPU/FSL_6/CUDA_8.0/probtrackx2_gpu.zip
    unzip -o probtrackx2_gpu.zip -d /usr/local/fsl/bin/
    wget http://users.fmrib.ox.ac.uk/~moisesf/Bedpostx_GPU/FSL_6/CUDA_8.0/bedpostx_gpu.zip
    unzip -o bedpostx_gpu.zip -d /usr/local/fsl/bin/
    apt-get clean && apt-get autoremove -y
    rm -f fslinstaller.py bedpostx_gpu.zip probtrackx_gpu.zip
    ln -sf /usr/local/fsl/bin/eddy_cuda8.0 /usr/local/fsl/bin/eddy_cuda

%environment
    FSLDIR=/usr/local/fsl
    . ${FSLDIR}/etc/fslconf/fsl.sh
    PATH=${FSLDIR}/bin:${PATH}
    export FSLDIR PATH
```

## Collection

 - Name: [MPIB/singularity-fsl](https://github.com/MPIB/singularity-fsl)
 - License: None

