---
id: 8253
name: "mcw-rcc/qiime2"
branch: "2019.1"
tag: "2019.1"
commit: "54bbd74484f0905b38501679aa8eec04d6bc22ee"
version: "50f870c880b591f43158b8c73b30d995"
build_date: "2020-03-06T12:26:31.495Z"
size_mb: 6683
size: 2891517983
sif: "https://datasets.datalad.org/shub/mcw-rcc/qiime2/2019.1/2020-03-06-54bbd744-50f870c8/50f870c880b591f43158b8c73b30d995.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mcw-rcc/qiime2/2019.1/2020-03-06-54bbd744-50f870c8/
recipe: https://datasets.datalad.org/shub/mcw-rcc/qiime2/2019.1/2020-03-06-54bbd744-50f870c8/Singularity
collection: mcw-rcc/qiime2
---

# mcw-rcc/qiime2:2019.1

```bash
$ singularity pull shub://mcw-rcc/qiime2:2019.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer Matthew Flister
Version 2019.1

%help
This container runs QIIME2.

%environment
    export PATH=/opt/miniconda3/bin:$PATH

%runscript
    source activate qiime2-2019.1
    exec qiime "${@}"

%post
    # default mount points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts
    
    # Install necessary packages
    apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc-multilib \
        ca-certificates \
        locales \
        wget
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
    
    # Install QIIME 2
    wget https://data.qiime2.org/distro/core/qiime2-2019.1-py36-linux-conda.yml
    conda env create -n qiime2-2019.1 --file qiime2-2019.1-py36-linux-conda.yml
    rm qiime2-2019.1-py36-linux-conda.yml
```

## Collection

 - Name: [mcw-rcc/qiime2](https://github.com/mcw-rcc/qiime2)
 - License: [MIT License](https://api.github.com/licenses/mit)

