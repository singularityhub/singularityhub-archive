---
id: 15158
name: "TomHarrop/pollen-its-wrapper"
branch: "master"
tag: "v0.0.1"
commit: "5e29f8caf08f173fae6035e25007ac91daad5096"
version: "d2ac9b40c5f4138db622e1fa7d450600a9caee8ecf40eb086364191026593856"
build_date: "2020-12-22T01:42:06.987Z"
size_mb: 1376.7578125
size: 1443635200
sif: "https://datasets.datalad.org/shub/TomHarrop/pollen-its-wrapper/v0.0.1/2020-12-22-5e29f8ca-d2ac9b40/d2ac9b40c5f4138db622e1fa7d450600a9caee8ecf40eb086364191026593856.sif"
url: https://datasets.datalad.org/shub/TomHarrop/pollen-its-wrapper/v0.0.1/2020-12-22-5e29f8ca-d2ac9b40/
recipe: https://datasets.datalad.org/shub/TomHarrop/pollen-its-wrapper/v0.0.1/2020-12-22-5e29f8ca-d2ac9b40/Singularity
collection: TomHarrop/pollen-its-wrapper
---

# TomHarrop/pollen-its-wrapper:v0.0.1

```bash
$ singularity pull shub://TomHarrop/pollen-its-wrapper:v0.0.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/verse:4.0.3

%help
    Container for pollen-its-wrapper v0.0.1

%labels
    VERSION "pollen-its-wrapper v0.0.1"
    MAINTAINER "Tom Harrop"

%post
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C

    # install dependencies
    apt-get update
    apt-get install -y \
        libbz2-dev \
        liblzma-dev \
        libpcre++-dev \
        python3-pip

    # install packages from bioconductor
    Rscript -e "options(Ncpus=8); \
        install.packages('BiocManager') ; \
        BiocManager::install(c(\
            'dada2', \
            'data.table', \
            'gtools'), 
            type='source', ask=FALSE)"

    /usr/bin/python3 -m pip \
        install --upgrade \
        pip \
        setuptools \
        wheel

    /usr/bin/python3 -m pip \
        install \
    	biopython==1.78 \
        cutadapt==3.1 \
        pandas==1.1.5

    # install pipeline
    /usr/bin/python3 -m pip \
        install \
        git+git://github.com/tomharrop/pollen-its-wrapper.git@v0.0.1

%runscript
    exec /usr/local/bin/pollen_its_wrapper "$@"
```

## Collection

 - Name: [TomHarrop/pollen-its-wrapper](https://github.com/TomHarrop/pollen-its-wrapper)
 - License: None

