---
id: 6054
name: "nickjer/singularity-r"
branch: "master"
tag: "3.5.2"
commit: "2b5eac6a651dc09f7abfd03d1bfc4ced8fb6b903"
version: "3c60214ffe6b9951719c117916771366"
build_date: "2020-08-03T17:56:17.863Z"
size_mb: 594
size: 232054815
sif: "https://datasets.datalad.org/shub/nickjer/singularity-r/3.5.2/2020-08-03-2b5eac6a-3c60214f/3c60214ffe6b9951719c117916771366.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/nickjer/singularity-r/3.5.2/2020-08-03-2b5eac6a-3c60214f/
recipe: https://datasets.datalad.org/shub/nickjer/singularity-r/3.5.2/2020-08-03-2b5eac6a-3c60214f/Singularity
collection: nickjer/singularity-r
---

# nickjer/singularity-r:3.5.2

```bash
$ singularity pull shub://nickjer/singularity-r:3.5.2
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels
  Maintainer Jeremy Nicklas
  R_Version 3.5.2

%apprun R
  exec R "${@}"

%apprun Rscript
  exec Rscript "${@}"

%runscript
  exec R "${@}"

%post
  # Software versions
  export R_VERSION=3.5.2

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

