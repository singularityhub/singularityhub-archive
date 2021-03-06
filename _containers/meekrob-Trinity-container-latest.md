---
id: 8319
name: "meekrob/Trinity-container"
branch: "master"
tag: "latest"
commit: "718ad62431de1484342a110ef6538dc9d69f1fc0"
version: "fb8cba4f98e3903af80a143276fa9038"
build_date: "2019-04-25T22:56:40.440Z"
size_mb: 3099
size: 1347694623
sif: "https://datasets.datalad.org/shub/meekrob/Trinity-container/latest/2019-04-25-718ad624-fb8cba4f/fb8cba4f98e3903af80a143276fa9038.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/meekrob/Trinity-container/latest/2019-04-25-718ad624-fb8cba4f/
recipe: https://datasets.datalad.org/shub/meekrob/Trinity-container/latest/2019-04-25-718ad624-fb8cba4f/Singularity
collection: meekrob/Trinity-container
---

# meekrob/Trinity-container:latest

```bash
$ singularity pull shub://meekrob/Trinity-container:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

##################################
# Based on Andy's repo at https://github.com/monaghaa/salmon

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
    conda install -y -c bioconda salmon trinity jellyfish numpy


%environment
    export LANG=en_US.UTF-8
    export LANGUAGE=en_US:en
    export LC_ALL=en_US.UTF-8
    export XDG_RUNTIME_DIR=""
export PATH=/opt/miniconda3/bin:$PATH
```

## Collection

 - Name: [meekrob/Trinity-container](https://github.com/meekrob/Trinity-container)
 - License: None

