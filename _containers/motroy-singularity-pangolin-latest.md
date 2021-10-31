---
id: 13732
name: "motroy/singularity-pangolin"
branch: "master"
tag: "latest"
commit: "e10803b08b07ae87d74fffec178b7ca9482ce1b7"
version: "140671597cf04a2599ce3c1a5365590c"
build_date: "2020-07-28T14:07:14.879Z"
size_mb: 3716.0
size: 1581895711
sif: "https://datasets.datalad.org/shub/motroy/singularity-pangolin/latest/2020-07-28-e10803b0-14067159/140671597cf04a2599ce3c1a5365590c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/motroy/singularity-pangolin/latest/2020-07-28-e10803b0-14067159/
recipe: https://datasets.datalad.org/shub/motroy/singularity-pangolin/latest/2020-07-28-e10803b0-14067159/Singularity
collection: motroy/singularity-pangolin
---

# motroy/singularity-pangolin:latest

```bash
$ singularity pull shub://motroy/singularity-pangolin:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer motroy

%help
This container runs pangolin

%environment
    export PATH=/opt/miniconda3/bin:/opt/miniconda3/envs/pangolin/bin:/pangolin/pangolin/:/pangolin/pangolin/data:/pangolin/pangolin/scripts:/lineages/:/lineages/lineages/:/pangoLEARN:/pangoLEARN/pangoLEARN:$PATH
    export OMPI_MCA_opal_cuda_support=true

%runscript
    eval "$(conda shell.bash hook)"
    source /opt/miniconda3/etc/profile.d/conda.sh
    conda activate pangolin
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
        r-base \
        r-cran-ape r-cran-optparse \
        curl wget less locate openssh-server zlib1g-dev libboost-all-dev \
        perl libmoo-perl liblist-moreutils-perl libjson-perl fastqc pkg-config \
        libfreetype6-dev libpng-dev python-matplotlib #python3 python3-numpy python3-scipy python3-pip
    apt-get clean
    echo "LC_ALL=en_US.UTF-8" >> /etc/environment
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    echo "LANG=en_US.UTF-8" > /etc/locale.conf
    locale-gen en_US.UTF-8

    # Install miniconda
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda3.sh
    bash miniconda3.sh -b -p /opt/miniconda3
    rm miniconda3.sh
    export PATH="/opt/miniconda3/bin:/opt/miniconda3/envs/pangolin/bin:/pangolin/pangolin/:/pangolin/pangolin/data:/pangolin/pangolin/scripts:/lineages/:/lineages/lineages:/pangoLEARN:/pangoLEARN/pangoLEARN:$PATH"
    export OMPI_MCA_opal_cuda_support=true

    # Install pangolin
    conda config --file /.condarc --add channels defaults && \
          conda config --file /.condarc --add channels conda-forge && \
          conda config --file /.condarc --add channels bioconda && \
          conda config --file /.condarc --add channels r
    conda update -n base -c defaults conda
    git clone https://github.com/cov-lineages/pangolin.git /pangolin
    conda env create -n pangolin -f /pangolin/environment.yml
    cd /pangolin && /opt/miniconda3/bin/python3 setup.py install
    /opt/miniconda3/bin/python3 -m pip install snakemake==5.13.0
    /opt/miniconda3/bin/python3 -m pip install lineages
    git clone https://github.com/cov-lineages/lineages.git /lineages
    cd /lineages && /opt/miniconda3/bin/python3 setup.py install
    git clone https://github.com/cov-lineages/pangoLEARN.git /pangoLEARN
    cd /pangoLEARN && /opt/miniconda3/bin/python3 setup.py install
```

## Collection

 - Name: [motroy/singularity-pangolin](https://github.com/motroy/singularity-pangolin)
 - License: [MIT License](https://api.github.com/licenses/mit)

