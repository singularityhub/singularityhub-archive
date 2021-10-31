---
id: 4877
name: "mcw-rcc/r-base"
branch: "3.5.1"
tag: "3.5.1"
commit: "796e2a96229fd0ded5aacb5c2eb62d27ac321a12"
version: "aa775918e99af2e91b67a103d6021715"
build_date: "2021-02-26T05:52:14.961Z"
size_mb: 2086
size: 845152287
sif: "https://datasets.datalad.org/shub/mcw-rcc/r-base/3.5.1/2021-02-26-796e2a96-aa775918/aa775918e99af2e91b67a103d6021715.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mcw-rcc/r-base/3.5.1/2021-02-26-796e2a96-aa775918/
recipe: https://datasets.datalad.org/shub/mcw-rcc/r-base/3.5.1/2021-02-26-796e2a96-aa775918/Singularity
collection: mcw-rcc/r-base
---

# mcw-rcc/r-base:3.5.1

```bash
$ singularity pull shub://mcw-rcc/r-base:3.5.1
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%help
    This container runs R.

%labels
    Maintainer Matthew Flister
    Version 09.18.18
    R_Version 3.5.1

%apprun R
    exec R "${@}"

%apprun Rscript
    exec Rscript "${@}"

%runscript
    exec R "${@}"

%environment 
    export R_LIBS=/usr/local/lib/R/library:/extR/library1:/extR/library2

%post
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts /extR/library1 /extR/library2
    apt-get update
    apt-get -y install \
        wget \
        build-essential \
        software-properties-common \
        apt-transport-https \
        locales
    echo "LC_ALL=en_US.UTF-8" >> /etc/environment
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    echo "LANG=en_US.UTF-8" > /etc/locale.conf
    locale-gen en_US.UTF-8
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
    add-apt-repository 'deb https://cran.mtu.edu/bin/linux/ubuntu xenial/'
    apt-get update &&\
    apt-get -y build-dep r-base 
    apt-get clean

    export R_VERSION=3.5.1
    export R_URL=https://cran.r-project.org/src/base/R-3/R-${R_VERSION}.tar.gz
    wget $R_URL
    tar -xvf R-${R_VERSION}.tar.gz
    cd R-${R_VERSION}
    ./configure --enable-R-shlib --with-blas --with-lapack
    make && make install
    cd .. && rm -rf R-${R_VERSION}*
```

## Collection

 - Name: [mcw-rcc/r-base](https://github.com/mcw-rcc/r-base)
 - License: [MIT License](https://api.github.com/licenses/mit)

