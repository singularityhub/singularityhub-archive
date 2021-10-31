---
id: 4910
name: "mcw-rcc/qiime2"
branch: "master"
tag: "2018.8"
commit: "6d96cb4d44b350b79d92fd83a0be20d136f8bea4"
version: "40865686fbaf6ed8ecb66a6c7a225f88"
build_date: "2018-09-19T22:54:40.158Z"
size_mb: 6477
size: 2875527199
sif: "https://datasets.datalad.org/shub/mcw-rcc/qiime2/2018.8/2018-09-19-6d96cb4d-40865686/40865686fbaf6ed8ecb66a6c7a225f88.simg"
url: https://datasets.datalad.org/shub/mcw-rcc/qiime2/2018.8/2018-09-19-6d96cb4d-40865686/
recipe: https://datasets.datalad.org/shub/mcw-rcc/qiime2/2018.8/2018-09-19-6d96cb4d-40865686/Singularity
collection: mcw-rcc/qiime2
---

# mcw-rcc/qiime2:2018.8

```bash
$ singularity pull shub://mcw-rcc/qiime2:2018.8
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer Matthew Flister
Version 2018.8

%help
This container runs QIIME2.

%environment
    export PATH=/opt/miniconda3/bin:$PATH

%runscript
    source activate qiime2-2018.8
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
    wget https://data.qiime2.org/distro/core/qiime2-2018.8-py35-linux-conda.yml
    conda env create -n qiime2-2018.8 --file qiime2-2018.8-py35-linux-conda.yml
    rm qiime2-2018.8-py35-linux-conda.yml
```

## Collection

 - Name: [mcw-rcc/qiime2](https://github.com/mcw-rcc/qiime2)
 - License: [MIT License](https://api.github.com/licenses/mit)

