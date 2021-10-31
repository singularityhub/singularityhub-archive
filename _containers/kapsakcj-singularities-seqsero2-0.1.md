---
id: 8819
name: "kapsakcj/singularities"
branch: "master"
tag: "seqsero2-0.1"
commit: "f11b870acf21e0c1ecd81831aa68fb91cf8fd1c1"
version: "6e6ed76e1815fb6e55090e2258516b04"
build_date: "2019-05-03T21:23:35.727Z"
size_mb: 935
size: 355098655
sif: "https://datasets.datalad.org/shub/kapsakcj/singularities/seqsero2-0.1/2019-05-03-f11b870a-6e6ed76e/6e6ed76e1815fb6e55090e2258516b04.simg"
url: https://datasets.datalad.org/shub/kapsakcj/singularities/seqsero2-0.1/2019-05-03-f11b870a-6e6ed76e/
recipe: https://datasets.datalad.org/shub/kapsakcj/singularities/seqsero2-0.1/2019-05-03-f11b870a-6e6ed76e/Singularity
collection: kapsakcj/singularities
---

# kapsakcj/singularities:seqsero2-0.1

```bash
$ singularity pull shub://kapsakcj/singularities:seqsero2-0.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial

%help
### This is the help for building a singularity image from a recipe (sudo priveleges required).
### To build me into an image, run:
    sudo singularity build my-new-seqsero2-image.simg /path/to/seqsero2/0.1/Singularity.seqsero2-0.1
### If the image already exists, add the --force flag to overwrite
    sudo singularity build --force my-new-seqsero2-image.simg /path/to/seqsero2/0.1/Singularity.seqsero2-0.1

#### Then to run in an interactive shell run:
    singularity shell my-new-seqsero2-image.simg
    SeqSero2_package.py [options]

#### To run without interactive shell
    singularity exec my-new-seqsero2-image.simg SeqSero2_package.py [options]

%labels
    MAINTAINER Curtis Kapsak
    SINGULARITY-IMAGE-VERSION 1.0.0
    SOFTWARE-VERSION 0.1
    SOFTWARE-WEBSITE https://github.com/denglab/SeqSero2
    SOFTWARE-LICENSE https://github.com/denglab/SeqSero2/blob/master/LICENSE

%environment
    PATH=${PATH}:/SeqSero2-0.1:/SPAdes-3.13.0-Linux/bin:/SalmID-0.123
    export PATH
    export LC_ALL=C

%post
    apt-get update
    apt-get -y install wget \
                       python3 \
                       python3-pip \
                       python3-venv \
                       python-setuptools \
                       curl \
                       file \
                       git \
                       bwa \
                       ncbi-blast+ \
                       sra-toolkit \
                       bedtools \
                       zlib1g-dev \
                       libbz2-dev \
                       liblzma-dev \
                       build-essential \
                       libncurses5-dev \
                       libcurl4-gnutls-dev \
                       libssl-dev \
                       perl \
                       bzip2 \
                       make \
                       gcc
    apt-get clean
    apt-get autoclean

    # install biopython
    pip3 install biopython poetry

    # install samtools
    wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
    tar -xjf samtools-1.9.tar.bz2
    rm samtools-1.9.tar.bz2
    cd samtools-1.9
    ./configure
    make
    make install

    # install SPAdes
    cd /
    wget http://cab.spbu.ru/files/release3.13.0/SPAdes-3.13.0-Linux.tar.gz
    tar -xzf SPAdes-3.13.0-Linux.tar.gz
    rm SPAdes-3.13.0-Linux.tar.gz

    # install SalmID
    git clone https://github.com/hcdenbakker/SalmID.git --branch 0.1.23 --single-branch
    cd SalmID
    poetry build -vvv
    pip3 install dist/salmid*.whl

    # install SeqSero2
    cd /
    wget https://github.com/denglab/SeqSero2/archive/v0.1.tar.gz
    tar -xzf v0.1.tar.gz
    rm v0.1.tar.gz

    # make /data directory for mounting volume
    mkdir /data

%runscript
    echo "This runscript shows SeqSero2 help options"
    SeqSero2_package.py
    echo ""
    echo ""
    echo ""
    echo 'Run "singularity help name-of-seqsero2-image.simg" for more help on running the image'
    echo ""
```

## Collection

 - Name: [kapsakcj/singularities](https://github.com/kapsakcj/singularities)
 - License: [MIT License](https://api.github.com/licenses/mit)

