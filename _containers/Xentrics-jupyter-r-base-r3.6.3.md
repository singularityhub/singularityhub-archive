---
id: 13163
name: "Xentrics/jupyter-r-base"
branch: "master"
tag: "r3.6.3"
commit: "4e8cf6510fdbde534dfa18eff2b460924d49f5bf"
version: "2fbf6df6a09e95ce551fd8d57dd782f9cf760a13fcf821e47cd0bf710ca54dd1"
build_date: "2020-09-10T16:26:26.813Z"
size_mb: 258.546875
size: 271106048
sif: "https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/r3.6.3/2020-09-10-4e8cf651-2fbf6df6/2fbf6df6a09e95ce551fd8d57dd782f9cf760a13fcf821e47cd0bf710ca54dd1.sif"
url: https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/r3.6.3/2020-09-10-4e8cf651-2fbf6df6/
recipe: https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/r3.6.3/2020-09-10-4e8cf651-2fbf6df6/Singularity
collection: Xentrics/jupyter-r-base
---

# Xentrics/jupyter-r-base:r3.6.3

```bash
$ singularity pull shub://Xentrics/jupyter-r-base:r3.6.3
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%labels
    Maintainer Bastian Seelbinder
    R_Version 3.6.3

%apprun R
    exec R "${@}"

%apprun Rscript
    exec Rscript "${@}"

%runscript
    exec R "${@}"

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
        libxml2-dev \
        libssl-dev \
        libcurl4-openssl-dev \
	freeglut3-dev
    
    # Update locales
    DEBIAN_FRONTEND=noninteractive  apt-get install tzdata
    echo "LC_ALL=en_US.UTF-8" >> /etc/environment
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    echo "LANG=en_US.UTF-8" > /etc/locale.conf
    locale-gen en_US.UTF-8
    
    # Install R from CRAN repository
    echo 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/' >> /etc/apt/sources.list
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
    apt-get update
    apt-get -y install --no-install-recommends \
        r-base=${R_VERSION}* \
        r-base-core=${R_VERSION}* \
        r-base-dev=${R_VERSION}* \
        r-recommended=${R_VERSION}* \
        r-base-html=${R_VERSION}* \
        r-doc-html=${R_VERSION}*
    
    # cleanup
    apt-get clean
    rm -rf /var/lib/apt/lists/*

    echo "options(repos = c(CRAN = 'https://cloud.r-project.org/'), download.file.method = 'libcurl')" >> /usr/lib/R/etc/Rprofile.site
```

## Collection

 - Name: [Xentrics/jupyter-r-base](https://github.com/Xentrics/jupyter-r-base)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

