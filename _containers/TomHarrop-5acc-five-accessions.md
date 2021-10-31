---
id: 10376
name: "TomHarrop/5acc"
branch: "master"
tag: "five-accessions"
commit: "d315e37518a64fb304bf4375f0f1418664452e89"
version: "43c579c98f1411004ce398c0123a4854dfaa0f5afd2fcc8cee69a3ad61b9eeb0"
build_date: "2019-07-29T03:37:13.925Z"
size_mb: 885.91796875
size: 928952320
sif: "https://datasets.datalad.org/shub/TomHarrop/5acc/five-accessions/2019-07-29-d315e375-43c579c9/43c579c98f1411004ce398c0123a4854dfaa0f5afd2fcc8cee69a3ad61b9eeb0.sif"
url: https://datasets.datalad.org/shub/TomHarrop/5acc/five-accessions/2019-07-29-d315e375-43c579c9/
recipe: https://datasets.datalad.org/shub/TomHarrop/5acc/five-accessions/2019-07-29-d315e375-43c579c9/Singularity
collection: TomHarrop/5acc
---

# TomHarrop/5acc:five-accessions

```bash
$ singularity pull shub://TomHarrop/5acc:five-accessions
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%runscript


%post

    export DEBIAN_FRONTEND=noninteractive

    # install apt packages
    apt-get update \
        && apt-get upgrade -y \
        && apt-get install -y \
        bcftools \
        bedtools \
        build-essential \
        cufflinks \
        default-jdk \
        git \
        language-pack-en \
        libbz2-dev \
        libcurl4-openssl-dev \
        liblzma-dev \
        libssl-dev \
        libxml2-dev \
        python3-pip=9.0.1-2.3~ubuntu1.18.04.1 \
        python3=3.6.7-1~18.04 \
        rna-star \
        samtools \
        software-properties-common \
        wget

    # install python3 packages
    pip3 install \
        cutadapt \
        HTSeq \
        psutil \
        snakemake

    # install R & packages
    add-apt-repository ppa:marutter/c2d4u
    add-apt-repository ppa:marutter/rrutter
    apt-get update
    apt-get install -y \
        r-base-core=3.4.4-1ubuntu1 \
        r-base-dev=3.4.4-1ubuntu1


    Rscript -e "source('https://bioconductor.org/biocLite.R') ; \
        biocLite(c('RCurl'), type='source', ask=FALSE)"
    Rscript -e "source('https://bioconductor.org/biocLite.R') ; \
        biocLite(c( \
            'cowplot', \
            'data.table', \
            'devtools', \
            'DESeq2', \
            'fgsea', \
            'GenomicRanges', \
            'ggtree', \
            'Mfuzz', \
            'png', \
            'rtracklayer', \
            'tidyverse', \
            'valr'), \
            type='source', ask=FALSE)"
    Rscript -e "devtools::install_github('TomHarrop/oryzr', ref = 'e9d099b')"

    # install wgsim
    git clone https://github.com/lh3/wgsim.git
    cd wgsim
    gcc -g -O2 -Wall -o wgsim wgsim.c -lz -lm
    cp wgsim /usr/local/bin
    cd ..
    rm -rf wgsim

    # install bbmap
    wget "https://sourceforge.net/projects/bbmap/files/BBMap_38.00.tar.gz"
    tar -zxf BBMap_38.00.tar.gz
    mv bbmap/* /usr/local/bin/
    rm -rf bbmap
```

## Collection

 - Name: [TomHarrop/5acc](https://github.com/TomHarrop/5acc)
 - License: None

