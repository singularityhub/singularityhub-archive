---
id: 14744
name: "TomHarrop/r-containers"
branch: "master"
tag: "bioconductor_3.11"
commit: "ae3e49fbdb6c7a9a05fc5b88cc55ac3663b40036"
version: "90e5137662810c688b0c3149b7acd5bb9d5163f1bc7e997fb7d47bcc7ee2dd6c"
build_date: "2021-04-13T02:15:38.947Z"
size_mb: 1561.7578125
size: 1637621760
sif: "https://datasets.datalad.org/shub/TomHarrop/r-containers/bioconductor_3.11/2021-04-13-ae3e49fb-90e51376/90e5137662810c688b0c3149b7acd5bb9d5163f1bc7e997fb7d47bcc7ee2dd6c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/r-containers/bioconductor_3.11/2021-04-13-ae3e49fb-90e51376/
recipe: https://datasets.datalad.org/shub/TomHarrop/r-containers/bioconductor_3.11/2021-04-13-ae3e49fb-90e51376/Singularity
collection: TomHarrop/r-containers
---

# TomHarrop/r-containers:bioconductor_3.11

```bash
$ singularity pull shub://TomHarrop/r-containers:bioconductor_3.11
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bioconductor/bioconductor_docker:RELEASE_3_11

%help

    R 4.0.0 with Bioconductor 3.11
    
%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "Bioconductor 3.11"

%post
    # install packages from bioconductor
    Rscript -e "options(Ncpus=8); \
        BiocManager::install(c( \
            'adegenet', \
            'apeglm', \
            'ashr', \
            'Biostrings', \
            'dada2', \
            'DESeq2', \
            'future.apply', \
            'GenomicAlignments', \
            'GenomicFeatures', \
            'GenomicRanges', \
            'Gviz', \
            'Mfuzz', \
            'pheatmap', \
            'phyloseq', \
            'rehh', \
            'ShortRead', \
            'SNPRelate', \
            'systemPipeR', \
            'tximport', \
            'tximeta', \
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

