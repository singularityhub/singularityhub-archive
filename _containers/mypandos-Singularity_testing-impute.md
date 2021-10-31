---
id: 4854
name: "mypandos/Singularity_testing"
branch: "master"
tag: "impute"
commit: "87af2528ae12d63d81feb610d4385887f7d682db"
version: "2d33e37347fac4293322eedad66d6b13"
build_date: "2018-09-18T03:28:18.935Z"
size_mb: 1025
size: 476839967
sif: "https://datasets.datalad.org/shub/mypandos/Singularity_testing/impute/2018-09-18-87af2528-2d33e373/2d33e37347fac4293322eedad66d6b13.simg"
url: https://datasets.datalad.org/shub/mypandos/Singularity_testing/impute/2018-09-18-87af2528-2d33e373/
recipe: https://datasets.datalad.org/shub/mypandos/Singularity_testing/impute/2018-09-18-87af2528-2d33e373/Singularity
collection: mypandos/Singularity_testing
---

# mypandos/Singularity_testing:impute

```bash
$ singularity pull shub://mypandos/Singularity_testing:impute
```

## Singularity Recipe

```singularity
#######################################################################
#
# This container provides an installation of tools needed for the chipimputation pipeline.
#
# Changelog
# ---------
#
#######################################################################

bootstrap: docker
From: ubuntu:16.04

%labels
    Mamana Mbiyavanga "mamana.mbiyavanga@uct.ac.za", Ayton Meintjes "ayton.meintjes@uct.ac.za"

%help
    This container provides an installation of tools needed for the chipimputation pipeline
    on https://github.com/h3abionet/chipimputation

%environment
    export PATH=/opt/miniconda2/bin:$PATH

%post
    # Install Basic tools
    apt-get update && apt-get install -y \
        autoconf \
        build-essential \
        git \
        libncurses5-dev \
        pkg-config \
        unzip \
        wget \
        zlib1g-dev &&
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

    # install anaconda
    if [ ! -d /opt/miniconda2 ]; then
         wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
         bash Miniconda2-latest-Linux-x86_64.sh -p /opt/miniconda2 -b
         rm -fr Miniconda2-latest-Linux-x86_64.sh
         export PATH=/opt/miniconda2/bin:$PATH
         conda update -n base conda
         conda config --add channels conda-forge
         conda config --add channels bioconda
    fi

    # Install IMPUTE2
    wget http://mathgen.stats.ox.ac.uk/impute/impute_v2.3.2_x86_64_static.tgz && \
        tar -zxvf impute_v2.3.2_x86_64_static.tgz && \
        mv impute_v2.3.2_x86_64_static/impute2 /usr/local/bin/impute2 && \
        mkdir /opt/impute2/example -p && \
        mv impute_v2.3.2_x86_64_static/Example/* /opt/impute2/example && \
        rm -rf impute_v2.3.2_x86_64_static impute_v2.3.2_x86_64_static.tgz

    # Install Eagle
    wget https://data.broadinstitute.org/alkesgroup/Eagle/downloads/Eagle_v2.4.tar.gz && \
        gunzip Eagle_v2.4.tar.gz && \
        tar xvf Eagle_v2.4.tar && \
        mv Eagle_v2.4/eagle /usr/local/bin/ && \
        rm -rf Eagle_v2.4

    conda install -y plink2 bcftools vcftools HTSlib

    conda clean --tarballs

%environment
    export LANG=en_US.UTF-8
    export LANGUAGE=en_US:en
    export LC_ALL=en_US.UTF-8
    export PATH=/opt/miniconda2/bin:$PATH
```

## Collection

 - Name: [mypandos/Singularity_testing](https://github.com/mypandos/Singularity_testing)
 - License: None

