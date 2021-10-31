---
id: 11496
name: "ivs-containers/r"
branch: "master"
tag: "latest"
commit: "814ccc3a2511de399df20fab7808638aafa0b39a"
version: "00053eb5b87a3df132566b28d1e1212b"
build_date: "2019-11-13T11:06:42.730Z"
size_mb: 1343.0
size: 392761375
sif: "https://datasets.datalad.org/shub/ivs-containers/r/latest/2019-11-13-814ccc3a-00053eb5/00053eb5b87a3df132566b28d1e1212b.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ivs-containers/r/latest/2019-11-13-814ccc3a-00053eb5/
recipe: https://datasets.datalad.org/shub/ivs-containers/r/latest/2019-11-13-814ccc3a-00053eb5/Singularity
collection: ivs-containers/r
---

# ivs-containers/r:latest

```bash
$ singularity pull shub://ivs-containers/r:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:buster-slim

%post
  # the R version to install
  export R_VERSION=3.6.1

  # install packages needed for the configuration
  apt update
  apt install -y --no-install-recommends locales gnupg2 software-properties-common 
  # dirmngr gnupg2 software-properties-common 

  # Configure default locale
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
  locale-gen en_US.utf8
  /usr/sbin/update-locale LANG=en_US.UTF-8
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8

  # Add the R repository
  apt-key adv --keyserver keys.gnupg.net --recv-key 'E19F5F87128899B192B1A2C2AD5F960A256A04AF'
  add-apt-repository 'deb http://cloud.r-project.org/bin/linux/debian buster-cran35/'
  apt update
    
  # install software packages
  apt install -y --no-install-recommends \
      gcc                                \
      gfortran                           \
      libcurl4-openssl-dev               \
      libssl-dev                         \
      libxml2-dev                        \
      libgsl-dev                         \
      libxt-dev                          \
      dirmngr                            \
      libpoppler-cpp-dev                 \
      r-base=${R_VERSION}*               \
      r-base-core=${R_VERSION}*          \
      r-base-dev=${R_VERSION}*           \
      r-recommended=${R_VERSION}* 
      
  # install R packages
  echo 'install.packages(c("tidyverse", "rstan"), clean=TRUE, Ncpus=parallel::detectCores())' | R --slave    
      
  # remove R tmp files
  rm -rf /tmp/Rtmp*
```

## Collection

 - Name: [ivs-containers/r](https://github.com/ivs-containers/r)
 - License: [MIT License](https://api.github.com/licenses/mit)

