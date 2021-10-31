---
id: 14079
name: "tylerakonom/rnaseq"
branch: "master"
tag: "latest"
commit: "3fa2919785f0610564d1993148c4036f4aa64ab7"
version: "751d57cc5548d30ec652e7032fab059d"
build_date: "2020-09-03T22:53:40.488Z"
size_mb: 3376.0
size: 1753542687
sif: "https://datasets.datalad.org/shub/tylerakonom/rnaseq/latest/2020-09-03-3fa29197-751d57cc/751d57cc5548d30ec652e7032fab059d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/tylerakonom/rnaseq/latest/2020-09-03-3fa29197-751d57cc/
recipe: https://datasets.datalad.org/shub/tylerakonom/rnaseq/latest/2020-09-03-3fa29197-751d57cc/Singularity
collection: tylerakonom/rnaseq
---

# tylerakonom/rnaseq:latest

```bash
$ singularity pull shub://tylerakonom/rnaseq:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:20.10

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
    #apt-get -y install firefox xpdf
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
    # apt-get -y install build-essential gfortran

    # install some bioinfo tools from Bioconda
    conda create -y -n rnaseq2 -c bioconda cutadapt fastqc hisat2 samtools rsem bowtie2 trimmomatic

#create a runscript so that conda is correctly invoked in bash
echo '#!/bin/bash' >/opt/runscript
echo '. "/opt/miniconda3/etc/profile.d/conda.sh"' >>/opt/runscript
echo 'conda activate rnaseq2' >>/opt/runscript
echo '$@' >>/opt/runscript

%runscript
bash /opt/runscript "$@"

%environment
    export LANG=en_US.UTF-8
    export LANGUAGE=en_US:en
    export LC_ALL=en_US.UTF-8
    export XDG_RUNTIME_DIR=""
```

## Collection

 - Name: [tylerakonom/rnaseq](https://github.com/tylerakonom/rnaseq)
 - License: None

