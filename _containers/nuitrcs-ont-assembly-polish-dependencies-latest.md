---
id: 5838
name: "nuitrcs/ont-assembly-polish-dependencies"
branch: "master"
tag: "latest"
commit: "c348b35db226f5b0b24b217f39f02a9674df9943"
version: "28bbb0b432c1808a5b8327d4e1bcd43d"
build_date: "2021-01-10T23:33:16.530Z"
size_mb: 1838
size: 837001247
sif: "https://datasets.datalad.org/shub/nuitrcs/ont-assembly-polish-dependencies/latest/2021-01-10-c348b35d-28bbb0b4/28bbb0b432c1808a5b8327d4e1bcd43d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/nuitrcs/ont-assembly-polish-dependencies/latest/2021-01-10-c348b35d-28bbb0b4/
recipe: https://datasets.datalad.org/shub/nuitrcs/ont-assembly-polish-dependencies/latest/2021-01-10-c348b35d-28bbb0b4/Singularity
collection: nuitrcs/ont-assembly-polish-dependencies
---

# nuitrcs/ont-assembly-polish-dependencies:latest

```bash
$ singularity pull shub://nuitrcs/ont-assembly-polish-dependencies:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
    apt-get update && apt-get upgrade -y && apt-get install -y \
        sudo git make build-essential mummer last-align python-numpy \
        python-matplotlib time bwa samtools software-properties-common \
        gnuplot zlib1g-dev mc wget libatlas-base-dev python-pip python-pandas curl
    add-apt-repository ppa:webupd8team/java && apt-get update && \
        (echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | sudo debconf-set-selections) && \
        apt-get install -y oracle-java8-installer
    cd /opt
    curl -L -O https://github.com/marbl/canu/releases/download/v1.8/canu-1.8.Linux-amd64.tar.xz && \
        tar -xJf canu-1.8.Linux-amd64.tar.xz && rm canu-1.8.Linux-amd64.tar.xz
    git clone https://github.com/lh3/minimap2 && (cd minimap2 && make) && \
        cp minimap2/minimap2 /usr/local/bin && rm -r minimap2
    git clone https://github.com/lh3/miniasm && (cd miniasm && make) && \
        cp miniasm/miniasm /usr/local/bin/ && rm -r miniasm
    git clone https://github.com/timmassingham/simNGS.git && (cd simNGS/src && make -f Makefile.linux) && \
        cp simNGS/bin/* /usr/local/bin/ && rm -r simNGS

%environment
    PATH=/opt/canu-1.8/Linux-amd64/bin:$PATH
    export PATH

%runscript
    exec /bin/bash -i
```

## Collection

 - Name: [nuitrcs/ont-assembly-polish-dependencies](https://github.com/nuitrcs/ont-assembly-polish-dependencies)
 - License: None

