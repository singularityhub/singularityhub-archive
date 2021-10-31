---
id: 2792
name: "granek/crne_transposon"
branch: "master"
tag: "canu"
commit: "233b0990d8100e14b620b9b06864ecd87d8b1dd7"
version: "d059a295a92f3df1205b6d2ff1e4f8e9"
build_date: "2018-05-16T11:13:33.252Z"
size_mb: 2065
size: 768196639
sif: "https://datasets.datalad.org/shub/granek/crne_transposon/canu/2018-05-16-233b0990-d059a295/d059a295a92f3df1205b6d2ff1e4f8e9.simg"
url: https://datasets.datalad.org/shub/granek/crne_transposon/canu/2018-05-16-233b0990-d059a295/
recipe: https://datasets.datalad.org/shub/granek/crne_transposon/canu/2018-05-16-233b0990-d059a295/Singularity
collection: granek/crne_transposon
---

# granek/crne_transposon:canu

```bash
$ singularity pull shub://granek/crne_transposon:canu
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:buster

%runscript
  exec "${@}"
  
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
    sra-toolkit \
    canu \
    bwa \
    samtools \
    ncbi-blast+ \
    python-biopython \
    mafft \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# other aligners: t-coffee, muscle, dialign-tx, kalign


##------------------------------------------------------------
CONDA_DIR=/opt/conda
cd /tmp && \
    mkdir -p $CONDA_DIR && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.4.10-Linux-x86_64.sh && \
    echo "bec6203dbb2f53011e974e9bf4d46e93 Miniconda3-4.4.10-Linux-x86_64.sh" | md5sum -c - && \
    /bin/bash Miniconda3-4.4.10-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda3-4.4.10-Linux-x86_64.sh && \
    $CONDA_DIR/bin/conda clean -tipsy

$CONDA_DIR/bin/conda install -c bioconda pilon biopython && \
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

%labels
    Maintainer Josh Granek
    Version v0.007
```

## Collection

 - Name: [granek/crne_transposon](https://github.com/granek/crne_transposon)
 - License: None

