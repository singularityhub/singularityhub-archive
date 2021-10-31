---
id: 12120
name: "MPIB/singularity-fsl"
branch: "master"
tag: "6.0.1"
commit: "ceb8d1fb612c12617e93716f5e3e3a0d02cf0355"
version: "c5d930313f429fd42a5eb32548657a2b34e9dfa26875e9e602fc0962cf4036e9"
build_date: "2021-01-25T22:58:18.664Z"
size_mb: 4590.48828125
size: 4813475840
sif: "https://datasets.datalad.org/shub/MPIB/singularity-fsl/6.0.1/2021-01-25-ceb8d1fb-c5d93031/c5d930313f429fd42a5eb32548657a2b34e9dfa26875e9e602fc0962cf4036e9.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/MPIB/singularity-fsl/6.0.1/2021-01-25-ceb8d1fb-c5d93031/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-fsl/6.0.1/2021-01-25-ceb8d1fb-c5d93031/Singularity
collection: MPIB/singularity-fsl
---

# MPIB/singularity-fsl:6.0.1

```bash
$ singularity pull shub://MPIB/singularity-fsl:6.0.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:9

%labels
    AUTHOR krause@mpib-berlin.mpg.de

%post
    apt-get update
    apt-get -y install wget python-minimal libgomp1 ca-certificates \
            libglu1-mesa libgl1-mesa-glx libsm6 libice6 libxt6 \
            libjpeg62-turbo libpng16-16 libxrender1 libxcursor1 \
            libxinerama1 libfreetype6 libxft2 libxrandr2 libmng1 \
            libgtk2.0-0 libpulse0 libasound2 libcaca0 libopenblas-base \
            bzip2 dc bc
    wget https://fsl.fmrib.ox.ac.uk/fsldownloads/fslinstaller.py
    python2 fslinstaller.py -d /usr/local/fsl -V 6.0.1
    echo '/usr/local/fsl/lib' > /etc/ld.so.conf.d/fsl.conf
    ldconfig
    apt-get clean && apt-get -y autoremove

%environment
    FSLDIR=/usr/local/fsl
    . ${FSLDIR}/etc/fslconf/fsl.sh
    PATH=${FSLDIR}/bin:${PATH}
    export FSLDIR PATH
```

## Collection

 - Name: [MPIB/singularity-fsl](https://github.com/MPIB/singularity-fsl)
 - License: None

