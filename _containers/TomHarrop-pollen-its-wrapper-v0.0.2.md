---
id: 15159
name: "TomHarrop/pollen-its-wrapper"
branch: "master"
tag: "v0.0.2"
commit: "09d7e6e1b8780ff318f50247ce67c53e7affb4e7"
version: "431d6d14a38bb4642447dd010ed8ed4316e9210aae5b36e7b6a63f700088d51f"
build_date: "2020-12-22T02:28:41.689Z"
size_mb: 1376.7578125
size: 1443635200
sif: "https://datasets.datalad.org/shub/TomHarrop/pollen-its-wrapper/v0.0.2/2020-12-22-09d7e6e1-431d6d14/431d6d14a38bb4642447dd010ed8ed4316e9210aae5b36e7b6a63f700088d51f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/pollen-its-wrapper/v0.0.2/2020-12-22-09d7e6e1-431d6d14/
recipe: https://datasets.datalad.org/shub/TomHarrop/pollen-its-wrapper/v0.0.2/2020-12-22-09d7e6e1-431d6d14/Singularity
collection: TomHarrop/pollen-its-wrapper
---

# TomHarrop/pollen-its-wrapper:v0.0.2

```bash
$ singularity pull shub://TomHarrop/pollen-its-wrapper:v0.0.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/verse:4.0.3

%help
    Container for pollen-its-wrapper v0.0.2

%labels
    VERSION "pollen-its-wrapper v0.0.2"
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
        git+git://github.com/tomharrop/pollen-its-wrapper.git@v0.0.2

%runscript
    exec /usr/local/bin/pollen_its_wrapper "$@"
```

## Collection

 - Name: [TomHarrop/pollen-its-wrapper](https://github.com/TomHarrop/pollen-its-wrapper)
 - License: None

