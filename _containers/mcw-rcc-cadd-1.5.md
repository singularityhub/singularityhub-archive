---
id: 8027
name: "mcw-rcc/cadd"
branch: "master"
tag: "1.5"
commit: "5aaafdcc0fb9b92bdd44eef5daa83f85f3e287ec"
version: "c02100da201ac1f07fbce76a8fffd4f2"
build_date: "2019-03-29T19:18:16.702Z"
size_mb: 2738
size: 1055682591
sif: "https://datasets.datalad.org/shub/mcw-rcc/cadd/1.5/2019-03-29-5aaafdcc-c02100da/c02100da201ac1f07fbce76a8fffd4f2.simg"
url: https://datasets.datalad.org/shub/mcw-rcc/cadd/1.5/2019-03-29-5aaafdcc-c02100da/
recipe: https://datasets.datalad.org/shub/mcw-rcc/cadd/1.5/2019-03-29-5aaafdcc-c02100da/Singularity
collection: mcw-rcc/cadd
---

# mcw-rcc/cadd:1.5

```bash
$ singularity pull shub://mcw-rcc/cadd:1.5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer Matthew Flister

%help
This container runs CADD.

%environment
    export PATH=/opt/miniconda2/bin:$PATH

%runscript
    exec /opt/CADD-scripts/CADD.sh "${@}"

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
        wget
    apt-get clean
    echo "LC_ALL=en_US.UTF-8" >> /etc/environment
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    echo "LANG=en_US.UTF-8" > /etc/locale.conf
    locale-gen en_US.UTF-8

    # Install miniconda
    wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O miniconda2.sh
    bash miniconda2.sh -b -p /opt/miniconda2
    rm miniconda2.sh
    export PATH="/opt/miniconda2/bin:$PATH"
    
    # Install CADD
    cd /opt && git clone https://github.com/kircherlab/CADD-scripts.git
    cd CADD-scripts && conda env create -f src/environment_v1.5.yml

    # setup data
    ln -s /rcc/stor1/refdata/cadd/v1.5/data/annotations/GRCh37_v1.4 /opt/CADD-scripts/data/annotations/GRCh37_v1.4
    ln -s /rcc/stor1/refdata/cadd/v1.5/data/prescored /opt/CADD-scripts/data/prescored
```

## Collection

 - Name: [mcw-rcc/cadd](https://github.com/mcw-rcc/cadd)
 - License: [MIT License](https://api.github.com/licenses/mit)

