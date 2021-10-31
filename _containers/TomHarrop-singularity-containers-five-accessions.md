---
id: 7888
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "five-accessions"
commit: "2de5f7df11d99408f4b6c1ad4c40e7beb0cc5ece"
version: "ec77092b3e6e20d70a44cde27c006de9"
build_date: "2020-01-17T03:41:35.830Z"
size_mb: 2027
size: 823021599
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/five-accessions/2020-01-17-2de5f7df-ec77092b/ec77092b3e6e20d70a44cde27c006de9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/five-accessions/2020-01-17-2de5f7df-ec77092b/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/five-accessions/2020-01-17-2de5f7df-ec77092b/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:five-accessions

```bash
$ singularity pull shub://TomHarrop/singularity-containers:five-accessions
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
        libcurl4-openssl-dev \
        libssl-dev \
        libxml2-dev \
        python3 \
        python3-pip \
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
        r-base-core r-base-dev

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

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

