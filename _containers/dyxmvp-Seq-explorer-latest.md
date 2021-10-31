---
id: 6565
name: "dyxmvp/Seq-explorer"
branch: "master"
tag: "latest"
commit: "ab651fb3adc3293e2cd859079da738af74987fef"
version: "4d3cc63290fa9c060d78641694c05bc8"
build_date: "2019-01-26T22:48:03.176Z"
size_mb: 1565
size: 527044639
sif: "https://datasets.datalad.org/shub/dyxmvp/Seq-explorer/latest/2019-01-26-ab651fb3-4d3cc632/4d3cc63290fa9c060d78641694c05bc8.simg"
url: https://datasets.datalad.org/shub/dyxmvp/Seq-explorer/latest/2019-01-26-ab651fb3-4d3cc632/
recipe: https://datasets.datalad.org/shub/dyxmvp/Seq-explorer/latest/2019-01-26-ab651fb3-4d3cc632/Singularity
collection: dyxmvp/Seq-explorer
---

# dyxmvp/Seq-explorer:latest

```bash
$ singularity pull shub://dyxmvp/Seq-explorer:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:18.04

%labels
  Maintainer Yanxiang Deng

%environment
  export SHINY_PORT=31337

%help
  A shiny app for interactive single-cell data analysis
  https://github.com/dyxmvp/Seq-explorer

%runscript
  export SINGULARITY_CACHEDIR=~/project/.singularity
  cd /Seq-explorer-master
  exec R -e "options(browser='firefox');shiny::runApp(host='0.0.0.0', port=$SHINY_PORT, launch.browser=TRUE)"

%post
  apt-get update
  apt-get install -y wget unzip firefox
  apt-get install -y libcurl4-openssl-dev
  apt-get install -y libsodium-dev
  apt-get install -y libhdf5-dev
  apt-get install -y libssl-dev
  apt-get install -y libopenblas-dev
  apt-get install -y gcc fort77 aptitude
  aptitude install -y g++
  aptitude install -y xorg-dev
  aptitude install -y libreadline-dev
  aptitude install -y gfortran
  apt-get clean
  apt-get install -y r-base
  wget https://github.com/dyxmvp/Seq-explorer/archive/master.zip
  unzip master.zip
  cd /Seq-explorer-master
  R --slave -e "install.packages('devtools'); install.packages('shiny');install.packages('shinyFiles'); \
  install.packages('shinydashboard');install.packages('shinyjs');install.packages('shinyBS'); \
  devtools::install_github('andrewsali/shinycssloaders');devtools::install_github('rstudio/DT');install.packages('dplyr'); \
  install.packages('Rcpp');install.packages('RcppProgress');install.packages('RcppEigen');install.packages('Matrix'); \
  install.packages('ggplot2');install.packages('plotly');install.packages('cowplot');install.packages('Seurat');install.packages('mclust')"
```

## Collection

 - Name: [dyxmvp/Seq-explorer](https://github.com/dyxmvp/Seq-explorer)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

