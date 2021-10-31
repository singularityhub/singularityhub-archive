---
id: 13701
name: "motroy/singularity-sarscov2phylo"
branch: "master"
tag: "latest"
commit: "e7903a34c796f815025c01cd554fd81bccefbab9"
version: "5d12fc5acad3437c9f3840fe96be5df5"
build_date: "2020-07-27T06:55:57.243Z"
size_mb: 3074.0
size: 1277300767
sif: "https://datasets.datalad.org/shub/motroy/singularity-sarscov2phylo/latest/2020-07-27-e7903a34-5d12fc5a/5d12fc5acad3437c9f3840fe96be5df5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/motroy/singularity-sarscov2phylo/latest/2020-07-27-e7903a34-5d12fc5a/
recipe: https://datasets.datalad.org/shub/motroy/singularity-sarscov2phylo/latest/2020-07-27-e7903a34-5d12fc5a/Singularity
collection: motroy/singularity-sarscov2phylo
---

# motroy/singularity-sarscov2phylo:latest

```bash
$ singularity pull shub://motroy/singularity-sarscov2phylo:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer motroy

%help
This container runs sarscov2phylo

%environment
    export PATH=/opt/miniconda3/bin:/opt/miniconda3/envs/sarscov2phylo/bin:/sarscov2phylo/scripts/:$PATH
    export OMPI_MCA_opal_cuda_support=true

%runscript
    eval "$(conda shell.bash hook)"
    source /opt/miniconda3/etc/profile.d/conda.sh
    conda activate sarscov2phylo
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
    export PATH="/opt/miniconda3/bin:/opt/miniconda3/envs/sarscov2phylo/bin:/sarscov2phylo/scripts/:$PATH"
    export OMPI_MCA_opal_cuda_support=true

    # Install sarscov2phylo
    conda config --file /.condarc --add channels defaults && \
          conda config --file /.condarc --add channels conda-forge && \
          conda config --file /.condarc --add channels bioconda && \
          conda config --file /.condarc --add channels r
    conda update -n base -c defaults conda
    cd / && git clone https://github.com/roblanf/sarscov2phylo.git
    cd /sarscov2phylo
    conda env create -f /sarscov2phylo/environment.yml
    conda install openssl -n sarscov2phylo
    conda install -c bioconda seqkit -n sarscov2phylo
    #conda install -c r r-optparse r-ape -n sarscov2phylo
    #pip install pandas==1.0.1
    #pip install pytools==2020.1
    #pip install dendropy>=4.4.0
    #pip install git+https://github.com/hCoV-2019/lineages.git
    #pip install git+https://github.com/hCoV-2019/pangolin
    #pip install dendropy==4.4.0
    #pip install pysam==0.15.4
    #pip install git+https://github.com/hCoV-2019/pangolin
```

## Collection

 - Name: [motroy/singularity-sarscov2phylo](https://github.com/motroy/singularity-sarscov2phylo)
 - License: [MIT License](https://api.github.com/licenses/mit)

