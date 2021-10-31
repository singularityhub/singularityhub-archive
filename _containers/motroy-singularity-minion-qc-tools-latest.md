---
id: 14019
name: "motroy/singularity-minion-qc-tools"
branch: "master"
tag: "latest"
commit: "6d9bdcce8dc3363ebff58c06bdfe4fb31b4f7362"
version: "f0f6ac2f3321355decca297234d1320f"
build_date: "2020-08-23T11:54:27.530Z"
size_mb: 3631.0
size: 1607970847
sif: "https://datasets.datalad.org/shub/motroy/singularity-minion-qc-tools/latest/2020-08-23-6d9bdcce-f0f6ac2f/f0f6ac2f3321355decca297234d1320f.sif"
url: https://datasets.datalad.org/shub/motroy/singularity-minion-qc-tools/latest/2020-08-23-6d9bdcce-f0f6ac2f/
recipe: https://datasets.datalad.org/shub/motroy/singularity-minion-qc-tools/latest/2020-08-23-6d9bdcce-f0f6ac2f/Singularity
collection: motroy/singularity-minion-qc-tools
---

# motroy/singularity-minion-qc-tools:latest

```bash
$ singularity pull shub://motroy/singularity-minion-qc-tools:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer motroy

%help
This container runs minion QC

%environment
    export PATH=/opt/miniconda3/bin:/minion_qc/:$PATH
    export OMPI_MCA_opal_cuda_support=true

%runscript
    eval "$(conda shell.bash hook)"
    source /opt/miniconda3/etc/profile.d/conda.sh
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
        libfreetype6-dev libpng-dev python-matplotlib #python3 python3-numpy python3-scipy python3-pip
    apt-get clean
    echo "LC_ALL=en_US.UTF-8" >> /etc/environment
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    echo "LANG=en_US.UTF-8" > /etc/locale.conf
    locale-gen en_US.UTF-8

    # Install miniconda
    wget https://repo.continuum.io/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh -O miniconda3.sh
    bash miniconda3.sh -b -p /opt/miniconda3
    rm miniconda3.sh
    export PATH="/opt/miniconda3/bin:$PATH"
    export OMPI_MCA_opal_cuda_support=true

    conda config --file /.condarc --add channels defaults && conda config --file /.condarc --add channels conda-forge && conda config --file /.condarc --add channels r && conda config --file /.condarc --add channels aleg
    conda install -c anaconda yaml
    conda install -c conda-forge r-base r-futile.logger r-optparse r-readr r-viridis
    conda install -c r r-data.table r-dplyr r-ggplot2 r-reshape2 r-scales r-ggplot2 r-yaml
    conda install -c aleg pycoqc
    mkdir /minion_qc
    wget "https://github.com/roblanf/minion_qc/releases/download/1.4.2/MinIONQC.R" -O /minion_qc/MinIONQC-1.4.2.R
    export PATH="/minion_qc/:$PATH"
```

## Collection

 - Name: [motroy/singularity-minion-qc-tools](https://github.com/motroy/singularity-minion-qc-tools)
 - License: [MIT License](https://api.github.com/licenses/mit)

