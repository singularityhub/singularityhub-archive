---
id: 15433
name: "dominik-handler/AP_singu"
branch: "master"
tag: "tailfindr"
commit: "2b68de003f7815639b336cfa84b2975454e7d262"
version: "4e9484e005b6d90e31129ed6a1ec7b7892d1402d0e964ca457948c3ca4a44e93"
build_date: "2021-02-01T07:31:59.018Z"
size_mb: 578.42578125
size: 606523392
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/tailfindr/2021-02-01-2b68de00-4e9484e0/4e9484e005b6d90e31129ed6a1ec7b7892d1402d0e964ca457948c3ca4a44e93.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/tailfindr/2021-02-01-2b68de00-4e9484e0/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/tailfindr/2021-02-01-2b68de00-4e9484e0/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:tailfindr

```bash
$ singularity pull shub://dominik-handler/AP_singu:tailfindr
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at  
  TailfindR to identify PolyA tails in Nanopore DRS

%post    
  apt-get update
  apt-get -y install locales
  locale-gen en_US.UTF-8

  export LANG=en_US.UTF-8  
  export LANGUAGE=en_US:en  
  export LC_ALL=en_US.UTF-8  

  mkdir /install

  #install all required tools
  export DEBIAN_FRONTEND=noninteractive
  apt-get update
  apt-get -y install parallel wget build-essential bzip2 unzip git-core tar libbz2-dev tzdata unzip gnupg2 software-properties-common
  
  #install R
    apt-get update
    apt-get --assume-yes install pandoc curl libgit2-dev libssl-dev libcurl4-gnutls-dev libxml2-dev xorg-dev libopenblas-dev libcairo2-dev libxt-dev libtiff5-dev openjdk-8-jdk libreadline6-dev libpng-dev libhdf5-dev

    mkdir -p /install/R
    cd /install/R
    version="3.6.3"

    gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
    gpg -a --export E298A3A825C0D65DFD57CBB651716619E084DAB9 | apt-key add -
    add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'
    apt-get update
    apt-get --assume-yes install r-base-dev

    #install R-packages  
    R --slave -e 'install.packages(c( "devtools"), repos = "http://cran.wu.ac.at/") '
    R --slave -e 'install.packages(c( "tidyverse"), repos = "http://cran.wu.ac.at/") '
    R --slave -e 'options(unzip = "internal"); devtools::install_github("adnaniazi/tailfindr", ref="gregor_polya_base_end") '

  #clean up and make container smaller
    rm -rf /install
   
%environment
  #!/bin/bash
  export LANG=en_US.UTF-8  
  export LANGUAGE=en_US:en  
  export LC_ALL=en_US.UTF-8  

%runscript
  $@
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

