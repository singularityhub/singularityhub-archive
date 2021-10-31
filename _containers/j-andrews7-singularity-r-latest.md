---
id: 13945
name: "j-andrews7/singularity-r"
branch: "master"
tag: "latest"
commit: "aa9f4ba080c244f625013a5ec5b4c4ac542cd9db"
version: "fd2768431ff1f8a0d5774894626850d4"
build_date: "2021-04-09T20:13:14.640Z"
size_mb: 893.0
size: 330817567
sif: "https://datasets.datalad.org/shub/j-andrews7/singularity-r/latest/2021-04-09-aa9f4ba0-fd276843/fd2768431ff1f8a0d5774894626850d4.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/j-andrews7/singularity-r/latest/2021-04-09-aa9f4ba0-fd276843/
recipe: https://datasets.datalad.org/shub/j-andrews7/singularity-r/latest/2021-04-09-aa9f4ba0-fd276843/Singularity
collection: j-andrews7/singularity-r
---

# j-andrews7/singularity-r:latest

```bash
$ singularity pull shub://j-andrews7/singularity-r:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels
  Maintainer Jared Andrews
  R_Version 4.0.2

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
    aptitude

  # Configure default locale
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
  locale-gen en_US.utf8
  /usr/sbin/update-locale LANG=en_US.UTF-8
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8

  # Install R
  echo "deb http://cran.r-project.org/bin/linux/ubuntu xenial-cran40/" > /etc/apt/sources.list.d/r.list
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
  apt-get update
  aptitude install -y \
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
    libpng-dev \
    libfreetype6-dev \
    libtiff5-dev \
    libjpeg-dev \
    libgsl-dev \
    librsvg2-dev \
    libnode-dev \
    libv8-dev \
    software-properties-common

  # Add a default CRAN mirror
  echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'), download.file.method = 'libcurl')" >> /usr/lib/R/etc/Rprofile.site

  # Add a directory for host R libraries
  mkdir -p /library
  echo "R_LIBS_SITE=/library:\${R_LIBS_SITE}" >> /usr/lib/R/etc/Renviron.site

  # Update python
  add-apt-repository ppa:deadsnakes/ppa
  apt-get update
  apt-get install -y python3.8 python3.8-dev python3.8-distutils python3.8-venv

  # Create/activate virtualenv
  python3.8 -m venv dev3.8/
  . dev3.8/bin/activate

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [j-andrews7/singularity-r](https://github.com/j-andrews7/singularity-r)
 - License: [MIT License](https://api.github.com/licenses/mit)

