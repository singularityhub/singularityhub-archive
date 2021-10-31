---
id: 10167
name: "jiayiliujiayi/R3.6sig"
branch: "master"
tag: "r"
commit: "23cbb9e6f45782cbca4171bf34e5e42ebeee51ba"
version: "976cf38d48e5e851eca25d66287b1948"
build_date: "2019-07-02T23:19:22.495Z"
size_mb: 595
size: 232779807
sif: "https://datasets.datalad.org/shub/jiayiliujiayi/R3.6sig/r/2019-07-02-23cbb9e6-976cf38d/976cf38d48e5e851eca25d66287b1948.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jiayiliujiayi/R3.6sig/r/2019-07-02-23cbb9e6-976cf38d/
recipe: https://datasets.datalad.org/shub/jiayiliujiayi/R3.6sig/r/2019-07-02-23cbb9e6-976cf38d/Singularity
collection: jiayiliujiayi/R3.6sig
---

# jiayiliujiayi/R3.6sig:r

```bash
$ singularity pull shub://jiayiliujiayi/R3.6sig:r
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

 - Name: [jiayiliujiayi/R3.6sig](https://github.com/jiayiliujiayi/R3.6sig)
 - License: None

