---
id: 9070
name: "meekrob/RSummit_container"
branch: "master"
tag: "latest"
commit: "264aaa9281f85f008f9c4df3c09e9c99e6521491"
version: "680a4093b4faec146335d2f0f451fd95"
build_date: "2020-05-16T20:09:26.213Z"
size_mb: 3501.0
size: 1500577823
sif: "https://datasets.datalad.org/shub/meekrob/RSummit_container/latest/2020-05-16-264aaa92-680a4093/680a4093b4faec146335d2f0f451fd95.sif"
url: https://datasets.datalad.org/shub/meekrob/RSummit_container/latest/2020-05-16-264aaa92-680a4093/
recipe: https://datasets.datalad.org/shub/meekrob/RSummit_container/latest/2020-05-16-264aaa92-680a4093/Singularity
collection: meekrob/RSummit_container
---

# meekrob/RSummit_container:latest

```bash
$ singularity pull shub://meekrob/RSummit_container:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%post

    # install some system deps
    apt-get -y update
    apt-get -y install locales curl bzip2 less unzip git wget vim ant default-jdk
    # this is a X11 dep 
    apt-get -y install libxext6
    # tools to open PDF and HTML files
    apt-get -y install firefox xpdf
    # some extra devel libs
    apt-get -y install zlib1g-dev libssl-dev libpng-dev uuid-dev
    # other
    locale-gen en_US.UTF-8
    apt-get clean

    # download and install miniconda3
    curl -sSL -O https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh -p /opt/miniconda3 -b
    rm -fr Miniconda3-latest-Linux-x86_64.sh
    export PATH=/opt/miniconda3/bin:$PATH
    conda update -n base conda
    conda config --add channels conda-forge
    conda config --add channels bioconda

    # install the R programming language
    conda install --yes -c conda-forge r-base==3.5.1

    # install some dependencies to build R packages
    apt-get -y install build-essential gfortran

    # install R bioconductor including DESeq2
    Rscript -e "install.packages('BiocManager', repos='https://cran.rstudio.com'); BiocManager::install('ggtree')"
    Rscript -e "source ('https://bioconductor.org/biocLite.R'); biocLite(c('ape', 'pegas', 'adegenet', 'ChIPpeakAnno','phangorn', 'sqldf', 'ggplot2', 'ggExtra', 'phytools', 'DESeq2','monocle', 'edgeR','ShortRead','rtracklayer','GenomicFeatures','Rsamtools','biomaRt','Repitools','QuasR'))"

    # install fastp
    wget http://opengene.org/fastp/fastp -P /opt/bin/
    chmod a+x /opt/bin/fastp
    export PATH="/opt/bin:$PATH"

%environment
    export LANG=en_US.UTF-8
    export LANGUAGE=en_US:en
    export LC_ALL=en_US.UTF-8
    export XDG_RUNTIME_DIR=""
    export PATH=/opt/miniconda3/bin:$PATH
    export PATH=/opt/bin/fastp:$PATH
```

## Collection

 - Name: [meekrob/RSummit_container](https://github.com/meekrob/RSummit_container)
 - License: None

