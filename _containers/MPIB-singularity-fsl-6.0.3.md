---
id: 12122
name: "MPIB/singularity-fsl"
branch: "master"
tag: "6.0.3"
commit: "aaadca891b40c34618000c2eb553b0d29a72f5d6"
version: "9ec2a141ea96aacd64e7f8074535006ca907a6901687a69c4649fe0eecb9b1a1"
build_date: "2021-03-30T03:54:55.581Z"
size_mb: 6550.3515625
size: 6868541440
sif: "https://datasets.datalad.org/shub/MPIB/singularity-fsl/6.0.3/2021-03-30-aaadca89-9ec2a141/9ec2a141ea96aacd64e7f8074535006ca907a6901687a69c4649fe0eecb9b1a1.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/MPIB/singularity-fsl/6.0.3/2021-03-30-aaadca89-9ec2a141/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-fsl/6.0.3/2021-03-30-aaadca89-9ec2a141/Singularity
collection: MPIB/singularity-fsl
---

# MPIB/singularity-fsl:6.0.3

```bash
$ singularity pull shub://MPIB/singularity-fsl:6.0.3
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
    python2 fslinstaller.py -d /usr/local/fsl -V 6.0.3
    echo '/usr/local/fsl/lib' > /etc/ld.so.conf.d/fsl.conf
    ldconfig
    apt-get clean && apt-get -y autoremove
    rm -f fslinstaller.py

%environment
    FSLDIR=/usr/local/fsl
    . ${FSLDIR}/etc/fslconf/fsl.sh
    PATH=${FSLDIR}/bin:${PATH}
    export FSLDIR PATH
```

## Collection

 - Name: [MPIB/singularity-fsl](https://github.com/MPIB/singularity-fsl)
 - License: None

