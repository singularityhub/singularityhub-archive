---
id: 2349
name: "MPIB/singularity-fsl"
branch: "master"
tag: "5.0.10"
commit: "7616243f0bcba0452e968235100b8e52bb37af7f"
version: "fc050b2ff8484bfeecf09ec4a631dbcb"
build_date: "2019-05-27T12:13:23.724Z"
size_mb: 8575
size: 3806195743
sif: "https://datasets.datalad.org/shub/MPIB/singularity-fsl/5.0.10/2019-05-27-7616243f-fc050b2f/fc050b2ff8484bfeecf09ec4a631dbcb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/MPIB/singularity-fsl/5.0.10/2019-05-27-7616243f-fc050b2f/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-fsl/5.0.10/2019-05-27-7616243f-fc050b2f/Singularity
collection: MPIB/singularity-fsl
---

# MPIB/singularity-fsl:5.0.10

```bash
$ singularity pull shub://MPIB/singularity-fsl:5.0.10
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
    python2 fslinstaller.py -d /usr/local/fsl -V 5.0.10
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

