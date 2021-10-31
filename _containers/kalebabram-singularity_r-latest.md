---
id: 1536
name: "kalebabram/singularity_r"
branch: "master"
tag: "latest"
commit: "3f8bae4d428648e0945b3bc982c2c38e8028a409"
version: "4815b95f991e9c500722752018a9b633"
build_date: "2018-02-01T11:37:40.333Z"
size_mb: 590
size: 230719519
sif: "https://datasets.datalad.org/shub/kalebabram/singularity_r/latest/2018-02-01-3f8bae4d-4815b95f/4815b95f991e9c500722752018a9b633.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kalebabram/singularity_r/latest/2018-02-01-3f8bae4d-4815b95f/
recipe: https://datasets.datalad.org/shub/kalebabram/singularity_r/latest/2018-02-01-3f8bae4d-4815b95f/Singularity
collection: kalebabram/singularity_r
---

# kalebabram/singularity_r:latest

```bash
$ singularity pull shub://kalebabram/singularity_r:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels
  Maintainer Kaleb Abram 
  R_Version 3.4.3

%apprun R
  exec R "${@}"

%apprun Rscript
  exec Rscript "${@}"

%runscript
  exec R "${@}"

%post
  # Software versions
  export R_VERSION=3.4.3

  # Get dependencies
  apt-get update
  apt-get install -y --no-install-recommends \
    locales \
    wget \
    libmariadb-client-lgpl-dev

  # Configure default locale
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
  locale-gen en_US.utf8
  /usr/sbin/update-locale LANG=en_US.UTF-8
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8

  # Install R
  echo "deb http://cran.r-project.org/bin/linux/ubuntu xenial/" > /etc/apt/sources.list.d/r.list
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
  apt-get update
  apt-get install -y --no-install-recommends \
    r-base=${R_VERSION}* \
    r-base-dev=${R_VERSION}* \
    r-recommended=${R_VERSION}* \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \


  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [kalebabram/singularity_r](https://github.com/kalebabram/singularity_r)
 - License: None

