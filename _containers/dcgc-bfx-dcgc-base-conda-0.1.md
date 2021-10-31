---
id: 15679
name: "dcgc-bfx/dcgc-base-conda"
branch: "main"
tag: "0.1"
commit: "014ff970e63b4ceff179d376798896e49810f457"
version: "15310e90b7f3c488d82392c52d3175897a77ff9a249f07fbd0dec9c52997d92e"
build_date: "2021-04-09T15:36:47.180Z"
size_mb: 1225.5703125
size: 1285103616
sif: "https://datasets.datalad.org/shub/dcgc-bfx/dcgc-base-conda/0.1/2021-04-09-014ff970-15310e90/15310e90b7f3c488d82392c52d3175897a77ff9a249f07fbd0dec9c52997d92e.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dcgc-bfx/dcgc-base-conda/0.1/2021-04-09-014ff970-15310e90/
recipe: https://datasets.datalad.org/shub/dcgc-bfx/dcgc-base-conda/0.1/2021-04-09-014ff970-15310e90/Singularity
collection: dcgc-bfx/dcgc-base-conda
---

# dcgc-bfx/dcgc-base-conda:0.1

```bash
$ singularity pull shub://dcgc-bfx/dcgc-base-conda:0.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:latest

%labels
    Author fabian.rost@tu-dresden.de
    Organisation DcGC
    Version v0.0.1

%help
    Base container based on conda docker container with basic python and R
    packages installed.

%environment
  DEBIAN_FRONTEND=noninteractive

%post
  export PATH=/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

  apt-get update --fix-missing
  apt-get install -y \
    build-essential \
    gawk \
    git \
    p7zip-full \
    unzip

  apt-get clean
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

