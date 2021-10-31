---
id: 8255
name: "monaghaa/rnaseq"
branch: "master"
tag: "latest"
commit: "afd0a9d796e60b56073552e163521acea3b8fb89"
version: "863e93f5337fb6e12c345d46972cd8ae"
build_date: "2020-08-28T18:29:33.405Z"
size_mb: 3624
size: 1759973407
sif: "https://datasets.datalad.org/shub/monaghaa/rnaseq/latest/2020-08-28-afd0a9d7-863e93f5/863e93f5337fb6e12c345d46972cd8ae.simg"
url: https://datasets.datalad.org/shub/monaghaa/rnaseq/latest/2020-08-28-afd0a9d7-863e93f5/
recipe: https://datasets.datalad.org/shub/monaghaa/rnaseq/latest/2020-08-28-afd0a9d7-863e93f5/Singularity
collection: monaghaa/rnaseq
---

# monaghaa/rnaseq:latest

```bash
$ singularity pull shub://monaghaa/rnaseq:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

##################################
#notes from andy:

#I didn't check to see if any genomics databases were needed
#these can generally be installed outside the container
#but sometimes they need environment variables to be set 
##################################

%post

    # install some system deps
    apt-get -y update
    apt-get -y install locales curl bzip2 less unzip git wget vim ant default-jdk
    # this is a X11 dep
    apt-get -y install libxext6
    # tools to open PDF and HTML files
    apt-get -y install firefox xpdf
    # some extra devel libs
    apt-get -y install zlib1g-dev libssl-dev libpng-dev uuid-dev
    # other
    locale-gen en_US.UTF-8
    apt-get clean

    # download and install miniconda3
    curl -sSL -O https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh -p /opt/miniconda3 -b
    rm -fr Miniconda3-latest-Linux-x86_64.sh
    export PATH=/opt/miniconda3/bin:$PATH
    conda update -n base conda
    conda config --add channels conda-forge
    conda config --add channels bioconda

    # install some dependencies to build R packages
    apt-get -y install build-essential gfortran

    # install some bioinfo tools from Bioconda
    conda install -y -c bioconda cutadapt fastqc hisat2 samtools rsem bowtie2
    

%environment
    export LANG=en_US.UTF-8
    export LANGUAGE=en_US:en
    export LC_ALL=en_US.UTF-8
    export XDG_RUNTIME_DIR=""
    export PATH=/opt/miniconda3/bin:$PATH
```

## Collection

 - Name: [monaghaa/rnaseq](https://github.com/monaghaa/rnaseq)
 - License: None

