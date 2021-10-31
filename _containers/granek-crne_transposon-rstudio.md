---
id: 2791
name: "granek/crne_transposon"
branch: "master"
tag: "rstudio"
commit: "9eb914165cac1cfc68b62fa4128dd308f4ab9b29"
version: "3594525a2ab7b04eaa8956090cf68c2b"
build_date: "2018-12-03T09:49:39.785Z"
size_mb: 3956
size: 1408311327
sif: "https://datasets.datalad.org/shub/granek/crne_transposon/rstudio/2018-12-03-9eb91416-3594525a/3594525a2ab7b04eaa8956090cf68c2b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/granek/crne_transposon/rstudio/2018-12-03-9eb91416-3594525a/
recipe: https://datasets.datalad.org/shub/granek/crne_transposon/rstudio/2018-12-03-9eb91416-3594525a/Singularity
collection: granek/crne_transposon
---

# granek/crne_transposon:rstudio

```bash
$ singularity pull shub://granek/crne_transposon:rstudio
```

## Singularity Recipe

```singularity
BootStrap: shub
From: nickjer/singularity-rstudio:3.5.1

%labels
    Maintainer Josh Granek
    Image_Version 0.009

##------------------------------------------------------------
## Build example:
## sudo singularity build canu_rstudio.simg Singularity.rstudio
##
## Run example:
## singularity run canu_rstudio.simg ls
## singularity run --app rstudio canu_rstudio.simg
##------------------------------------------------------------

%runscript
  exec "${@}"

%apprun rstudio
  exec rserver "${@}"

%environment
  export PATH=/usr/lib/rstudio-server/bin:${PATH}
  export CONDA_DIR=/opt/conda
  export PATH=$CONDA_DIR/bin:$PATH
  export SHELL=/bin/bash
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8
  export LANGUAGE=en_US.UTF-8

%post
  # Install extra stuff
  apt-get update
  apt-get install -y --no-install-recommends \
    curl \
    wget \
    bzip2 \
    parallel \
    bwa \
    samtools \
    ncbi-blast+ \
    mafft \
    git \
    ssh \
    emacs \
    less \
    make \
    libxml2-dev \
    libgsl0-dev \
    libglu1-mesa \
    libmariadb-client-lgpl-dev \
    htop
   apt-get clean
   rm -rf /var/lib/apt/lists/*

#--------------------------------------------------------------------------------
Rscript -e "install.packages(pkgs = c('argparse','tidyverse','R.utils','caTools'), \
    repos='https://cran.revolutionanalytics.com/', \
    dependencies=TRUE)"   

Rscript -e "if (!requireNamespace('BiocManager')){install.packages('BiocManager')}; \
    BiocManager::install(); \
    BiocManager::install(c('ggbio','GenomicRanges','rtracklayer'))"

# install ggbio 1.31.1 from github to get geom_arrowrect bugfix
Rscript -e "install.packages(pkgs = c('devtools'), \
    repos='https://cran.revolutionanalytics.com/', \
    dependencies=TRUE); \
    require(devtools); \
    install_github('tengfei/ggbio', ref='ce0b2a04c4dd15807eb60795a95ae73a1e4758dc')"
##------------------------------------------------------------
CONDA_DIR=/opt/conda
cd /tmp && \
    mkdir -p $CONDA_DIR && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.4.10-Linux-x86_64.sh && \
    echo "bec6203dbb2f53011e974e9bf4d46e93 Miniconda3-4.4.10-Linux-x86_64.sh" | md5sum -c - && \
    /bin/bash Miniconda3-4.4.10-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda3-4.4.10-Linux-x86_64.sh && \
    $CONDA_DIR/bin/conda clean -tipsy

$CONDA_DIR/bin/conda install -c bioconda canu pilon biopython snpeff gatk sra-tools samtools bwakit bwa bcftools && \
    $CONDA_DIR/bin/conda clean -tipsy
#--------------------------------------------------------------------------------


# Helpful:
#------------------
# https://gitlab.oit.duke.edu/mccahill/jupyter-HTS-2017/blob/master/Dockerfile
# https://github.com/nickjer/singularity-r/blob/master/Singularity.3.4.3
# https://github.com/nickjer/singularity-rstudio/blob/master/Singularity
# https://www.singularity-hub.org/collections/174
# https://www.singularity-hub.org/collections/463

# sudo singularity build canu_rstudio.simg singularity_canu_rstudio
```

## Collection

 - Name: [granek/crne_transposon](https://github.com/granek/crne_transposon)
 - License: None

