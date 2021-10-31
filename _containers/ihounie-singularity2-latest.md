---
id: 12784
name: "ihounie/singularity2"
branch: "master"
tag: "latest"
commit: "81846fd231187c8f23eb897cd6fbd69c68a05fd3"
version: "3cac7d80423dcd89e8b27826b524306e"
build_date: "2020-04-23T17:31:48.672Z"
size_mb: 610.0
size: 242327583
sif: "https://datasets.datalad.org/shub/ihounie/singularity2/latest/2020-04-23-81846fd2-3cac7d80/3cac7d80423dcd89e8b27826b524306e.sif"
url: https://datasets.datalad.org/shub/ihounie/singularity2/latest/2020-04-23-81846fd2-3cac7d80/
recipe: https://datasets.datalad.org/shub/ihounie/singularity2/latest/2020-04-23-81846fd2-3cac7d80/Singularity
collection: ihounie/singularity2
---

# ihounie/singularity2:latest

```bash
$ singularity pull shub://ihounie/singularity2:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%help
    This container runs R.

%labels
    Maintainer Matthew Flister
    R_Version 3.6.0

%apprun R
    exec R "${@}"

%apprun Rscript
    exec Rscript "${@}"

%runscript
    exec Rscript "${@}"

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
    echo 'deb https://cloud.r-project.org/bin/linux/ubuntu xenial-cran35/' >> /etc/apt/sources.list
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
    apt-get update
    apt-get -y install --allow-unauthenticated --no-install-recommends \
        r-base=${R_VERSION}* \
        r-base-core=${R_VERSION}* \
        r-base-dev=${R_VERSION}* \
        r-recommended=${R_VERSION}* \
        r-base-html=${R_VERSION}* \
        r-doc-html=${R_VERSION}*
    apt-get clean
    rm -rf /var/lib/apt/lists/*

    echo "options(repos = c(CRAN = 'https://cloud.r-project.org/'), download.file.method = 'libcurl')" >> /usr/lib/R/etc/Rprofile.site
```

## Collection

 - Name: [ihounie/singularity2](https://github.com/ihounie/singularity2)
 - License: None

