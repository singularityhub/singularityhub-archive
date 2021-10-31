---
id: 12558
name: "sschmeier/container-metafunc-shiny"
branch: "master"
tag: "latest"
commit: "3d3b37a39df2ebeec6be7a1eea570e0d46b3c3f2"
version: "937106de06df339e828bab3466113340f2604f89153e5928c619c663f697ccae"
build_date: "2020-03-18T22:20:47.991Z"
size_mb: 480.5546875
size: 503898112
sif: "https://datasets.datalad.org/shub/sschmeier/container-metafunc-shiny/latest/2020-03-18-3d3b37a3-937106de/937106de06df339e828bab3466113340f2604f89153e5928c619c663f697ccae.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/container-metafunc-shiny/latest/2020-03-18-3d3b37a3-937106de/
recipe: https://datasets.datalad.org/shub/sschmeier/container-metafunc-shiny/latest/2020-03-18-3d3b37a3-937106de/Singularity
collection: sschmeier/container-metafunc-shiny
---

# sschmeier/container-metafunc-shiny:latest

```bash
$ singularity pull shub://sschmeier/container-metafunc-shiny:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%labels
   AUTHOR s.schmeier@pm.me

%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container
  export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
  unset CONDA_DEFAULT_ENV
  export ANACONDA_HOME=/opt/conda

%post
   export PATH=/opt/conda/bin:$PATH
   echo "We add conda channels."
   conda config --add channels defaults
   conda config --add channels conda-forge
   # update conda
   conda update -n base -c defaults conda
   echo "We install tools."
   conda install --yes r-base=3.6.1 r-shiny=1.4.0.2  r-shinydashboard=0.7.1 r-shinythemes=1.1.2 r-dt=0.12 r-formattable=0.2.0.1 r-tidyverse=1.3.0 r-ggplot2=3.3.0 r-data.table=1.12.8 r-dplyr=0.8.5 r-stringr=1.4.0 r-reshape2=1.4.3 r-rsqlite=2.2.0 r-splitstackshape=1.4.8
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/container-metafunc-shiny](https://github.com/sschmeier/container-metafunc-shiny)
 - License: None

