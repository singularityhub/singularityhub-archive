---
id: 8257
name: "monaghaa/salmon"
branch: "master"
tag: "latest"
commit: "8fde9fbb35271ce22b700b6fd00a60da69b52613"
version: "66bd6d1f12f5a41badd00386a0566b90"
build_date: "2020-09-23T13:58:58.267Z"
size_mb: 1999
size: 751013919
sif: "https://datasets.datalad.org/shub/monaghaa/salmon/latest/2020-09-23-8fde9fbb-66bd6d1f/66bd6d1f12f5a41badd00386a0566b90.simg"
url: https://datasets.datalad.org/shub/monaghaa/salmon/latest/2020-09-23-8fde9fbb-66bd6d1f/
recipe: https://datasets.datalad.org/shub/monaghaa/salmon/latest/2020-09-23-8fde9fbb-66bd6d1f/Singularity
collection: monaghaa/salmon
---

# monaghaa/salmon:latest

```bash
$ singularity pull shub://monaghaa/salmon:latest
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
    conda install -y -c bioconda salmon
    

%environment
    export LANG=en_US.UTF-8
    export LANGUAGE=en_US:en
    export LC_ALL=en_US.UTF-8
    export XDG_RUNTIME_DIR=""
export PATH=/opt/miniconda3/bin:$PATH
```

## Collection

 - Name: [monaghaa/salmon](https://github.com/monaghaa/salmon)
 - License: None

