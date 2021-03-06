---
id: 13196
name: "churchill-lab/scRATE"
branch: "master"
tag: "latest"
commit: "e31c6d76a12098e5a3f9573d5761f16d8013dec9"
version: "ddb9e1af8de277699f172145b40b59b7"
build_date: "2020-08-10T06:23:45.368Z"
size_mb: 1112.0
size: 395677727
sif: "https://datasets.datalad.org/shub/churchill-lab/scRATE/latest/2020-08-10-e31c6d76-ddb9e1af/ddb9e1af8de277699f172145b40b59b7.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/churchill-lab/scRATE/latest/2020-08-10-e31c6d76-ddb9e1af/
recipe: https://datasets.datalad.org/shub/churchill-lab/scRATE/latest/2020-08-10-e31c6d76-ddb9e1af/Singularity
collection: churchill-lab/scRATE
---

# churchill-lab/scRATE:latest

```bash
$ singularity pull shub://churchill-lab/scRATE:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%help
    This container runs R.

%labels
    Maintainer Kwangbom (KB) Choi, Ph.D.

%apprun R
    exec R "${@}"

%apprun Rscript
    exec Rscript "${@}"

%runscript
    exec R "${@}"

%post
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts /extR/library1 /extR/library2
    apt-get update
    apt-get -y install \
        wget \
        build-essential \
        software-properties-common \
        apt-transport-https \
        locales \
        libv8-dev \
        libhdf5-serial-dev
    echo "LC_ALL=en_US.UTF-8" >> /etc/environment
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    echo "LANG=en_US.UTF-8" > /etc/locale.conf
    locale-gen en_US.UTF-8
    echo 'deb https://cloud.r-project.org/bin/linux/ubuntu xenial-cran35/' >> /etc/apt/sources.list
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 51716619E084DAB9
    add-apt-repository -y "ppa:marutter/rrutter3.5"
    add-apt-repository -y "ppa:marutter/c2d4u3.5"
    apt-get update
    apt-get -y install --no-install-recommends --allow-unauthenticated\
        r-base \
        r-base-core \
        r-base-dev \
        r-recommended \
        r-base-html \
        r-doc-html \
        r-cran-devtools \
        r-cran-rcpp \
        r-cran-rcppparallel \
        r-cran-bh
    apt-get clean

    mkdir -p $HOME/.R/
    echo "CXX14FLAGS=-O3 -march=native -mtune=native -fPIC\n" >> $HOME/.R/Makevars

    Rscript -e "install.packages('rstan')"
    Rscript -e "install.packages('rstanarm')"
    Rscript -e "install.packages('brms')"
    Rscript -e "install.packages('hdf5r')"
    Rscript -e "devtools::install_github('mojaveazure/loomR', ref='develop')"
    Rscript -e "devtools::install_github('churchill-lab/scRATE', dep=FALSE, build_vignettes=TRUE)"

    rm -rf /var/lib/apt/lists/*

    echo "options(repos = c(CRAN = 'https://cloud.r-project.org/'), download.file.method = 'libcurl')" >> /usr/lib/R/etc/Rprofile.site
```

## Collection

 - Name: [churchill-lab/scRATE](https://github.com/churchill-lab/scRATE)
 - License: None

