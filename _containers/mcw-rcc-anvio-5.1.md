---
id: 4781
name: "mcw-rcc/anvio"
branch: "master"
tag: "5.1"
commit: "a06ef7c2dec241f46782ad202265878c08248377"
version: "e149ed2f37bf3ffe0ef8b740017dba00"
build_date: "2019-08-28T21:51:40.441Z"
size_mb: 4989
size: 2085060639
sif: "https://datasets.datalad.org/shub/mcw-rcc/anvio/5.1/2019-08-28-a06ef7c2-e149ed2f/e149ed2f37bf3ffe0ef8b740017dba00.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mcw-rcc/anvio/5.1/2019-08-28-a06ef7c2-e149ed2f/
recipe: https://datasets.datalad.org/shub/mcw-rcc/anvio/5.1/2019-08-28-a06ef7c2-e149ed2f/Singularity
collection: mcw-rcc/anvio
---

# mcw-rcc/anvio:5.1

```bash
$ singularity pull shub://mcw-rcc/anvio:5.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer Matthew Flister
Version 09.12.18

%help
This container runs anvi'o 5.1.0.

%environment
    SHELL=/bin/bash
    export PATH="/opt/miniconda3/bin:$PATH"

%post
    # default mount points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts

    # Install necessary packages
    apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc-multilib \
        libboost-all-dev \
        libhdf5-serial-dev \
        zlib1g-dev \
        python3-pip \
        pkg-config \
        python3-dev \
        python3-setuptools \
        wget
    apt-get clean

    # install miniconda
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda3.sh
    bash miniconda3.sh -b -p /opt/miniconda3
    rm miniconda3.sh
    export PATH="/opt/miniconda3/bin:$PATH"

    # install pacbio apps
    conda install -c bioconda -c conda-forge anvio diamond bwa
```

## Collection

 - Name: [mcw-rcc/anvio](https://github.com/mcw-rcc/anvio)
 - License: [MIT License](https://api.github.com/licenses/mit)

