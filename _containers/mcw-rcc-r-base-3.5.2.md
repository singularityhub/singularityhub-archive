---
id: 6277
name: "mcw-rcc/r-base"
branch: "3.5.2"
tag: "3.5.2"
commit: "56cdec0f967c1cf9a0c756ed993aea36fcf8e3eb"
version: "fe088eecc141ebfa11fe2b2d5d11db93"
build_date: "2019-01-23T18:33:54.756Z"
size_mb: 603
size: 237314079
sif: "https://datasets.datalad.org/shub/mcw-rcc/r-base/3.5.2/2019-01-23-56cdec0f-fe088eec/fe088eecc141ebfa11fe2b2d5d11db93.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mcw-rcc/r-base/3.5.2/2019-01-23-56cdec0f-fe088eec/
recipe: https://datasets.datalad.org/shub/mcw-rcc/r-base/3.5.2/2019-01-23-56cdec0f-fe088eec/Singularity
collection: mcw-rcc/r-base
---

# mcw-rcc/r-base:3.5.2

```bash
$ singularity pull shub://mcw-rcc/r-base:3.5.2
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%help
    This container runs R.

%labels
    Maintainer Matthew Flister
    R_Version 3.5.2

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
    echo 'deb https://cloud.r-project.org/bin/linux/ubuntu xenial-cran35/' >> /etc/apt/sources.list
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
    apt-get update 
    apt-get -y install --no-install-recommends \
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

 - Name: [mcw-rcc/r-base](https://github.com/mcw-rcc/r-base)
 - License: [MIT License](https://api.github.com/licenses/mit)

