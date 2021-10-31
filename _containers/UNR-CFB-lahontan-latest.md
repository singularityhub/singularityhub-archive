---
id: 1238
name: "UNR-CFB/lahontan"
branch: "master"
tag: "latest"
commit: "eb0abdec585da93a12de8615fb216d838c2d5ddc"
version: "108af69556c7ebff0047c9eb9757b4c0"
build_date: "2018-01-10T06:32:43.264Z"
size_mb: 6102
size: 3810979871
sif: "https://datasets.datalad.org/shub/UNR-CFB/lahontan/latest/2018-01-10-eb0abdec-108af695/108af69556c7ebff0047c9eb9757b4c0.simg"
url: https://datasets.datalad.org/shub/UNR-CFB/lahontan/latest/2018-01-10-eb0abdec-108af695/
recipe: https://datasets.datalad.org/shub/UNR-CFB/lahontan/latest/2018-01-10-eb0abdec-108af695/Singularity
collection: UNR-CFB/lahontan
---

# UNR-CFB/lahontan:latest

```bash
$ singularity pull shub://UNR-CFB/lahontan:latest
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

###############################################################
# Command used to build:
# sudo singularity build lahontan.simg Singularity
###############################################################

%labels
    MAINTAINER Alberto Nava
    VERSION v1.0

%post
    locale-gen en_US.UTF-8

    echo "Installing necessary packages..."
    echo "deb http://us.archive.ubuntu.com/ubuntu/ xenial universe" >> /etc/apt/sources.list
    apt-get update && apt-get install --yes git cmake gcc g++ libncurses-dev libhdf5-cpp-11 libhdf5-dev python3-docopt vim unzip openjdk-8-jdk-headless wget gfortran libbz2-dev liblzma-dev libpcre++-dev libcurl4-openssl-dev libssl-dev pandoc texlive-latex-extra libxml2-dev libmariadb-client-lgpl-dev libreadline6-dev libreadline6 libtbb-dev bzip2

    cd /opt
    wget https://cran.r-project.org/src/base/R-3/R-3.4.3.tar.gz
    tar xzf R-3.4.3.tar.gz
    cd R-3.4.3
    ./configure --with-x=no 
    make && make install
    R -e 'source("https://bioconductor.org/biocLite.R");biocLite(ask=FALSE);biocLite(c("devtools","DESeq2","edgeR","ReportingTools","regionReport","pachterlab/sleuth","ballgown","DT","pheatmap"));devtools::install_github(c("docopt/docopt.R","alyssafrazee/RSkittleBrewer"))'
    
    echo "Cloning repository..."
    git clone --recursive https://github.com/UNR-CFB/lahontan.git /lahontan

    echo "Installing pipeline..."
    cd /lahontan
    echo 'export RNASEQDIR=/lahontan/bin' >> $SINGULARITY_ENVIRONMENT
    /lahontan/lib/autoSetup.sh

    ln -s /usr/local/bin/R /lahontan/bin/R
    ln -s /usr/local/bin/Rscript /lahontan/bin/Rscript

%environment
    RNASEQDIR=/lahontan/bin
    PATH="${PATH}:/lahontan/bin:/lahontan/lib"
    LANG=en_US.UTF-8
    LANGUAGE=en_US
    export RNASEQDIR PATH LANG LANGUAGE

%help
    Go to https://github.com/UNR-CFB/lahontan for more help OR try "./lahontan.simg -h" for pipeline help

%runscript
    exec /lahontan/lib/lahontan "$@"
```

## Collection

 - Name: [UNR-CFB/lahontan](https://github.com/UNR-CFB/lahontan)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

