---
id: 15089
name: "BrendelGroup/AllRice"
branch: "main"
tag: "ddn"
commit: "edf58bf226f68cd8ce71ed7ae55380a02f32b8b2"
version: "1679aff38c3d3f257f8d644baa0a11681cd2c240f558e50a18be43234ea328d1"
build_date: "2020-12-23T22:17:05.965Z"
size_mb: 1081.09765625
size: 1133613056
sif: "https://datasets.datalad.org/shub/BrendelGroup/AllRice/ddn/2020-12-23-edf58bf2-1679aff3/1679aff38c3d3f257f8d644baa0a11681cd2c240f558e50a18be43234ea328d1.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/BrendelGroup/AllRice/ddn/2020-12-23-edf58bf2-1679aff3/
recipe: https://datasets.datalad.org/shub/BrendelGroup/AllRice/ddn/2020-12-23-edf58bf2-1679aff3/Singularity
collection: BrendelGroup/AllRice
---

# BrendelGroup/AllRice:ddn

```bash
$ singularity pull shub://BrendelGroup/AllRice:ddn
```

## Singularity Recipe

```singularity
bootstrap: docker
From: ubuntu:14.04

%help
    This container provides a working version of DiscovarDeNovo.
    (Note: The code does not compile on newer gcc versions in our hands.)

%post
    export DEBIAN_FRONTEND=noninteractive
    apt -y update
    apt -y install build-essential
    apt -y install git tcsh tzdata unzip wget zip
    apt -y install ncurses-dev libcurl4-openssl-dev zlib1g-dev libbz2-dev liblzma-dev
    apt -y install libjemalloc-dev
    apt -y install python python-biopython


### Installing prerequisites and DiscovarDeNovo

    echo 'Installing HTSLIB from http://www.htslib.org/ '
    cd /opt
    git clone git://github.com/samtools/htslib.git htslib
    cd htslib
    make && make install

    echo 'Installing SAMTOOLS from http://www.htslib.org/ '
    cd /opt
    git clone git://github.com/samtools/samtools.git samtools
    cd samtools
    make && make install

    echo 'Installing DiscovarDenovo from https://software.broadinstitute.org/software/discovar/blog/ '
    cd /opt
    wget ftp://ftp.broadinstitute.org/pub/crd/DiscovarDeNovo/latest_source_code/discovardenovo-52488.tar.gz
    tar xzf discovardenovo-52488.tar.gz
    cd discovardenovo-52488
    ./configure
    make && make install


### Installing additional software

    echo 'Installing scripts from AllRice repository '
    cd /opt
    git clone https://github.com/BrendelGroup/AllRice
    cp AllRice/bin/* /usr/local/bin


%environment
    export LC_ALL=C

%labels
    Maintainer vpbrendel
    Version v1.1
```

## Collection

 - Name: [BrendelGroup/AllRice](https://github.com/BrendelGroup/AllRice)
 - License: None

