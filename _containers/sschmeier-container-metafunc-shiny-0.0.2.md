---
id: 12934
name: "sschmeier/container-metafunc-shiny"
branch: "master"
tag: "0.0.2"
commit: "4e9096ab0986e9423a665e4f662ba6a4867a3d71"
version: "9ab0c8b5887213d6a6e398b476a7dbc4741bd64922dda299f4d46ad4b4910be9"
build_date: "2020-05-11T22:49:52.580Z"
size_mb: 486.81640625
size: 510464000
sif: "https://datasets.datalad.org/shub/sschmeier/container-metafunc-shiny/0.0.2/2020-05-11-4e9096ab-9ab0c8b5/9ab0c8b5887213d6a6e398b476a7dbc4741bd64922dda299f4d46ad4b4910be9.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/container-metafunc-shiny/0.0.2/2020-05-11-4e9096ab-9ab0c8b5/
recipe: https://datasets.datalad.org/shub/sschmeier/container-metafunc-shiny/0.0.2/2020-05-11-4e9096ab-9ab0c8b5/Singularity
collection: sschmeier/container-metafunc-shiny
---

# sschmeier/container-metafunc-shiny:0.0.2

```bash
$ singularity pull shub://sschmeier/container-metafunc-shiny:0.0.2
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
   conda install --yes r-base=3.6.1 r-shiny=1.4.0.2  r-shinydashboard=0.7.1 r-shinythemes=1.1.2 r-dt=0.12 r-formattable=0.2.0.1 r-tidyverse=1.3.0 r-ggplot2=3.3.0 r-data.table=1.12.8 r-dplyr=0.8.5 r-stringr=1.4.0 r-reshape2=1.4.3 r-rsqlite=2.2.0 r-splitstackshape=1.4.8 r-dbi=1.1.0
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/container-metafunc-shiny](https://github.com/sschmeier/container-metafunc-shiny)
 - License: None

