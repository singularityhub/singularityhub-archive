---
id: 15160
name: "TomHarrop/pollen-its-wrapper"
branch: "master"
tag: "v0.0.3"
commit: "69cf3b435b0524b7437af495abcb9407852d4c4b"
version: "ae57dab3ff0bbb8869ffa24bf39531b507d472fc790ab5e90117b5b67ad8a298"
build_date: "2020-12-22T02:47:35.030Z"
size_mb: 1463.02734375
size: 1534095360
sif: "https://datasets.datalad.org/shub/TomHarrop/pollen-its-wrapper/v0.0.3/2020-12-22-69cf3b43-ae57dab3/ae57dab3ff0bbb8869ffa24bf39531b507d472fc790ab5e90117b5b67ad8a298.sif"
url: https://datasets.datalad.org/shub/TomHarrop/pollen-its-wrapper/v0.0.3/2020-12-22-69cf3b43-ae57dab3/
recipe: https://datasets.datalad.org/shub/TomHarrop/pollen-its-wrapper/v0.0.3/2020-12-22-69cf3b43-ae57dab3/Singularity
collection: TomHarrop/pollen-its-wrapper
---

# TomHarrop/pollen-its-wrapper:v0.0.3

```bash
$ singularity pull shub://TomHarrop/pollen-its-wrapper:v0.0.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/verse:4.0.3

%help
    Container for pollen-its-wrapper v0.0.3

%labels
    VERSION "pollen-its-wrapper v0.0.3"
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
        pandas==1.1.5 \
        snakemake==5.31.1

    # install pipeline
    /usr/bin/python3 -m pip \
        install \
        git+git://github.com/tomharrop/pollen-its-wrapper.git@v0.0.3

%runscript
    exec /usr/local/bin/pollen_its_wrapper "$@"
```

## Collection

 - Name: [TomHarrop/pollen-its-wrapper](https://github.com/TomHarrop/pollen-its-wrapper)
 - License: None

