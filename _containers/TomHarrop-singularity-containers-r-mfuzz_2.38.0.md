---
id: 4891
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "r-mfuzz_2.38.0"
commit: "a1ddf489cab7e2174093a62e0c3483430b3237e8"
version: "8071cabc09218f1b86af73f094411bae"
build_date: "2018-09-19T07:00:17.345Z"
size_mb: 2564
size: 982110239
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/r-mfuzz_2.38.0/2018-09-19-a1ddf489-8071cabc/8071cabc09218f1b86af73f094411bae.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/r-mfuzz_2.38.0/2018-09-19-a1ddf489-8071cabc/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/r-mfuzz_2.38.0/2018-09-19-a1ddf489-8071cabc/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:r-mfuzz_2.38.0

```bash
$ singularity pull shub://TomHarrop/singularity-containers:r-mfuzz_2.38.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/verse:3.4.4

%help

    Container for Mfuzz 2.38.0 in R 3.4.4 with data.table and DESeq2

%labels

    MAINTAINER "Tom Harrop"
    VERSION "R 3.4.4 with Mfuzz 2.38.0 and DESeq2 1.18.1"

%post

    # install depenedencies
    apt-get update
    apt-get install -y \
        tk-dev tcl-dev

    # install packages from bioconductor
    Rscript -e "options(Ncpus=8); \
        source('https://bioconductor.org/biocLite.R') ; \
        biocLite(c('data.table', 'DESeq2', 'Mfuzz'), \
            type='source', ask=FALSE)"

%runscript

    exec /usr/local/bin/R "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

