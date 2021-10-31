---
id: 6033
name: "mypandos/exome_analysis"
branch: "master"
tag: "latest"
commit: "36ba0a72f312e009c87d5393edde5944ac4546be"
version: "b6667196b1afad9cf5e23a81351c4ab5"
build_date: "2019-02-26T11:50:35.147Z"
size_mb: 954
size: 388050975
sif: "https://datasets.datalad.org/shub/mypandos/exome_analysis/latest/2019-02-26-36ba0a72-b6667196/b6667196b1afad9cf5e23a81351c4ab5.simg"
url: https://datasets.datalad.org/shub/mypandos/exome_analysis/latest/2019-02-26-36ba0a72-b6667196/
recipe: https://datasets.datalad.org/shub/mypandos/exome_analysis/latest/2019-02-26-36ba0a72-b6667196/Singularity
collection: mypandos/exome_analysis
---

# mypandos/exome_analysis:latest

```bash
$ singularity pull shub://mypandos/exome_analysis:latest
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
    apt-get update && apt-get install -y \
        autoconf \
        build-essential \
        git \
        libncurses5-dev \
        pkg-config \
        unzip \
        wget curl \
        python python-dev \
        libbz2-dev \
        liblzma-dev \
        zlib1g-dev \
        r-base && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

    wget --quiet https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc
#
#     # conda install -y -c bioconda vcftools bcftools htslib samtools plink2
#
#     # install R packages
# #    R --slave -e 'install.packages("dplyr", repos="https://cloud.r-project.org/")'
# #    R --slave -e 'install.packages("ggplot2", repos="https://cloud.r-project.org/")'
# #    R --slave -e 'install.packages("data.table", repos="https://cloud.r-project.org/")'
# #    R --slave -e 'install.packages("sm", repos="https://cloud.r-project.org/")'
#
#     # Install minimac4
#     wget http://debian.mirror.ac.za/debian/pool/main/libs/libstatgen/libstatgen0_1.0.14-2_amd64.deb
#     dpkg -i libstatgen0_1.0.14-2_amd64.deb
#     wget http://debian.mirror.ac.za/debian/pool/main/m/minimac4/minimac4_1.0.0-2_amd64.deb
#     dpkg -i minimac4_1.0.0-2_amd64.deb
#
#     # Install PLINK2
#     # there is an undocumented stable url (without the date)
# #    wget http://www.cog-genomics.org/static/bin/plink/plink_linux_x86_64.zip -O plink.zip && \
# #        unzip plink.zip -d /usr/local/bin/ && \
# #        rm -f plink.zip
# #
# #    # Install bcftools
# #    wget https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2 && \
# #    tar -xvf bcftools-1.9.tar.bz2 && \
# #    cd bcftools-1.9 && \
# #    ./configure --prefix=/usr/local && \
# #    make && \
# #    make install && \
# #    cd .. && rm -rf bcftools-1.9*
# #
# #    # Install htslib
# #    wget https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2 && \
# #    tar -xvf htslib-1.9.tar.bz2 && \
# #    cd htslib-1.9 && \
# #    ./configure --prefix=/usr/local && \
# #    make && \
# #    make install && \
# #    cd .. && rm -rf htslib-1.9*
# #
# #    # Install samtools
# #    wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 && \
# #    tar -xvf samtools-1.9.tar.bz2 && \
# #    cd samtools-1.9 && \
# #    ./configure --prefix=/usr/local && \
# #    make && \
# #    make install && \
# #    cd .. && rm -rf samtools-1.9*
# #
# #    # Install Eagle
#     eagle="Eagle_v2.4_1"
#     wget https://data.broadinstitute.org/alkesgroup/Eagle/downloads/${eagle}.tar.gz && \
#         gunzip ${eagle}.tar.gz && \
#         tar xvf ${eagle}.tar && \
#         mv ${eagle}/eagle /usr/local/bin/ && \
#         rm -rf ${eagle}

%environment
    export LANG=en_US.UTF-8
    export LANGUAGE=en_US:en
    export LC_ALL=C.UTF-8
```

## Collection

 - Name: [mypandos/exome_analysis](https://github.com/mypandos/exome_analysis)
 - License: None

