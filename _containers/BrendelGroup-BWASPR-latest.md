---
id: 10328
name: "BrendelGroup/BWASPR"
branch: "master"
tag: "latest"
commit: "725db571e6f426c6651089ecc00a9e27fb02b57c"
version: "5537fafbf0d47ba240fd66a1557703fb"
build_date: "2021-03-08T17:55:51.157Z"
size_mb: 2283.0
size: 1005314079
sif: "https://datasets.datalad.org/shub/BrendelGroup/BWASPR/latest/2021-03-08-725db571-5537fafb/5537fafbf0d47ba240fd66a1557703fb.sif"
url: https://datasets.datalad.org/shub/BrendelGroup/BWASPR/latest/2021-03-08-725db571-5537fafb/
recipe: https://datasets.datalad.org/shub/BrendelGroup/BWASPR/latest/2021-03-08-725db571-5537fafb/Singularity
collection: BrendelGroup/BWASPR
---

# BrendelGroup/BWASPR:latest

```bash
$ singularity pull shub://BrendelGroup/BWASPR:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
From: ubuntu:20.04

%help
    This container is a companion to BWASP: Bisulfite-seq data Workflow Automation
    Software and Protocols from the Brendel Group, providing R packages and scripts
    for BWASP data analyses.
    Please see https://github.com/BrendelGroup/BWASPR for complete documentation.

%post
    export DEBIAN_FRONTEND=noninteractive
    apt -y update
    apt-get -y upgrade
    apt -y install bc bzip2 git tcsh tzdata unzip zip wget \
                   build-essential \
                   openjdk-11-jdk \
                   software-properties-common \
                   libcairo2-dev \
                   libcurl4-gnutls-dev \
                   libgd-dev \
                   libgd-graph-perl \
                   libmariadb-client-lgpl-dev-compat \
                   libpq-dev \
                   libssl-dev \
                   libtbb-dev \
                   libxml2-dev \
                   poppler-utils unoconv


    echo 'Installing R'
    #### 
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
    add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
    apt -y update
    apt -y install r-base
    R CMD javareconf

    echo 'Installing CRAN and Bioconductor packages'
    ######
    echo 'install.packages("BiocManager", repos="http://ftp.ussg.iu.edu/CRAN", dependencies=TRUE)'         > R2install
    echo 'install.packages("dplyr", repos="http://ftp.ussg.iu.edu/CRAN", dependencies=TRUE)'              >> R2install
    echo 'install.packages("gplots", repos="http://ftp.ussg.iu.edu/CRAN", dependencies=TRUE)'             >> R2install
    echo 'install.packages("gtable", repos="http://ftp.ussg.iu.edu/CRAN", dependencies=TRUE)'             >> R2install
    echo 'install.packages("gridExtra", repos="http://ftp.ussg.iu.edu/CRAN", dependencies=TRUE)'          >> R2install
    echo 'install.packages("gridExtra", repos="http://ftp.ussg.iu.edu/CRAN", dependencies=TRUE)'          >> R2install
    echo 'install.packages("pastecs", repos="http://ftp.ussg.iu.edu/CRAN", dependencies=TRUE)'            >> R2install
    echo 'install.packages("RCurl", repos="http://ftp.ussg.iu.edu/CRAN", dependencies=TRUE)'              >> R2install
    echo 'install.packages("rJava", repos="http://ftp.ussg.iu.edu/CRAN", dependencies=TRUE)'              >> R2install
    echo 'install.packages("sqldf", repos="http://ftp.ussg.iu.edu/CRAN", dependencies=TRUE)'              >> R2install
    echo 'install.packages("venneuler", repos="http://ftp.ussg.iu.edu/CRAN", dependencies=TRUE)'          >> R2install
    echo 'install.packages("XML", repos="http://ftp.ussg.iu.edu/CRAN", dependencies=TRUE)'                >> R2install
    echo 'install.packages("R.devices", repos="http://ftp.ussg.iu.edu/CRAN", dependencies=TRUE)'          >> R2install
    echo 'BiocManager::install(c("BiocGenerics", "GenomicRanges", "genomation","methylKit"), ask=FALSE)'  >> R2install

    Rscript R2install

    echo 'Installing BWASPR from https://github.com/BrendelGroup/BWASPR '
    ######
    cd /opt
    git clone https://github.com/BrendelGroup/BWASPR.git
    R CMD INSTALL BWASPR

    echo 'Installing unoconv from https://github.com/unoconv/unoconv/archive/0.9.0.tar.gz '
    ######
    cd /opt
    wget https://github.com/unoconv/unoconv/archive/0.9.0.tar.gz
    tar -xzf 0.9.0.tar.gz
    sed -e "s#/usr/bin/env python#/usr/bin/env python3#" unoconv-0.9.0/unoconv > /usr/bin/unoconv

    echo 'Installing rbo from https://github.com/dlukes/rbo '
    ######
    cd /opt
    git clone https://github.com/dlukes/rbo


%environment
    export LC_ALL=C
    export PATH=$PATH:/opt/BWASPR/bin

%labels
    Maintainer vpbrendel
    Version v1.1
```

## Collection

 - Name: [BrendelGroup/BWASPR](https://github.com/BrendelGroup/BWASPR)
 - License: None

