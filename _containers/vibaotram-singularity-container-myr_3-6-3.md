---
id: 13959
name: "vibaotram/singularity-container"
branch: "master"
tag: "myr_3-6-3"
commit: "8a1166ea654a1ff6e35a765109bdc6e0b94a33eb"
version: "8bbe86c3cf94b0cf1c7de4cc764b043001d8f1e7e8db3356acc5b6dabf83d981"
build_date: "2021-03-22T09:55:25.173Z"
size_mb: 1206.78125
size: 1265401856
sif: "https://datasets.datalad.org/shub/vibaotram/singularity-container/myr_3-6-3/2021-03-22-8a1166ea-8bbe86c3/8bbe86c3cf94b0cf1c7de4cc764b043001d8f1e7e8db3356acc5b6dabf83d981.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/vibaotram/singularity-container/myr_3-6-3/2021-03-22-8a1166ea-8bbe86c3/
recipe: https://datasets.datalad.org/shub/vibaotram/singularity-container/myr_3-6-3/2021-03-22-8a1166ea-8bbe86c3/Singularity
collection: vibaotram/singularity-container
---

# vibaotram/singularity-container:myr_3-6-3

```bash
$ singularity pull shub://vibaotram/singularity-container:myr_3-6-3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/tidyverse:3.6.3 #or: rocker/tidyverse:latest

%environment
  R_VERSION=3.6.3
  export R_VERSION
  export PATH=$PATH

%labels
  Author Sebastien Cunnac
  Version v0.0.2
  R_Version 3.6.3
  build_date June 2020
  R_bioconductor True

%post
  apt-get update
#  apt-get install -y apt-transport-https apt-utils software-properties-common
#  add-apt-repository main
#  add-apt-repository universe
#  add-apt-repository multiverse

  # General Utilities
  apt-get install -y wget rsync git-lfs openssh-client build-essential libudunits2-dev gdal-bin libgdal-dev

  # java-8
  apt update
  apt install -y apt-transport-https ca-certificates wget dirmngr gnupg software-properties-common
  wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | sudo apt-key add -
  add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/
  apt update
  apt install -y adoptopenjdk-8-hotspot

  # Specific libs for R packages to run
  apt-get install -y texinfo texlive-latex-extra libmagick++-dev \
      libcairo2-dev libxt-dev \
      libglu1-mesa-dev libgmp-dev libmpfr-dev libv8-dev

  # cleaning up
  apt-get autoremove --purge --yes
  apt-get clean

  # installing packages from cran
  install2.r --error \
      --deps TRUE \
      Cairo \
      svglite \
      nloptr \
      rgl \
      fs \
      BiocManager

  # installing Bioconductor
  R --slave -e 'BiocManager::install(ask = FALSE)'

  # Display versions
  echo '############################################'
  echo "## Build Date: $(date)"
  echo "## R sessionInfo:\n"
  R --slave -e 'sessionInfo()'
```

## Collection

 - Name: [vibaotram/singularity-container](https://github.com/vibaotram/singularity-container)
 - License: None

