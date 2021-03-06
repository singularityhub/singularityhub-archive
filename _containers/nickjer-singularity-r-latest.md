---
id: 1360
name: "nickjer/singularity-r"
branch: "master"
tag: "latest"
commit: "293552151ec669928896871af79f596648abf568"
version: "2528af32d7ead298d4350dedb6b3ed3d"
build_date: "2021-04-19T19:38:57.390Z"
size_mb: 602.0
size: 237121567
sif: "https://datasets.datalad.org/shub/nickjer/singularity-r/latest/2021-04-19-29355215-2528af32/2528af32d7ead298d4350dedb6b3ed3d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/nickjer/singularity-r/latest/2021-04-19-29355215-2528af32/
recipe: https://datasets.datalad.org/shub/nickjer/singularity-r/latest/2021-04-19-29355215-2528af32/Singularity
collection: nickjer/singularity-r
---

# nickjer/singularity-r:latest

```bash
$ singularity pull shub://nickjer/singularity-r:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels
  Maintainer Jeremy Nicklas
  R_Version 3.6.2

%apprun R
  exec R "${@}"

%apprun Rscript
  exec Rscript "${@}"

%runscript
  exec R "${@}"

%post
  # Software versions
  export R_VERSION=3.6.2

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
  apt-get install -y --no-install-recommends --allow-unauthenticated \
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

