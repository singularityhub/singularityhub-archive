---
id: 10457
name: "rsettlage/singularity-r"
branch: "master"
tag: "latest"
commit: "291292aa8dabdd9b7498507695d74fed9b46dcd5"
version: "0ef07a8674053947931575429904e279"
build_date: "2019-11-14T14:23:21.900Z"
size_mb: 599.0
size: 234164255
sif: "https://datasets.datalad.org/shub/rsettlage/singularity-r/latest/2019-11-14-291292aa-0ef07a86/0ef07a8674053947931575429904e279.sif"
url: https://datasets.datalad.org/shub/rsettlage/singularity-r/latest/2019-11-14-291292aa-0ef07a86/
recipe: https://datasets.datalad.org/shub/rsettlage/singularity-r/latest/2019-11-14-291292aa-0ef07a86/Singularity
collection: rsettlage/singularity-r
---

# rsettlage/singularity-r:latest

```bash
$ singularity pull shub://rsettlage/singularity-r:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels
  Maintainer Robert Settlage
  R_Version 3.6.1

%apprun R
  exec R "${@}"

%apprun Rscript
  exec Rscript "${@}"

%runscript
  exec R "${@}"

%post
  # Software versions
  export R_VERSION=3.6.1

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

 - Name: [rsettlage/singularity-r](https://github.com/rsettlage/singularity-r)
 - License: [MIT License](https://api.github.com/licenses/mit)

