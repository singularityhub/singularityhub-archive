---
id: 13192
name: "Xentrics/jupyter-r-base"
branch: "master"
tag: "r3.6.3_banocc"
commit: "5cfce8763ea4021f913f70d941d0da28b41bbb86"
version: "f7592d2222f0f29fd7b5eec0049f59dcc9694a69501632660f004ba1e22f7fe2"
build_date: "2020-09-09T12:52:53.631Z"
size_mb: 367.21484375
size: 385052672
sif: "https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/r3.6.3_banocc/2020-09-09-5cfce876-f7592d22/f7592d2222f0f29fd7b5eec0049f59dcc9694a69501632660f004ba1e22f7fe2.sif"
url: https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/r3.6.3_banocc/2020-09-09-5cfce876-f7592d22/
recipe: https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/r3.6.3_banocc/2020-09-09-5cfce876-f7592d22/Singularity
collection: Xentrics/jupyter-r-base
---

# Xentrics/jupyter-r-base:r3.6.3_banocc

```bash
$ singularity pull shub://Xentrics/jupyter-r-base:r3.6.3_banocc
```

## Singularity Recipe

```singularity
BootStrap: shub
From: Xentrics/jupyter-r-base:r3.6.3

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
        libopenblas-dev r-base-core libfontconfig1-dev libcairo2-dev \
	openssh-client openssh-server libssh-dev wget vim git gfortran autoconf pandoc qpdf libssh2-1-dev
    
    # Update locales
    DEBIAN_FRONTEND=noninteractive  apt-get install tzdata
    echo "LC_ALL=en_US.UTF-8" >> /etc/environment
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    echo "LANG=en_US.UTF-8" > /etc/locale.conf
    locale-gen en_US.UTF-8
    
    # to solve the "locale.Error: unsupported locale setting" error [https://stackoverflow.com/questions/14547631/python-locale-error-unsupported-locale-setting ]
    export LC_ALL=C
    
    # cleanup
    apt-get clean
    rm -rf /var/lib/apt/lists/*

    echo "options(repos = c(CRAN = 'https://cloud.r-project.org/'), download.file.method = 'libcurl')" >> /usr/lib/R/etc/Rprofile.site

    # Install BanoCC
    export R_LIBS_USER="/usr/local/lib/R/site-library" # make sure packages go here
    R --vanilla -e 'install.packages("BiocManager", repos="https://cloud.r-project.org")'
    R --vanilla -e 'BiocManager::install(c("tidyverse", "magrittr", "readxl", "writexl"))'
```

## Collection

 - Name: [Xentrics/jupyter-r-base](https://github.com/Xentrics/jupyter-r-base)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

