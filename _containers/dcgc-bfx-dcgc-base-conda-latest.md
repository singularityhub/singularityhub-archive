---
id: 15677
name: "dcgc-bfx/dcgc-base-conda"
branch: "main"
tag: "latest"
commit: "d58a0e586d927e7bae1ea7b50560de461de48c88"
version: "f0eae72c8b5cdc4459a6310a1dcc909cdd5e37c67dca58f8ca1737e2d39cc9a3"
build_date: "2021-04-09T17:52:07.016Z"
size_mb: 1253.3125
size: 1314193408
sif: "https://datasets.datalad.org/shub/dcgc-bfx/dcgc-base-conda/latest/2021-04-09-d58a0e58-f0eae72c/f0eae72c8b5cdc4459a6310a1dcc909cdd5e37c67dca58f8ca1737e2d39cc9a3.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dcgc-bfx/dcgc-base-conda/latest/2021-04-09-d58a0e58-f0eae72c/
recipe: https://datasets.datalad.org/shub/dcgc-bfx/dcgc-base-conda/latest/2021-04-09-d58a0e58-f0eae72c/Singularity
collection: dcgc-bfx/dcgc-base-conda
---

# dcgc-bfx/dcgc-base-conda:latest

```bash
$ singularity pull shub://dcgc-bfx/dcgc-base-conda:latest
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

