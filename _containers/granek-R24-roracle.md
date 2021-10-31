---
id: 2645
name: "granek/R24"
branch: "master"
tag: "roracle"
commit: "d1cc413598ab4366ce7412c8f36b6d04c58090e8"
version: "ea20409bbc713b5c13a2b7ffbfd39497"
build_date: "2018-04-25T06:48:58.773Z"
size_mb: 1988
size: 841273375
sif: "https://datasets.datalad.org/shub/granek/R24/roracle/2018-04-25-d1cc4135-ea20409b/ea20409bbc713b5c13a2b7ffbfd39497.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/granek/R24/roracle/2018-04-25-d1cc4135-ea20409b/
recipe: https://datasets.datalad.org/shub/granek/R24/roracle/2018-04-25-d1cc4135-ea20409b/Singularity
collection: granek/R24
---

# granek/R24:roracle

```bash
$ singularity pull shub://granek/R24:roracle
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:stretch

##------------------------------------------------------------
## Build example:
## sudo singularity build roracle.simg singularity_roracle
##
## Run example:
## singularity run roracle.simg
##------------------------------------------------------------


%runscript
exec "$@"

%apprun standard
    exec "${@}"

%environment
  export CONDA_DIR=/opt/conda
  export PATH=$CONDA_DIR/bin:$PATH
  export SHELL=/bin/bash
  export LC_ALL=C.UTF-8
  export LANG=C.UTF-8

%post
  ##------------------------------------------------------------
  ## Install basics needed by conda
  ##------------------------------------------------------------
  apt-get update
  apt-get install -y --no-install-recommends \
    wget \
    bzip2 \
    ca-certificates \
    ssh \
    build-essential \
    libaio1 libaio-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

  ##------------------------------------------------------------
  ## Install conda (for qiime2)
  ##------------------------------------------------------------
  CONDA_DIR=/opt/conda
  export PATH=$CONDA_DIR/bin:$PATH
  cd /tmp && \
      mkdir -p $CONDA_DIR && \
      wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.4.10-Linux-x86_64.sh && \
      echo "bec6203dbb2f53011e974e9bf4d46e93 Miniconda3-4.4.10-Linux-x86_64.sh" | md5sum -c - && \
      /bin/bash Miniconda3-4.4.10-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
      rm Miniconda3-4.4.10-Linux-x86_64.sh && \
      $CONDA_DIR/bin/conda clean -tipsy
  
  ##------------------------------------------------------------
  ## Install roracle with conda
  ##------------------------------------------------------------
  $CONDA_DIR/bin/conda install -c anaconda -c r oracle-instantclient r-base
  export LD_LIBRARY_PATH=/opt/conda/lib:$LD_LIBRARY_PATH
  export OCI_LIB=/opt/conda/lib
  export OCI_INC=/opt/conda/include

  $CONDA_DIR/bin/Rscript -e "install.packages(pkgs = c('DBI','ROracle'), \
     repos='https://cran.revolutionanalytics.com/', \
     dependencies=TRUE)"
  
  ##------------------------------------------------------------
  ## Make some mountpoints 
  ##------------------------------------------------------------
  mkdir -p /data
  mkdir -p /intermediate
  mkdir -p /results
  mkdir -p /scripts

%labels
    Maintainer Josh Granek
    Version v0.001
```

## Collection

 - Name: [granek/R24](https://github.com/granek/R24)
 - License: None

