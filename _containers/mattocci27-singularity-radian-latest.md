---
id: 13446
name: "mattocci27/singularity-radian"
branch: "master"
tag: "latest"
commit: "0e6113f9231ccaa3b3f93c08f863ca9f8b984dc2"
version: "f1dc0e796665f344950e106107257fc2c05f6a3366f0843eabc26713505d0048"
build_date: "2020-07-07T03:51:23.642Z"
size_mb: 284.69921875
size: 298528768
sif: "https://datasets.datalad.org/shub/mattocci27/singularity-radian/latest/2020-07-07-0e6113f9-f1dc0e79/f1dc0e796665f344950e106107257fc2c05f6a3366f0843eabc26713505d0048.sif"
url: https://datasets.datalad.org/shub/mattocci27/singularity-radian/latest/2020-07-07-0e6113f9-f1dc0e79/
recipe: https://datasets.datalad.org/shub/mattocci27/singularity-radian/latest/2020-07-07-0e6113f9-f1dc0e79/Singularity
collection: mattocci27/singularity-radian
---

# mattocci27/singularity-radian:latest

```bash
$ singularity pull shub://mattocci27/singularity-radian:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:focal

%labels
  Maintainer mattocci
  R_Version 4.0.2

%apprun radian
  exec radian "${@}"

%apprun R
  exec R "${@}"

%apprun Rscript
  exec Rscript "${@}"

%runscript
  exec R "${@}"

%post
  # Software versions
  export R_VERSION=4.0.2

  # Get dependencies
  apt-get update
  apt-get install -y --no-install-recommends \
    locales \
    gnupg

  # Configure default locale
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
  locale-gen en_US.utf8
  /usr/sbin/update-locale LANG=en_US.UTF-8
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8

  # Install R
  echo "deb http://cran.r-project.org/bin/linux/ubuntu focal-cran40/" > /etc/apt/sources.list.d/r.list
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
  apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
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
    libopenblas-openmp-dev \
    libpython3-dev \
    python3-dev \
    python3-pip

  # Add a default CRAN mirror
  echo "options(repos = c(CRAN = 'https://cloud.r-project.org/'), download.file.method = 'libcurl')" >> /usr/lib/R/etc/Rprofile.site

  # Add a directory for host R libraries
  mkdir -p /library
  echo "R_LIBS_SITE=/library:\${R_LIBS_SITE}" >> /usr/lib/R/etc/Renviron.site

  # install radian
  pip3 install -U radian

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [mattocci27/singularity-radian](https://github.com/mattocci27/singularity-radian)
 - License: [MIT License](https://api.github.com/licenses/mit)

