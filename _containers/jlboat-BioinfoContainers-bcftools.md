---
id: 8793
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "bcftools"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "b3d4788a767083104db5b1251bf305e9"
build_date: "2020-09-16T08:06:18.589Z"
size_mb: 427
size: 146665503
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/bcftools/2020-09-16-5f15386e-b3d4788a/b3d4788a767083104db5b1251bf305e9.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/bcftools/2020-09-16-5f15386e-b3d4788a/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/bcftools/2020-09-16-5f15386e-b3d4788a/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:bcftools

```bash
$ singularity pull shub://jlboat/BioinfoContainers:bcftools
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:latest

%labels
    Topic Bioinformatics
    Input BCF
    bcftools 1.9

%post
    apt-get update --fix-missing && apt-get install -y wget make zlib1g-dev gcc \
        pkg-config autoconf libncurses5-dev libbz2-dev liblzma-dev libcurl4-gnutls-dev libssl-dev
    cd /opt/
    wget --quiet https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2
    tar xvfj bcftools-1.9.tar.bz2
    rm bcftools-1.9.tar.bz2
    cd bcftools-1.9
    ./configure
    make
    make install
    chmod -R 777 /opt/*

%runscript
    exec bcftools "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

