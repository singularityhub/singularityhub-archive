---
id: 6106
name: "mcw-meier-lab/Singularity"
branch: "master"
tag: "dcm2niix"
commit: "9ad4e4abe3c43ca5ce5292fefa5482ba4f7a8785"
version: "5198cd813a6806e3ef33425d7cbfe05e"
build_date: "2019-01-04T07:48:36.634Z"
size_mb: 519
size: 203509791
sif: "https://datasets.datalad.org/shub/mcw-meier-lab/Singularity/dcm2niix/2019-01-04-9ad4e4ab-5198cd81/5198cd813a6806e3ef33425d7cbfe05e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mcw-meier-lab/Singularity/dcm2niix/2019-01-04-9ad4e4ab-5198cd81/
recipe: https://datasets.datalad.org/shub/mcw-meier-lab/Singularity/dcm2niix/2019-01-04-9ad4e4ab-5198cd81/Singularity
collection: mcw-meier-lab/Singularity
---

# mcw-meier-lab/Singularity:dcm2niix

```bash
$ singularity pull shub://mcw-meier-lab/Singularity:dcm2niix
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
    Maintainer Lezlie Espana
    Version v1.0

%help
    This is a test container for installing dcm2niix.

%post
    mkdir -p /scratch/global /scratch/local
    apt-get update && apt-get install -y git \
        build-essential \
        gcc-multilib \
        curl \
        bc \
        wget \
        tcsh \
        python \
        cmake \
        pkg-config

    #dcm2niix
    git clone https://github.com/rordenlab/dcm2niix.git
    cd dcm2niix && mkdir build && cd build
    cmake ..
    make install

    echo 'export PATH=/dcm2niix/build/bin:$PATH' >> $SINGULARITY_ENVIRONMENT
    export PATH=/dcm2niix/build/bin:$PATH

    apt-get update
    apt-get clean
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [mcw-meier-lab/Singularity](https://github.com/mcw-meier-lab/Singularity)
 - License: None

