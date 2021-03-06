---
id: 5780
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "purge_haplotigs_20181203"
commit: "a71c1166c631da09a93008cf17385f0ab9b0c597"
version: "02c2d344b2d1f5938b4dd9b38922a4bb"
build_date: "2020-01-06T22:06:14.715Z"
size_mb: 2586
size: 969924639
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/purge_haplotigs_20181203/2020-01-06-a71c1166-02c2d344/02c2d344b2d1f5938b4dd9b38922a4bb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/purge_haplotigs_20181203/2020-01-06-a71c1166-02c2d344/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/purge_haplotigs_20181203/2020-01-06-a71c1166-02c2d344/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:purge_haplotigs_20181203

```bash
$ singularity pull shub://TomHarrop/singularity-containers:purge_haplotigs_20181203
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/verse:3.5.1 

%help

    Container for purge_haplotigs
    https://bitbucket.org/mroachawri/purge_haplotigs

%labels

    VERSION "purge_haplotigs 20181203"

%post

    # dependencies
    apt-get update
    apt-get install -y \
        bedtools \
        build-essential \
        fig2dev \
        gnuplot \
        samtools \
        wget \
        zlib1g-dev \
        xfig


    # install minimap2
    wget -O "minimap2.tar.gz" \
        --no-check-certificate \
        https://github.com/lh3/minimap2/archive/v2.11.tar.gz
    mkdir minimap2
    tar -zxf minimap2.tar.gz \
        -C minimap2 \
        --strip-components 1

    cd minimap2 || exit 1
    make
    mv minimap2 /usr/local/bin/

    cd .. || exit 1
    rm -rf minimap2 minimap2.tar.gz

    # install mummer
    wget -O "mummer.tar.gz" \
        --no-check-certificate \
        https://github.com/mummer4/mummer/releases/download/v4.0.0beta2/mummer-4.0.0beta2.tar.gz
    mkdir mummer-install
    tar -zxf mummer.tar.gz \
        -C mummer-install \
        --strip-components 1
    cd mummer-install || exit 1
    ./configure && make && make install
    cd .. || exit 1
    rm -rf mummer.tar.gz mummer-install
    ldconfig

    # clone
    git clone https://bitbucket.org/mroachawri/purge_haplotigs.git

%environment

    export PATH="${PATH}:/purge_haplotigs/bin"

%runscript

    exec /purge_haplotigs/bin/purge_haplotigs "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

