---
id: 2378
name: "neurodebian/dcm2niix"
branch: "enh-singularity"
tag: "debian-unstable-i386"
commit: "8d2e296bceaa4fa8e7b18fe5e90d0f3e330da7f0"
version: "d09a28ec39c4fb936f854f56bea4d1c9"
build_date: "2018-04-03T16:39:16.654Z"
size_mb: 778
size: 232427551
sif: "https://datasets.datalad.org/shub/neurodebian/dcm2niix/debian-unstable-i386/2018-04-03-8d2e296b-d09a28ec/d09a28ec39c4fb936f854f56bea4d1c9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/neurodebian/dcm2niix/debian-unstable-i386/2018-04-03-8d2e296b-d09a28ec/
recipe: https://datasets.datalad.org/shub/neurodebian/dcm2niix/debian-unstable-i386/2018-04-03-8d2e296b-d09a28ec/Singularity
collection: neurodebian/dcm2niix
---

# neurodebian/dcm2niix:debian-unstable-i386

```bash
$ singularity pull shub://neurodebian/dcm2niix:debian-unstable-i386
```

## Singularity Recipe

```singularity
BootStrap: docker
From: i386/debian:unstable

# so if image is executed we just enter the environment
%runscript
    echo "Welcome to the Debian unstable dcm2niix devel env. (Architecture: i386)"
    echo "Just cd to your dcm2niix sources or"
    echo " git clone https://github.com/neurolabusc/dcm2niix/"
    /bin/bash


%post
    echo "Configuring the environment"
    sed -e  's,^deb ,deb-src ,g' /etc/apt/sources.list > /etc/apt/sources.list.d/sources.list
    apt-get update
    apt-get -y install eatmydata
    # just useful little tools
    eatmydata apt-get -y install vim wget strace time ncdu gnupg curl procps netcat
    eatmydata apt-get -y build-dep dcm2niix
    # some external depends might have not been needed then
    eatmydata apt-get -y install markdown git
    chmod a+rX -R /etc/apt/sources.list.d
    rm -rf /var/lib/apt/lists/*
    apt-get clean
```

## Collection

 - Name: [neurodebian/dcm2niix](https://github.com/neurodebian/dcm2niix)
 - License: [Other](None)

