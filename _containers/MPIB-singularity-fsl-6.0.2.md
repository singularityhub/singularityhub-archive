---
id: 12088
name: "MPIB/singularity-fsl"
branch: "master"
tag: "6.0.2"
commit: "066ab246088d07e6f19969f588e599c4b45a9a00"
version: "4697460737806a77cc5e211569e0e5a1dfd14d7d076d06e8fbccba713aecc662"
build_date: "2020-09-21T12:23:20.153Z"
size_mb: 6503.42578125
size: 6819336192
sif: "https://datasets.datalad.org/shub/MPIB/singularity-fsl/6.0.2/2020-09-21-066ab246-46974607/4697460737806a77cc5e211569e0e5a1dfd14d7d076d06e8fbccba713aecc662.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/MPIB/singularity-fsl/6.0.2/2020-09-21-066ab246-46974607/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-fsl/6.0.2/2020-09-21-066ab246-46974607/Singularity
collection: MPIB/singularity-fsl
---

# MPIB/singularity-fsl:6.0.2

```bash
$ singularity pull shub://MPIB/singularity-fsl:6.0.2
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
    echo 'deb http://deb.debian.org/debian stretch-backports main contrib non-free' >> /etc/apt/sources.list
    apt-get update -y
    DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install \
            wget python-minimal libgomp1 ca-certificates \
            libglu1-mesa libgl1-mesa-glx libsm6 libice6 libxt6 \
            libjpeg62-turbo libpng16-16 libxrender1 libxcursor1 \
            libxinerama1 libfreetype6 libxft2 libxrandr2 libmng1 \
            libgtk2.0-0 libpulse0 libasound2 libcaca0 libopenblas-base \
            bzip2 dc bc
    # Cuda 9.1 from stretch-backports
    DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install \
            nvidia-cuda-toolkit libcupti-dev nvidia-smi -t stretch-backports
    wget https://fsl.fmrib.ox.ac.uk/fsldownloads/fslinstaller.py
    python2 fslinstaller.py -d /usr/local/fsl -V 6.0.2
    echo '/usr/local/fsl/lib' > /etc/ld.so.conf.d/fsl.conf
    ldconfig
    apt-get clean && apt-get -y autoremove
    rm -f fslinstaller.py
    ln -sf /usr/local/fsl/bin{eddy_cuda9.1,eddy_cuda}

%environment
    FSLDIR=/usr/local/fsl
    . ${FSLDIR}/etc/fslconf/fsl.sh
    PATH=${FSLDIR}/bin:${PATH}
    export FSLDIR PATH
```

## Collection

 - Name: [MPIB/singularity-fsl](https://github.com/MPIB/singularity-fsl)
 - License: None

