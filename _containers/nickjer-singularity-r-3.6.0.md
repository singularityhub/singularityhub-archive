---
id: 8718
name: "nickjer/singularity-r"
branch: "master"
tag: "3.6.0"
commit: "dc2ed699e49e55a8238ae2e9912cc236089cd1bd"
version: "e05be5b9bda5319247e1cfe866b9f9b8"
build_date: "2021-04-15T13:28:42.051Z"
size_mb: 595
size: 232787999
sif: "https://datasets.datalad.org/shub/nickjer/singularity-r/3.6.0/2021-04-15-dc2ed699-e05be5b9/e05be5b9bda5319247e1cfe866b9f9b8.simg"
url: https://datasets.datalad.org/shub/nickjer/singularity-r/3.6.0/2021-04-15-dc2ed699-e05be5b9/
recipe: https://datasets.datalad.org/shub/nickjer/singularity-r/3.6.0/2021-04-15-dc2ed699-e05be5b9/Singularity
collection: nickjer/singularity-r
---

# nickjer/singularity-r:3.6.0

```bash
$ singularity pull shub://nickjer/singularity-r:3.6.0
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels
  Maintainer Jeremy Nicklas
  R_Version 3.6.0

%apprun R
  exec R "${@}"

%apprun Rscript
  exec Rscript "${@}"

%runscript
  exec R "${@}"

%post
  # Software versions
  export R_VERSION=3.6.0

  # Get dependencies
  apt-get update
  apt-get install -y --no-install-recommends \
    locales

  # Configure default locale
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
  locale-gen en_US.utf8
  /usr/sbin/update-locale LANG=en_US.UTF-8
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8

  # Install R
  echo "deb http://cran.r-project.org/bin/linux/ubuntu xenial-cran35/" > /etc/apt/sources.list.d/r.list
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
  apt-get update
  apt-get install -y --no-install-recommends \
    r-base=${R_VERSION}* \
    r-base-core=${R_VERSION}* \
    r-base-dev=${R_VERSION}* \
    r-recommended=${R_VERSION}* \
    r-base-html=${R_VERSION}* \
    r-doc-html=${R_VERSION}* \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    libcairo2-dev \
    libxt-dev \

  # Add a default CRAN mirror
  echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'), download.file.method = 'libcurl')" >> /usr/lib/R/etc/Rprofile.site

  # Add a directory for host R libraries
  mkdir -p /library
  echo "R_LIBS_SITE=/library:\${R_LIBS_SITE}" >> /usr/lib/R/etc/Renviron.site

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [nickjer/singularity-r](https://github.com/nickjer/singularity-r)
 - License: [MIT License](https://api.github.com/licenses/mit)

