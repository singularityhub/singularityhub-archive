---
id: 14806
name: "mlell/singularity-r"
branch: "master"
tag: "latest"
commit: "799fcd185848a04e103a9a0eae457ec4c22c568a"
version: "a8c5a6010f3934af032edfca440280bc"
build_date: "2021-02-03T18:16:49.316Z"
size_mb: 2564.0
size: 804618271
sif: "https://datasets.datalad.org/shub/mlell/singularity-r/latest/2021-02-03-799fcd18-a8c5a601/a8c5a6010f3934af032edfca440280bc.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/mlell/singularity-r/latest/2021-02-03-799fcd18-a8c5a601/
recipe: https://datasets.datalad.org/shub/mlell/singularity-r/latest/2021-02-03-799fcd18-a8c5a601/Singularity
collection: mlell/singularity-r
---

# mlell/singularity-r:latest

```bash
$ singularity pull shub://mlell/singularity-r:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:sid

%labels
  Maintainer Moritz Lell
  R_Version 4.0.2

%environment
  export OMP_NUM_THREADS=1

%apprun R
  exec R "${@}"

%apprun Rscript
  exec Rscript "${@}"

%runscript
  exec R "${@}"

%post
  # Software versions
  export R_VERSION=4.0.3

  # Get dependencies
  apt-get update
  apt-get install -y --no-install-recommends \
    locales curl gpg dirmngr gpg-agent libopenblas-dev

  # Configure default locale
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
  locale-gen en_US.utf8
  /usr/sbin/update-locale LANG=en_US.UTF-8
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8

  # Install R
  apt-get update
  apt-get install -y --no-install-recommends \
    r-base=${R_VERSION}* \
    r-base-core=${R_VERSION}* \
    r-base-dev=${R_VERSION}* \
    r-recommended=${R_VERSION}* \
    r-base-html=${R_VERSION}* \
    r-doc-html=${R_VERSION}* \
    libpython3-all-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    libcairo2-dev \
    libxt-dev \
    pandoc \
    git \
    vim  \
    emacs \
    nano \
    graphviz \
    procps \
    libnetcdf18 libnetcdf-dev
    
  # Add a default CRAN mirror
  echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'), download.file.method = 'libcurl')" >> /usr/lib/R/etc/Rprofile.site
  
  # Set default python version
  ln -s python3 /usr/bin/python

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [mlell/singularity-r](https://github.com/mlell/singularity-r)
 - License: [Other](None)

