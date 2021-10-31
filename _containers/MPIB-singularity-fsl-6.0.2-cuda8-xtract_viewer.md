---
id: 11370
name: "MPIB/singularity-fsl"
branch: "master"
tag: "6.0.2-cuda8-xtract_viewer"
commit: "066ab246088d07e6f19969f588e599c4b45a9a00"
version: "974c4969e764433005e36ce421976a42b80911a46e2e91859796db9d88ec987d"
build_date: "2020-12-08T11:53:49.878Z"
size_mb: 6654.79296875
size: 6978056192
sif: "https://datasets.datalad.org/shub/MPIB/singularity-fsl/6.0.2-cuda8-xtract_viewer/2020-12-08-066ab246-974c4969/974c4969e764433005e36ce421976a42b80911a46e2e91859796db9d88ec987d.sif"
url: https://datasets.datalad.org/shub/MPIB/singularity-fsl/6.0.2-cuda8-xtract_viewer/2020-12-08-066ab246-974c4969/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-fsl/6.0.2-cuda8-xtract_viewer/2020-12-08-066ab246-974c4969/Singularity
collection: MPIB/singularity-fsl
---

# MPIB/singularity-fsl:6.0.2-cuda8-xtract_viewer

```bash
$ singularity pull shub://MPIB/singularity-fsl:6.0.2-cuda8-xtract_viewer
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: gw000/debian-cuda:8.0_7.0

%labels
    AUTHOR krause@mpib-berlin.mpg.de

# missing in 6.0.2 release, deprecated for 6.0.3
%files
    data/xtract_viewer /root/xtract_viewer

%post
    apt-get update
    apt-get -y install wget python-minimal libgomp1 ca-certificates \
            libglu1-mesa libgl1-mesa-glx libsm6 libice6 libxt6 \
            libjpeg62-turbo libpng16-16 libxrender1 libxcursor1 \
            libxinerama1 libfreetype6 libxft2 libxrandr2 libmng1 \
            libgtk2.0-0 libpulse0 libasound2 libcaca0 libopenblas-base \
            bzip2 dc bc
    wget https://fsl.fmrib.ox.ac.uk/fsldownloads/fslinstaller.py
    python2 fslinstaller.py -d /usr/local/fsl -V 6.0.2
    echo '/usr/local/fsl/lib' > /etc/ld.so.conf.d/fsl.conf
    ldconfig
    apt-get clean && apt-get -y autoremove
    mv /root/xtract_viewer /usr/local/fsl/bin/

%environment
    FSLDIR=/usr/local/fsl
    . ${FSLDIR}/etc/fslconf/fsl.sh
    PATH=${FSLDIR}/bin:${PATH}
    export FSLDIR PATH
```

## Collection

 - Name: [MPIB/singularity-fsl](https://github.com/MPIB/singularity-fsl)
 - License: None

