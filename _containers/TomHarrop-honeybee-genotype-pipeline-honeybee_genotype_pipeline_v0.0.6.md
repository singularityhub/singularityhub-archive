---
id: 11974
name: "TomHarrop/honeybee-genotype-pipeline"
branch: "master"
tag: "honeybee_genotype_pipeline_v0.0.6"
commit: "3b7c30d651181780938811a8c51142df2c39a0ad"
version: "2d7d7d29e6790ddd7bc542e2b7a57f815c27dad9aadb03f25dcb340532147103"
build_date: "2020-01-10T01:08:50.865Z"
size_mb: 791.4453125
size: 829890560
sif: "https://datasets.datalad.org/shub/TomHarrop/honeybee-genotype-pipeline/honeybee_genotype_pipeline_v0.0.6/2020-01-10-3b7c30d6-2d7d7d29/2d7d7d29e6790ddd7bc542e2b7a57f815c27dad9aadb03f25dcb340532147103.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/honeybee-genotype-pipeline/honeybee_genotype_pipeline_v0.0.6/2020-01-10-3b7c30d6-2d7d7d29/
recipe: https://datasets.datalad.org/shub/TomHarrop/honeybee-genotype-pipeline/honeybee_genotype_pipeline_v0.0.6/2020-01-10-3b7c30d6-2d7d7d29/Singularity
collection: TomHarrop/honeybee-genotype-pipeline
---

# TomHarrop/honeybee-genotype-pipeline:honeybee_genotype_pipeline_v0.0.6

```bash
$ singularity pull shub://TomHarrop/honeybee-genotype-pipeline:honeybee_genotype_pipeline_v0.0.6
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help
    Container for honeybee-genotype-pipeline v0.0.6
    https://github.com/tomharrop/honeybee-genotype-pipeline

    bbmap 38.73
    bwa 0.7.17-r1188
    freebayes 1.3.1
    python 3.7.5
    R 3.6.1 with data.table 1.12.6 and ggplot2 3.2.1
    samtools 1.9 and bcftools 1.9 using htslib 1.9
    vcflib 1.0.1
    vcftools 0.1.16

%labels
    MAINTAINER "Tom Harrop"

%runscript
    exec /usr/local/bin/honeybee_genotype_pipeline "$@"

%environment
    export PATH="${PATH}:/vcflib/bin:/freebayes/bin:/freebayes/scripts"
    export LC_ALL=C

%post
        export DEBIAN_FRONTEND=noninteractive
    (
        . /etc/os-release
        cat << _EOF_ > mirror.txt
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME} main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-updates main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-backports main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-security main restricted universe multiverse

_EOF_
        mv /etc/apt/sources.list /etc/apt/sources.list.bak
        cat mirror.txt /etc/apt/sources.list.bak > /etc/apt/sources.list
    )

    # packages
    apt-get update
    apt-get install -y \
        build-essential \
        bwa \
        default-jre-headless \
        git \
        libbz2-dev \
        liblzma-dev \
        libtabixpp-dev \
        parallel \
        python \
        python3 \
        python3-pip \
        r-cran-cairo \
        r-cran-data.table \
        r-cran-ggplot2 \
        samtools \
        tabix \
        wget \
        zlib1g-dev

    # bbmap
    wget -O "bbmap.tar.gz" \
        https://sourceforge.net/projects/bbmap/files/BBMap_38.73.tar.gz
    mkdir bbmap
    tar -zxf bbmap.tar.gz \
        -C bbmap \
        --strip-components 1
    cp -r bbmap/resources/* /
    cp -r bbmap/* /usr/local/bin/
    rm -rf bbmap.tar.gz bbmap

    # vcflib
    git clone \
        https://github.com/vcflib/vcflib.git
    cd vcflib || exit 1
    git checkout tags/v1.0.1
    git submodule update --init --recursive
    make openmp
    cd .. || exit 1

    # freebayes
    git clone \
        https://github.com/ekg/freebayes.git
    cd freebayes || exit 1
    git checkout tags/v1.3.1
    git submodule update --init --recursive
    make

    # fix freebayes scripts
    sed \
        's/..\/vcflib\/scripts\/vcffirstheader/vcffirstheader/g' \
        scripts/freebayes-parallel \
        | sed \
        's/..\/vcflib\/bin\/vcfstreamsort/vcfstreamsort/g' \
        > scripts/freebayes-parallel.new
    rm scripts/freebayes-parallel
    mv scripts/freebayes-parallel.new scripts/freebayes-parallel
    chmod 755 scripts/freebayes-parallel
    cd .. || exit 1

    # vcftools
    mkdir vcftools
    wget \
        -O "vcftools.tar.gz" \
        --no-check-certificate \
        https://github.com/vcftools/vcftools/releases/download/v0.1.16/vcftools-0.1.16.tar.gz
    tar -zxf vcftools.tar.gz \
        -C vcftools \
        --strip-components 2

    cd vcftools || exit 1
    ./configure
    make 
    make install
    cd .. || exit 1
    rm -rf vcftools vcftools.tar.gz

    # install pipeline package
    /usr/bin/pip3 \
        install \
        git+git://github.com/tomharrop/honeybee-genotype-pipeline.git@v0.0.6
```

## Collection

 - Name: [TomHarrop/honeybee-genotype-pipeline](https://github.com/TomHarrop/honeybee-genotype-pipeline)
 - License: None

