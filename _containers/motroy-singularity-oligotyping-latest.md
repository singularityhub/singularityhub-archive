---
id: 14002
name: "motroy/singularity-oligotyping"
branch: "master"
tag: "latest"
commit: "765479d1ab5f5fabe0d7566b079bebd9f770d9fb"
version: "f4136f17581309a21b28604ab47d0561"
build_date: "2020-08-20T07:38:06.227Z"
size_mb: 3149.0
size: 1322545183
sif: "https://datasets.datalad.org/shub/motroy/singularity-oligotyping/latest/2020-08-20-765479d1-f4136f17/f4136f17581309a21b28604ab47d0561.sif"
url: https://datasets.datalad.org/shub/motroy/singularity-oligotyping/latest/2020-08-20-765479d1-f4136f17/
recipe: https://datasets.datalad.org/shub/motroy/singularity-oligotyping/latest/2020-08-20-765479d1-f4136f17/Singularity
collection: motroy/singularity-oligotyping
---

# motroy/singularity-oligotyping:latest

```bash
$ singularity pull shub://motroy/singularity-oligotyping:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer motroy

%help
This container runs oligotyping

%environment
    export PATH=/opt/miniconda3/bin:$PATH
    export OMPI_MCA_opal_cuda_support=true

%runscript
    eval "$(conda shell.bash hook)"
    source /opt/miniconda2/etc/profile.d/conda.sh
    #conda activate pangolin
    #exec qiime "${@}"

%post
    # default mount points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts

    # Install necessary packages
    apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc-multilib \
        ca-certificates \
        locales \
        git \
        libjpeg62 \
        curl wget less locate openssh-server zlib1g-dev libboost-all-dev \
        perl libmoo-perl liblist-moreutils-perl libjson-perl fastqc pkg-config \
        libfreetype6-dev libpng-dev #python-matplotlib #python3 python3-numpy python3-scipy python3-pip
        #r-base \
        #r-cran-ape r-cran-optparse \
    apt-get clean
    echo "LC_ALL=en_US.UTF-8" >> /etc/environment
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    echo "LANG=en_US.UTF-8" > /etc/locale.conf
    locale-gen en_US.UTF-8

    # Install miniconda
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda3.sh
    bash miniconda3.sh -b -p /opt/miniconda3
    rm miniconda3.sh
    export PATH="/opt/miniconda3/bin:$PATH"
    export OMPI_MCA_opal_cuda_support=true

    # Install oligotyping
    conda config --file /.condarc --add channels defaults && \
          conda config --file /.condarc --add channels conda-forge && \
          conda config --file /.condarc --add channels bioconda && \
          conda config --file /.condarc --add channels r
    conda update -n base -c defaults conda
    conda install -c conda-forge mamba
    mamba install -c conda-forge -y r-base pip r-vegan
    mamba install -c bioconda -y blast=2.9.0
    mamba install -c r -c conda-forge -y r-ggplot2 r-gplots r-gtools r-reshape r-optparse r-pheatmap r-rcolorbrewer r-compute.es
    pip install oligotyping
```

## Collection

 - Name: [motroy/singularity-oligotyping](https://github.com/motroy/singularity-oligotyping)
 - License: [MIT License](https://api.github.com/licenses/mit)

