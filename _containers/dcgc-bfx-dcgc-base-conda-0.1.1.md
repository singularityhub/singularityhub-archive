---
id: 15881
name: "dcgc-bfx/dcgc-base-conda"
branch: "main"
tag: "0.1.1"
commit: "3261047224132096bd5598481c48efc0998f022a"
version: "e7889a60384d3f009fbdb2d3a093efc44137cc6a3a35f6caeb6d49d54fb56dae"
build_date: "2021-04-09T22:32:53.761Z"
size_mb: 1255.640625
size: 1316634624
sif: "https://datasets.datalad.org/shub/dcgc-bfx/dcgc-base-conda/0.1.1/2021-04-09-32610472-e7889a60/e7889a60384d3f009fbdb2d3a093efc44137cc6a3a35f6caeb6d49d54fb56dae.sif"
url: https://datasets.datalad.org/shub/dcgc-bfx/dcgc-base-conda/0.1.1/2021-04-09-32610472-e7889a60/
recipe: https://datasets.datalad.org/shub/dcgc-bfx/dcgc-base-conda/0.1.1/2021-04-09-32610472-e7889a60/Singularity
collection: dcgc-bfx/dcgc-base-conda
---

# dcgc-bfx/dcgc-base-conda:0.1.1

```bash
$ singularity pull shub://dcgc-bfx/dcgc-base-conda:0.1.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:latest

%labels
    Author fabian.rost@tu-dresden.de
    Organisation DcGC
    Version latest

%help
    Base container based on conda docker container with basic python and R
    packages installed.

%environment
  DEBIAN_FRONTEND=noninteractive

%post
  export PATH=/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

  apt-get update --fix-missing -q
  apt-get install -y -q\
    build-essential \
    gawk \
    git \
    libatlas-base-dev \
    p7zip-full \
    unzip

  apt-get clean -q
  rm -rf /var/lib/apt/lists/*

  conda update --quiet --yes conda
  conda config --add channels defaults
  conda config --add channels bioconda
  conda config --add channels conda-forge

  conda install --quiet --yes mamba

  mamba update --quiet --yes --all

  mamba install --quiet --yes \
    blosc \
    bottleneck \
    cmake \
    fastparquet \
    fsspec \
    gcsfs \
    html5lib \
    jinja2 \
    lxml \
    matplotlib \
    mscorefonts \
    numba \
    numexpr \
    openpyxl \
    pandas \
    pip \
    pyarrow \
    pyreadstat \
    pytables \
    pyyaml \
    rpy2 \
    scipy \
    seaborn \
    tabulate \
    zlib \
    `# R packages` \
    r-base>=4.0.3 \
    r-data.table \
    r-devtools \
    r-dplyr \
    r-essentials \
    r-ggplot2 \
    r-ggpubr \
    r-ggsci \
    r-ggsignif \
    r-hmisc \
    r-knitr \
    r-magrittr \
    r-matrix \
    r-purrr \
    r-usethis \
    r-r.utils \
    r-rcolorbrewer \
    r-reticulate \
    r-tidyr \
    r-tidyverse \
    r-xlsx

  mamba clean --quiet --yes --all

  chmod -R a+w /opt
```

## Collection

 - Name: [dcgc-bfx/dcgc-base-conda](https://github.com/dcgc-bfx/dcgc-base-conda)
 - License: None

