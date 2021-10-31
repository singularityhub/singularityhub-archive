---
id: 4930
name: "dominik-handler/AP_singu"
branch: "master"
tag: "r"
commit: "ed20f19ac3fbdce6ad9625280215d88bf6fcb8fc"
version: "3d832ed3dcd6a6311ddacb15fc71c165"
build_date: "2019-10-18T12:26:33.072Z"
size_mb: 2440
size: 904704031
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/r/2019-10-18-ed20f19a-3d832ed3/3d832ed3dcd6a6311ddacb15fc71c165.simg"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/r/2019-10-18-ed20f19a-3d832ed3/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/r/2019-10-18-ed20f19a-3d832ed3/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:r

```bash
$ singularity pull shub://dominik-handler/AP_singu:r
```

## Singularity Recipe

```singularity
#R in singularity
Bootstrap: docker
From: ubuntu:14.04

%runscript
  "$@"

%post

  apt-get update
  apt-get -y install wget git sudo curl libssl-dev libxml2-dev software-properties-common libcurl4-openssl-dev
  add-apt-repository universe
  apt-get update
  apt-get -y install pandoc
  
  apt-get clean && apt-get update && apt-get install -y \
      locales \
      language-pack-fi  \
      language-pack-en && \
      export LANGUAGE=en_US.UTF-8 && \
      export LANG=en_US.UTF-8 && \
      export LC_ALL=en_US.UTF-8 && \
      locale-gen en_US.UTF-8 && \
      dpkg-reconfigure locales

  #insall R-dependencies
  apt-get -y build-dep r-base
  
  #install R
  mkdir /R
  cd /R
  version="3.5.0"
  wget http://cran.at.r-project.org/src/base/R-3/R-$version.tar.gz
  tar -xzf R-$version.tar.gz  
  cd /R/R-$version
  ./configure 
  make
  make install

  apt-get clean

  #install R-packages  
  R --slave -e 'install.packages(c( "devtools"), repos = "http://cran.wu.ac.at/") '
  R --slave -e 'install.packages(c( "tidyverse", "plotly", "Cairo", "gridExtra"), repos = "http://cran.wu.ac.at/") '
  R --slave -e 'options(unzip = "internal"); devtools::install_github("tidyverse/ggplot2") '
  R --slave -e 'install.packages(c( "cowplot" ), repos = "http://cran.wu.ac.at/") '
  R --slave -e 'source("http://bioconductor.org/biocLite.R"); biocLite("remotes"); biocLite("pachterlab/sleuth@v0.30.0")'
  R --slave -e 'source("https://bioconductor.org/biocLite.R"); biocLite("rhdf5")'
  #R --slave -e 'options(unzip = "internal"); devtools::install_github("dominik-handler/sleuth", ref = "master")'
  R --slave -e 'source("https://bioconductor.org/biocLite.R"); biocLite("remotes"); biocLite("COMBINE-lab/wasabi")'

  apt-get clean
    
  mkdir /groups
  mkdir /scratch
  mkdir /scratch-ii2
  mkdir /clustertmp


%test
  R --version
  Rscript --version
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

