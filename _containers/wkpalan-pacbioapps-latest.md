---
id: 6922
name: "wkpalan/pacbioapps"
branch: "master"
tag: "latest"
commit: "6eaffab64105f3e4c7db07e24b795530a93ba0e3"
version: "049485f25dab1606638b03cd672ccc45"
build_date: "2019-02-09T23:03:29.251Z"
size_mb: 1405
size: 545005599
sif: "https://datasets.datalad.org/shub/wkpalan/pacbioapps/latest/2019-02-09-6eaffab6-049485f2/049485f25dab1606638b03cd672ccc45.simg"
url: https://datasets.datalad.org/shub/wkpalan/pacbioapps/latest/2019-02-09-6eaffab6-049485f2/
recipe: https://datasets.datalad.org/shub/wkpalan/pacbioapps/latest/2019-02-09-6eaffab6-049485f2/Singularity
collection: wkpalan/pacbioapps
---

# wkpalan/pacbioapps:latest

```bash
$ singularity pull shub://wkpalan/pacbioapps:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
Maintainer Matthew Flister
Version v1.0

%help
This container runs includes several PacBio apps.

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
    conda install -c bioconda pbccs bax2bam lima bam2fastx pbmm2
    mkdir /media/data
```

## Collection

 - Name: [wkpalan/pacbioapps](https://github.com/wkpalan/pacbioapps)
 - License: [MIT License](https://api.github.com/licenses/mit)

