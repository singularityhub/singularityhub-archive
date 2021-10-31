---
id: 12538
name: "TomHarrop/r-containers"
branch: "master"
tag: "bioconductor_3.10"
commit: "22b77812ec8211c7bbe29c9bbfc6dfba6a833982"
version: "3e5f3908a1390ac19cd46ea7c895b861c4604b9c7fc9e5ea9275dab40ad218b5"
build_date: "2021-03-01T03:47:57.989Z"
size_mb: 1294.71484375
size: 1357606912
sif: "https://datasets.datalad.org/shub/TomHarrop/r-containers/bioconductor_3.10/2021-03-01-22b77812-3e5f3908/3e5f3908a1390ac19cd46ea7c895b861c4604b9c7fc9e5ea9275dab40ad218b5.sif"
url: https://datasets.datalad.org/shub/TomHarrop/r-containers/bioconductor_3.10/2021-03-01-22b77812-3e5f3908/
recipe: https://datasets.datalad.org/shub/TomHarrop/r-containers/bioconductor_3.10/2021-03-01-22b77812-3e5f3908/Singularity
collection: TomHarrop/r-containers
---

# TomHarrop/r-containers:bioconductor_3.10

```bash
$ singularity pull shub://TomHarrop/r-containers:bioconductor_3.10
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bioconductor/bioconductor_full:RELEASE_3_10

%help

    R 3.6.1 with Bioconductor 3.10
    
%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "Bioconductor 3.10"

%post
    # install packages from bioconductor
    Rscript -e "options(Ncpus=8); \
        BiocManager::install(c( \
            'adegenet', \
            'Biostrings', \
            'dada2', \
            'DESeq2', \
            'GenomicAlignments', \
            'GenomicFeatures', \
            'GenomicRanges', \
            'Gviz', \
            'Mfuzz', \
            'pheatmap', \
            'phyloseq', \
            'ShortRead', \
            'SNPRelate', \
            'systemPipeR', \
            'tximport', \
            'valr', \
            'VariantAnnotation', \
            'vcfR' \
            ), \
        type='source', ask=FALSE)"

%runscript

    exec /usr/local/bin/R "$@"
```

## Collection

 - Name: [TomHarrop/r-containers](https://github.com/TomHarrop/r-containers)
 - License: None

