---
id: 7709
name: "rses-singularity/fsl-debian-stretch-singularity"
branch: "master"
tag: "latest"
commit: "b26a4aa0e50d89abe606954b765022b4a030d609"
version: "4a830abfbba3d55e8b5b594fd9687415"
build_date: "2020-07-01T13:53:24.220Z"
size_mb: 2282
size: 1762279455
sif: "https://datasets.datalad.org/shub/rses-singularity/fsl-debian-stretch-singularity/latest/2020-07-01-b26a4aa0-4a830abf/4a830abfbba3d55e8b5b594fd9687415.simg"
url: https://datasets.datalad.org/shub/rses-singularity/fsl-debian-stretch-singularity/latest/2020-07-01-b26a4aa0-4a830abf/
recipe: https://datasets.datalad.org/shub/rses-singularity/fsl-debian-stretch-singularity/latest/2020-07-01-b26a4aa0-4a830abf/Singularity
collection: rses-singularity/fsl-debian-stretch-singularity
---

# rses-singularity/fsl-debian-stretch-singularity:latest

```bash
$ singularity pull shub://rses-singularity/fsl-debian-stretch-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:debian:stretch
 
%labels
MAINTAINER willfurnass

#%setup
#    mkdir ${SINGULARITY_ROOTFS}/somedir
#    cp somefile ${SINGULARITY_ROOTFS}/

%post
    DEBIAN_FRONTEND=noninteractive apt-get update 
    DEBIAN_FRONTEND=noninteractive apt-get install -y curl gnupg2
    curl -sSL http://neuro.debian.net/lists/stretch.de-md.full > /etc/apt/sources.list.d/neurodebian.sources.list
    DEBIAN_FRONTEND=noninteractive apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9
    DEBIAN_FRONTEND=noninteractive apt-get update 
    DEBIAN_FRONTEND=noninteractive apt-get install -y fsl-complete fsl-feeds
    rm -r /var/lib/apt/lists/*
    ln -s /usr/share/fsl/5.0/etc/fslconf/fsl.sh /usr/share/fsl/5.0/etc/fslconf/fsl.csh /etc/profile.d

#%environment
#    export SOMEVAR=some_value
 
#%runscript
#    someprogram arg1 arg2
```

## Collection

 - Name: [rses-singularity/fsl-debian-stretch-singularity](https://github.com/rses-singularity/fsl-debian-stretch-singularity)
 - License: [Other](None)

