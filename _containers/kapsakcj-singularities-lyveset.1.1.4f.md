---
id: 8595
name: "kapsakcj/singularities"
branch: "master"
tag: "lyveset.1.1.4f"
commit: "a0d2f44f31f165690e809d1470290c36662ce3ea"
version: "0848eee9a4a1b5ed141defee44cc9d7b"
build_date: "2019-04-30T20:21:09.221Z"
size_mb: 2901
size: 1248505887
sif: "https://datasets.datalad.org/shub/kapsakcj/singularities/lyveset.1.1.4f/2019-04-30-a0d2f44f-0848eee9/0848eee9a4a1b5ed141defee44cc9d7b.simg"
url: https://datasets.datalad.org/shub/kapsakcj/singularities/lyveset.1.1.4f/2019-04-30-a0d2f44f-0848eee9/
recipe: https://datasets.datalad.org/shub/kapsakcj/singularities/lyveset.1.1.4f/2019-04-30-a0d2f44f-0848eee9/Singularity
collection: kapsakcj/singularities
---

# kapsakcj/singularities:lyveset.1.1.4f

```bash
$ singularity pull shub://kapsakcj/singularities:lyveset.1.1.4f
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial

%help
### This is the help for building a singularity image from a recipe (sudo priveleges required).
### To build me into an image, run:
    sudo singularity build my-new-lyveset-image.simg /path/to/lyveset/1.1.4f/Singularity.lyveset.1.1.4f
### If the image already exists, add the --force flag to overwrite
    sudo singularity build --force my-new-lyveset-image.simg /path/to/lyveset/1.1.4f/Singularity.lyveset.1.1.4f

#### Then to run in an interactive shell run:
    singularity shell my-new-lyveset-image.simg
    launch_set.pl [options]

#### To run without interactive shell
    singularity exec my-new-lyveset-image.simg launch_set.pl [options]

%labels
    MAINTAINER Curtis Kapsak
    SINGULARITY-IMAGE-VERSION 1.0.0
    SOFTWARE-VERSION 1.1.4f
    SOFTWARE-WEBSITE https://github.com/lskatz/lyve-SET/
    SOFTWARE-LICENSE https://github.com/lskatz/lyve-SET/blob/master/LICENSE

%environment
    PATH=${PATH}:/edirect:/lyve-SET-1.1.4f:/lyve-SET-1.1.4f/scripts
    export PATH
    export LC_ALL=C

%post
    apt-get update
    apt-get -y install wget \
                       perl \
                       libfile-slurp-perl \
                       openjdk-9-jre \
                       bioperl \
                       zlib1g-dev \
                       libncurses5-dev \
                       libncursesw5-dev \
                       make \
                       build-essential \
                       ncbi-blast+ \
                       libsvn-perl \
                       subversion \
                       libsvn1 \
                       automake1.11 \
                       libpthread-stubs0-dev \
                       cpanminus \
                       git \
                       clang \
                       mpich
    apt-get clean
    apt-get autoclean
    # install edirect
    wget ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/edirect.tar.gz
    tar -xzf edirect.tar.gz
    rm edirect.tar.gz
    cd edirect
    ./setup.sh
    # install smalt
    cd /
    wget --max-redirect 50 --continue 'https://downloads.sourceforge.net/project/smalt/smalt-0.7.6-static.tar.gz' -O smalt-0.7.6-static.tar.gz
    tar -zxf smalt-0.7.6-static.tar.gz
    rm smalt-0.7.6-static.tar.gz
    cd smalt-0.7.6
    ./configure
    make
    make install
    # get lyveset files
    cd /
    wget https://github.com/lskatz/lyve-SET/archive/v1.1.4f.tar.gz
    tar -xzf v1.1.4f.tar.gz
    rm v1.1.4f.tar.gz
    # install perl modules
    cpanm Test::Most Bio::FeatureIO String::Escape File::Slurp URI::Escape
    # install lyveset
    cd lyve-SET-1.1.4f
    make install
    make env
    # make /data directory for mounting volume
    mkdir /data

%runscript
    echo "This runscript shows Lyve-SET help options"
    launch_set.pl
    echo ""
    echo ""
    echo ""
    echo 'Run "singularity help name-of-lyveset-image.simg" for more help on running the image'
    echo ""
```

## Collection

 - Name: [kapsakcj/singularities](https://github.com/kapsakcj/singularities)
 - License: [MIT License](https://api.github.com/licenses/mit)

