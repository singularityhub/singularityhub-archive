---
id: 10173
name: "mcw-rcc/r-base"
branch: "3.6.0"
tag: "3.6.0"
commit: "632c68009f7a3be71ef2bdbbfbea561fe15d5b66"
version: "f6cb75f2e2bf4cbd7f398249165fa30b"
build_date: "2020-10-20T19:36:47.401Z"
size_mb: 603
size: 237805599
sif: "https://datasets.datalad.org/shub/mcw-rcc/r-base/3.6.0/2020-10-20-632c6800-f6cb75f2/f6cb75f2e2bf4cbd7f398249165fa30b.simg"
url: https://datasets.datalad.org/shub/mcw-rcc/r-base/3.6.0/2020-10-20-632c6800-f6cb75f2/
recipe: https://datasets.datalad.org/shub/mcw-rcc/r-base/3.6.0/2020-10-20-632c6800-f6cb75f2/Singularity
collection: mcw-rcc/r-base
---

# mcw-rcc/r-base:3.6.0

```bash
$ singularity pull shub://mcw-rcc/r-base:3.6.0
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
    exec R "${@}"

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

