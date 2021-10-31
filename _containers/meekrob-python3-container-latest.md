---
id: 8731
name: "meekrob/python3-container"
branch: "master"
tag: "latest"
commit: "57708548adf1730793f27a6a3f290f730fed84b3"
version: "e327cca805f25b201c102422b69bbad6"
build_date: "2021-01-27T21:59:28.751Z"
size_mb: 3930.0
size: 1570639903
sif: "https://datasets.datalad.org/shub/meekrob/python3-container/latest/2021-01-27-57708548-e327cca8/e327cca805f25b201c102422b69bbad6.sif"
url: https://datasets.datalad.org/shub/meekrob/python3-container/latest/2021-01-27-57708548-e327cca8/
recipe: https://datasets.datalad.org/shub/meekrob/python3-container/latest/2021-01-27-57708548-e327cca8/Singularity
collection: meekrob/python3-container
---

# meekrob/python3-container:latest

```bash
$ singularity pull shub://meekrob/python3-container:latest
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
    conda install -y -c bioconda numpy pandas scikit-learn deeptools ArviZ pymc3 meme proteinortho ac-diamond


%environment
    export LANG=en_US.UTF-8
    export LANGUAGE=en_US:en
    export LC_ALL=en_US.UTF-8
    export XDG_RUNTIME_DIR=""
export PATH=/opt/miniconda3/bin:$PATH
```

## Collection

 - Name: [meekrob/python3-container](https://github.com/meekrob/python3-container)
 - License: None

