---
id: 13161
name: "Xentrics/jupyter-r-base"
branch: "master"
tag: "r4"
commit: "afc4c67a51eba3a131ca629e705f9801cec002b5"
version: "8b7652d99f7e3b31687fd2a52b3d7960f908ff6b4491eee5f1bd5fe7816df9b5"
build_date: "2020-09-09T12:52:30.086Z"
size_mb: 1195.23046875
size: 1253289984
sif: "https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/r4/2020-09-09-afc4c67a-8b7652d9/8b7652d99f7e3b31687fd2a52b3d7960f908ff6b4491eee5f1bd5fe7816df9b5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/Xentrics/jupyter-r-base/r4/2020-09-09-afc4c67a-8b7652d9/
recipe: https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/r4/2020-09-09-afc4c67a-8b7652d9/Singularity
collection: Xentrics/jupyter-r-base
---

# Xentrics/jupyter-r-base:r4

```bash
$ singularity pull shub://Xentrics/jupyter-r-base:r4
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%labels
    Maintainer Bastian Seelbinder
    R_Version 4

%apprun R
    exec R "${@}"

%apprun Rscript
    exec Rscript "${@}"

%runscript
    exec R "${@}"

%environment
    export LC_ALL=C

%post
    # set mount points
    mkdir -p /scratch/global /scratch/local
    
    # Install dependencies
    apt-get update
    apt-get -y install \
        wget \
        build-essential \
        software-properties-common \
        apt-transport-https \
        locales \
        libpcre2-dev \
        pcre2-utils \
        libxml2-dev \
        libssl-dev \
        libcurl4-openssl-dev \
        libgtk3-nocsd0 \
        gtk3-nocsd
    
    # Update locales
    DEBIAN_FRONTEND=noninteractive  apt-get install tzdata
    echo "LC_ALL=en_US.UTF-8" >> /etc/environment
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    echo "LANG=en_US.UTF-8" > /etc/locale.conf
    locale-gen en_US.UTF-8
    
    # Install R from CRAN repository
    #echo 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/' >> /etc/apt/sources.list
    #apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
    #gpg --keyserver keyserver.ubuntu.com --recv-key E298A3A825C0D65DFD57CBB651716619E084DAB9
    #gpg -a --export E298A3A825C0D65DFD57CBB651716619E084DAB9 | sudo apt-key add -
    sed -i~orig -e 's/# deb-src/deb-src/' /etc/apt/sources.list   
    apt-get update
    
    # Install R devel
    apt-get build-dep -y r-base
    wget https://stat.ethz.ch/R/daily/R-devel.tar.gz && tar -xzvf R-devel.tar.gz
    rm R-devel.tar.gz
    cd R-devel
    ./configure --enable-R-shlib
    make
    make check
    make install
    
    # cleanup    
    apt-get clean
    rm -rf /var/lib/apt/lists/*

    mkdir -p /usr/lib/R/etc/
    echo "options(repos = c(CRAN = 'https://cloud.r-project.org/'), download.file.method = 'libcurl')" >> /usr/lib/R/etc/Rprofile.site
```

## Collection

 - Name: [Xentrics/jupyter-r-base](https://github.com/Xentrics/jupyter-r-base)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

