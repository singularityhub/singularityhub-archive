---
id: 8790
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "samtools"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "c84f59ff4a9044323908da588663c150"
build_date: "2019-05-08T15:11:14.483Z"
size_mb: 441
size: 153260063
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/samtools/2019-05-08-5f15386e-c84f59ff/c84f59ff4a9044323908da588663c150.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jlboat/BioinfoContainers/samtools/2019-05-08-5f15386e-c84f59ff/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/samtools/2019-05-08-5f15386e-c84f59ff/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:samtools

```bash
$ singularity pull shub://jlboat/BioinfoContainers:samtools
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:latest

%post
    apt-get update --fix-missing && apt-get install -y wget make zlib1g-dev gcc \
        pkg-config autoconf libncurses5-dev libbz2-dev liblzma-dev libcurl4-gnutls-dev libssl-dev
    cd /opt/
    wget --quiet https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
    tar xvfj samtools-1.9.tar.bz2
    rm samtools-1.9.tar.bz2
    cd samtools-1.9
    ./configure
    make
    make install
    chmod -R 777 /opt/*

%runscript
    exec samtools "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

