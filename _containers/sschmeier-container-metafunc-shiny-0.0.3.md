---
id: 13059
name: "sschmeier/container-metafunc-shiny"
branch: "master"
tag: "0.0.3"
commit: "936fdbc40130a4ddd7cc7d2bc025bd8c4fb37aa9"
version: "47370d6f5913c43659e69d81dedd85dd60d7fd52d308629cc18481754b9f7b5e"
build_date: "2020-08-31T03:21:17.653Z"
size_mb: 536.9296875
size: 563011584
sif: "https://datasets.datalad.org/shub/sschmeier/container-metafunc-shiny/0.0.3/2020-08-31-936fdbc4-47370d6f/47370d6f5913c43659e69d81dedd85dd60d7fd52d308629cc18481754b9f7b5e.sif"
url: https://datasets.datalad.org/shub/sschmeier/container-metafunc-shiny/0.0.3/2020-08-31-936fdbc4-47370d6f/
recipe: https://datasets.datalad.org/shub/sschmeier/container-metafunc-shiny/0.0.3/2020-08-31-936fdbc4-47370d6f/Singularity
collection: sschmeier/container-metafunc-shiny
---

# sschmeier/container-metafunc-shiny:0.0.3

```bash
$ singularity pull shub://sschmeier/container-metafunc-shiny:0.0.3
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
   conda install --yes r-base=3.6.3 r-shiny=1.4.0.2  r-shinydashboard=0.7.1 r-shinythemes=1.1.2 r-dt=0.12 r-formattable=0.2.0.1 r-tidyverse r-ggplot2=3.3.0 r-data.table=1.12.8 r-dplyr=0.8.5 r-stringr=1.4.0 r-reshape2=1.4.3 r-rsqlite=2.2.0 r-splitstackshape=1.4.8 r-dbi=1.1.0
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/container-metafunc-shiny](https://github.com/sschmeier/container-metafunc-shiny)
 - License: None

