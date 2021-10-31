---
id: 2646
name: "granek/R24"
branch: "master"
tag: "qiime2"
commit: "345516c216546fdb2b50718f51d995c180d685f6"
version: "a06708821b28c31b19a36ac460f3e63b"
build_date: "2018-05-25T02:19:39.040Z"
size_mb: 5814
size: 1884123167
sif: "https://datasets.datalad.org/shub/granek/R24/qiime2/2018-05-25-345516c2-a0670882/a06708821b28c31b19a36ac460f3e63b.simg"
url: https://datasets.datalad.org/shub/granek/R24/qiime2/2018-05-25-345516c2-a0670882/
recipe: https://datasets.datalad.org/shub/granek/R24/qiime2/2018-05-25-345516c2-a0670882/Singularity
collection: granek/R24
---

# granek/R24:qiime2

```bash
$ singularity pull shub://granek/R24:qiime2
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:stretch

##------------------------------------------------------------
## Build example:
## sudo singularity build qiime2.simg Singularity.qiime2
##
## Run example:
## singularity run qiime2.simg qiime info
##------------------------------------------------------------

%runscript
    exec "${@}"

%apprun standard
    exec "${@}"

%apprun qiime2
  ##------------------------------------------------------------
  ## Hack to avoid sourcing qiime2 for every command
  ## Best way I could figure out, since installing to conda base fails
  ## based on https://github.com/singularityware/singularity/issues/1038
  ##------------------------------------------------------------
  /bin/bash <<EOF
    source activate qiime2-2018.2
    # echo "$PATH"
    exec ${@}
EOF 

%environment
  export CONDA_DIR=/opt/conda
  export PATH=$CONDA_DIR/bin:$PATH
  export SHELL=/bin/bash
  export LC_ALL=C.UTF-8
  export LANG=C.UTF-8

%post
  ##------------------------------------------------------------
  ## Install basics needed by conda, plus lftp
  ##------------------------------------------------------------
  apt-get update
  apt-get install -y --no-install-recommends \
    wget \
    bzip2 \
    ca-certificates \
    lftp \
    ssh \
    build-essential \
    ea-utils \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

  ##------------------------------------------------------------
  ## Install conda (for qiime2)
  ##------------------------------------------------------------
  CONDA_DIR=/opt/conda
  cd /tmp && \
      mkdir -p $CONDA_DIR && \
      wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.4.10-Linux-x86_64.sh && \
      echo "bec6203dbb2f53011e974e9bf4d46e93 Miniconda3-4.4.10-Linux-x86_64.sh" | md5sum -c - && \
      /bin/bash Miniconda3-4.4.10-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
      rm Miniconda3-4.4.10-Linux-x86_64.sh && \
      $CONDA_DIR/bin/conda clean -tipsy
  
  ##------------------------------------------------------------
  ## Install qiime2 with conda
  ##------------------------------------------------------------
  cd /tmp && \
      wget --quiet https://data.qiime2.org/distro/core/qiime2-2018.2-py35-linux-conda.yml && \
      $CONDA_DIR/bin/conda env create -n qiime2-2018.2 --file qiime2-2018.2-py35-linux-conda.yml && \
      rm qiime2-2018.2-py35-linux-conda.yml && \
      $CONDA_DIR/bin/conda clean -tipsy
   
  ##------------------------------------------------------------
  ## Install R packages into qiime environment
  ##------------------------------------------------------------
  $CONDA_DIR/envs/qiime2-2018.2/bin/Rscript -e "install.packages(pkgs = c('argparser','tidyverse'), \
    repos='https://cran.revolutionanalytics.com/', \
    dependencies=TRUE)"

  ##------------------------------------------------------------
  ## set up link so vsearch can masquerade as usearch61
  ##------------------------------------------------------------
  ln -sf $CONDA_DIR/bin/vsearch $CONDA_DIR/bin/usearch61
  
  ##------------------------------------------------------------
  ## Make some mountpoints 
  ##------------------------------------------------------------
  mkdir -p /data
  mkdir -p /intermediate
  mkdir -p /results
  mkdir -p /scripts

%labels
    Maintainer Josh Granek
    Version v0.005
```

## Collection

 - Name: [granek/R24](https://github.com/granek/R24)
 - License: None

