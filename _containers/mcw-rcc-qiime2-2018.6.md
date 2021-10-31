---
id: 4556
name: "mcw-rcc/qiime2"
branch: "master"
tag: "2018.6"
commit: "75ec4c043a083f5203ade18ac50eaacd1d30ce06"
version: "dc9351c18aecb1006fb25c70266b648d"
build_date: "2018-09-19T22:54:40.165Z"
size_mb: 6755
size: 2937532447
sif: "https://datasets.datalad.org/shub/mcw-rcc/qiime2/2018.6/2018-09-19-75ec4c04-dc9351c1/dc9351c18aecb1006fb25c70266b648d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mcw-rcc/qiime2/2018.6/2018-09-19-75ec4c04-dc9351c1/
recipe: https://datasets.datalad.org/shub/mcw-rcc/qiime2/2018.6/2018-09-19-75ec4c04-dc9351c1/Singularity
collection: mcw-rcc/qiime2
---

# mcw-rcc/qiime2:2018.6

```bash
$ singularity pull shub://mcw-rcc/qiime2:2018.6
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer Matthew Flister
Version 2018.6

%help
This container runs QIIME 2.

%environment
    

%runscript
    source activate qiime2-2018.6
    exec qiime "${@}"

%post
    # default mount points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts
    
    # Install necessary packages
    apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc-multilib \
        ca-certificates \
        wget
    apt-get clean

    # Install miniconda
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda3.sh
    bash miniconda3.sh -b -p /opt/miniconda3
    rm miniconda3.sh
    export PATH="/opt/miniconda3/bin:$PATH"
    
    # Install QIIME 2
    wget https://data.qiime2.org/distro/core/qiime2-2018.6-py35-linux-conda.yml
    conda env create -n qiime2-2018.6 --file qiime2-2018.6-py35-linux-conda.yml
    rm -rf qiime2-2018.6-py35-linux-conda.yml
```

## Collection

 - Name: [mcw-rcc/qiime2](https://github.com/mcw-rcc/qiime2)
 - License: [MIT License](https://api.github.com/licenses/mit)

