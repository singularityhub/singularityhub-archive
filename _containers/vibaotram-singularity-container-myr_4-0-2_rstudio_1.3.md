---
id: 15785
name: "vibaotram/singularity-container"
branch: "master"
tag: "myr_4-0-2_rstudio_1.3"
commit: "db024c9f89dcce2a2be7ffbaf2c9460bbc279134"
version: "fbdac18d650d22ccde6177be28a4b34a18276c00f155e21ab14af7a5aba329c3"
build_date: "2021-04-01T06:37:19.881Z"
size_mb: 892.265625
size: 935608320
sif: "https://datasets.datalad.org/shub/vibaotram/singularity-container/myr_4-0-2_rstudio_1.3/2021-04-01-db024c9f-fbdac18d/fbdac18d650d22ccde6177be28a4b34a18276c00f155e21ab14af7a5aba329c3.sif"
url: https://datasets.datalad.org/shub/vibaotram/singularity-container/myr_4-0-2_rstudio_1.3/2021-04-01-db024c9f-fbdac18d/
recipe: https://datasets.datalad.org/shub/vibaotram/singularity-container/myr_4-0-2_rstudio_1.3/2021-04-01-db024c9f-fbdac18d/Singularity
collection: vibaotram/singularity-container
---

# vibaotram/singularity-container:myr_4-0-2_rstudio_1.3

```bash
$ singularity pull shub://vibaotram/singularity-container:myr_4-0-2_rstudio_1.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/rstudio:4.0.2 #rocker/tidyverse:4.0.3 #or: rocker/tidyverse:latest

%environment
  R_VERSION=4.0.2
  export R_VERSION
  export PATH=$PATH

%labels
  Author Sebastien Cunnac
  Version v0.0.1
  R_Version 4.0.2
  build_date March 2021
  R_bioconductor True

%post
  apt-get update
#  apt-get install -y apt-transport-https apt-utils software-properties-common
#  add-apt-repository main
#  add-apt-repository universe
#  add-apt-repository multiverse

  # General Utilities
  apt-get install -y wget rsync git-lfs openssh-client build-essential

  # Specific libs for R packages to run
  apt-get install -y texinfo texlive-latex-extra libmagick++-dev \
      libcairo2-dev libxt-dev \
      libglu1-mesa-dev libgmp-dev libmpfr-dev libv8-dev \
      libudunits2-dev gdal-bin libgdal-dev libglpk-dev libpoppler-cpp-dev

  # cleaning up
  apt-get autoremove --purge --yes
  apt-get clean

  # installing packages from cran
  install2.r --error \
      --deps FALSE --skipinstalled \
      Cairo \
      svglite \
      nloptr \
      rgl \
      fs \
      BiocManager

  # installing Bioconductor
  R --slave -e 'BiocManager::install(ask = FALSE)'

  # disable session timeout
  echo "session-timeout-minutes=0" >> /etc/rstudio/rsession.conf
  echo "auth-timeout-minutes=0" >> /etc/rstudio/rserver.conf
  rstudio-server restart

  # Display versions
  echo '############################################'
  echo "## Build Date: $(date)"
  echo "## R sessionInfo:\n"
  R --slave -e 'sessionInfo()'
```

## Collection

 - Name: [vibaotram/singularity-container](https://github.com/vibaotram/singularity-container)
 - License: None

