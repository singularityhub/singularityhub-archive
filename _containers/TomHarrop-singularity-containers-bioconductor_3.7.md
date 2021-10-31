---
id: 9193
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "bioconductor_3.7"
commit: "a78f80e501dc9a2fb8c5bf0a0a01328964f68472"
version: "dc548d01d69b512cd9da6b331263c9d3"
build_date: "2019-10-09T22:28:12.838Z"
size_mb: 2358
size: 852619295
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/bioconductor_3.7/2019-10-09-a78f80e5-dc548d01/dc548d01d69b512cd9da6b331263c9d3.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/bioconductor_3.7/2019-10-09-a78f80e5-dc548d01/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/bioconductor_3.7/2019-10-09-a78f80e5-dc548d01/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:bioconductor_3.7

```bash
$ singularity pull shub://TomHarrop/singularity-containers:bioconductor_3.7
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bioconductor/release_core2:R3.5.1_Bioc3.7

%help

    R 3.5.1 with Bioconductor 3.7, DESeq2_1.20.0 and Mfuzz_2.40.0
    
%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "Bioconductor 3.7"

%post

    # install depenedencies
    apt-get update
    apt-get install -y \
        libbz2-dev \
        liblzma-dev \
        libpcre++-dev \
        tk-dev \
        tcl-dev

    # install packages from bioconductor
    Rscript -e "options(Ncpus=8); \
        BiocInstaller::biocLite(c( \
            'adegenet', \
            'DESeq2', \
            'Mfuzz', \
            'pheatmap', \
            'phyloseq', \
            'SNPRelate', \
            'systemPipeR', \
            'valr', \
            'VariantAnnotation' \
            ), \
        type='source', ask=FALSE)"

%runscript

    exec /usr/local/bin/R "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

