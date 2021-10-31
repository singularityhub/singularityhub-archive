---
id: 2350
name: "MPIB/singularity-fsl"
branch: "master"
tag: "5.0.11"
commit: "7616243f0bcba0452e968235100b8e52bb37af7f"
version: "37477f2d1c931119be85137b49691d16"
build_date: "2021-01-26T06:33:43.391Z"
size_mb: 9045
size: 4064059423
sif: "https://datasets.datalad.org/shub/MPIB/singularity-fsl/5.0.11/2021-01-26-7616243f-37477f2d/37477f2d1c931119be85137b49691d16.simg"
url: https://datasets.datalad.org/shub/MPIB/singularity-fsl/5.0.11/2021-01-26-7616243f-37477f2d/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-fsl/5.0.11/2021-01-26-7616243f-37477f2d/Singularity
collection: MPIB/singularity-fsl
---

# MPIB/singularity-fsl:5.0.11

```bash
$ singularity pull shub://MPIB/singularity-fsl:5.0.11
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:8

%labels
    AUTHOR krause@mpib-berlin.mpg.de

%post
    apt-get update
    apt-get -y install wget python-minimal libgomp1 ca-certificates \
            libglu1-mesa libgl1-mesa-glx libsm6 libice6 libxt6 \
            libjpeg62-turbo libpng12-0 libxrender1 libxcursor1 \
            libxinerama1 libfreetype6 libxft2 libxrandr2 libmng1 \
            libgtk2.0-0 libpulse0 libasound2 libcaca0 bzip2
    wget https://fsl.fmrib.ox.ac.uk/fsldownloads/fslinstaller.py
    python2 fslinstaller.py -d /usr/local/fsl -V 5.0.11
    echo '/usr/local/fsl/lib' > /etc/ld.so.conf.d/fsl.conf
    ldconfig

%environment
    FSLDIR=/usr/local/fsl
    . ${FSLDIR}/etc/fslconf/fsl.sh
    PATH=${FSLDIR}/bin:${PATH}
    export FSLDIR PATH
```

## Collection

 - Name: [MPIB/singularity-fsl](https://github.com/MPIB/singularity-fsl)
 - License: None

