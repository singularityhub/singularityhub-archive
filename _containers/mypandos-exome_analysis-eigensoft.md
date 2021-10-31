---
id: 10158
name: "mypandos/exome_analysis"
branch: "master"
tag: "eigensoft"
commit: "1826868fc7ffabe95c258656162feb6eaa52eef9"
version: "5e4215f2f2c5ffa99b9d220144921e51"
build_date: "2019-07-02T13:32:14.878Z"
size_mb: 2071
size: 854798367
sif: "https://datasets.datalad.org/shub/mypandos/exome_analysis/eigensoft/2019-07-02-1826868f-5e4215f2/5e4215f2f2c5ffa99b9d220144921e51.simg"
url: https://datasets.datalad.org/shub/mypandos/exome_analysis/eigensoft/2019-07-02-1826868f-5e4215f2/
recipe: https://datasets.datalad.org/shub/mypandos/exome_analysis/eigensoft/2019-07-02-1826868f-5e4215f2/Singularity
collection: mypandos/exome_analysis
---

# mypandos/exome_analysis:eigensoft

```bash
$ singularity pull shub://mypandos/exome_analysis:eigensoft
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

%runscript
    echo "This is what happens when you run the container..."
    export PATH=/opt/conda/bin:${PATH}
    /bin/bash

%post
    # Install Basic tools
    apt-get update \
    && apt-get install -y --no-install-recommends \
         make \
         git \
         ca-certificates \
         gcc \
         wget \
         build-essential \
         gfortran \
         libgsl0-dev \
         libopenblas-base \
         libopenblas-dev \
         liblapacke-dev \
         libfontconfig1 \
         libxi6 \
         libxrender1 \
         libxext6 \
         libbz2-dev \
         liblzma-dev \
         zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*


    # Compile EIG
    git clone --depth 1 --branch master https://github.com/DReichLab/EIG /tmp/EIG
    cd /tmp/EIG/src
    make clobber OPENBLAS=/opt/openblas LDLIBS="-llapacke"\
    && make install OPENBLAS=/opt/openblas LDLIBS="-llapacke" \
    && mv ../bin/* /usr/local/bin

    # Install Eagle
    eagle="Eagle_v2.4.1"
    wget https://data.broadinstitute.org/alkesgroup/Eagle/downloads/${eagle}.tar.gz && \
        gunzip ${eagle}.tar.gz && \
        tar xvf ${eagle}.tar && \
        mv ${eagle}/eagle /usr/local/bin/ && \
        rm -rf ${eagle}

    # Install conda
    wget --quiet https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/miniconda2 && \
    rm ~/miniconda.sh && \

    # use conda to install some bioinfo tools
    export PATH=/opt/miniconda2/bin:$PATH
    conda config --add channels bioconda
    conda config --add channels r
    conda install -y vcftools bcftools htslib samtools plink2 snpeff snpsift r-base=3.4.1 r-ggplot2 r-dplyr r-reshape2 r-cairo

    # Tidy up
    rm -rf /tmp/*


%environment
    export LANG=en_US.UTF-8
    export LANGUAGE=en_US:en
    export LC_ALL=C.UTF-8
    export PATH="/opt/miniconda2/bin:$PATH"
```

## Collection

 - Name: [mypandos/exome_analysis](https://github.com/mypandos/exome_analysis)
 - License: None

