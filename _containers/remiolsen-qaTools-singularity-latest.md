---
id: 616
name: "remiolsen/qaTools-singularity"
branch: "master"
tag: "latest"
commit: "ce54e8d2eb4beb9bad19ae9be976ef2975b753d6"
version: "dcb1acb519d19dd9c0289feb8a6e7a0f"
build_date: "2017-10-30T16:11:34.728Z"
size_mb: 647
size: 164974623
sif: "https://datasets.datalad.org/shub/remiolsen/qaTools-singularity/latest/2017-10-30-ce54e8d2-dcb1acb5/dcb1acb519d19dd9c0289feb8a6e7a0f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/remiolsen/qaTools-singularity/latest/2017-10-30-ce54e8d2-dcb1acb5/
recipe: https://datasets.datalad.org/shub/remiolsen/qaTools-singularity/latest/2017-10-30-ce54e8d2-dcb1acb5/Singularity
collection: remiolsen/qaTools-singularity
---

# remiolsen/qaTools-singularity:latest

```bash
$ singularity pull shub://remiolsen/qaTools-singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:9

%label
    Maintainer remi-andre.olsen@scilifelab.se

%post
    apt-get update
    apt-get install -y git build-essential autoconf zlib1g-dev libbz2-dev liblzma-dev wget

    #Fetch things
    wget https://downloads.sourceforge.net/project/samtools/samtools/1.3/samtools-1.3.tar.bz2
    wget https://downloads.sourceforge.net/project/samtools/samtools/1.3/htslib-1.3.tar.bz2
    tar xfj samtools-1.3.tar.bz2
    tar xfj htslib-1.3.tar.bz2
    rm *.bz2
    git clone https://github.com/vezzi/qaTools.git

    #samtools
    cd samtools-1.3
    autoconf -Wno-syntax
    ./configure --without-curses
    make
    make install
    cd htslib-1.3 
    make
    make install
    cd ../..
    cp /usr/local/lib/libhts.* /lib

    #qaTools
    cd qaTools
    make SAMTOOLS=../samtools-1.3 VERSION=1.3
    cp computeInsertSizeHistogram /bin
    cp doBWAQualTrimming /bin
    cp qaCompute /bin
    cp removeUnmapped /bin

    #UPPMAX stuff NOTE: Only testing for now, should use singulary run -B /sw:/sw etc container.img
    mkdir /sw
    mkdir /proj
    mkdir /pica
    mkdir /lupus

    apt-get clean
    rm -rf /var/lib/apt/lists/*

%runscript
    exec qaCompute "$@"
```

## Collection

 - Name: [remiolsen/qaTools-singularity](https://github.com/remiolsen/qaTools-singularity)
 - License: None

