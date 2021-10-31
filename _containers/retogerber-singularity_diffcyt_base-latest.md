---
id: 13197
name: "retogerber/singularity_diffcyt_base"
branch: "master"
tag: "latest"
commit: "c4fc1d74fdab1e8da2752eef31f392a2bd348081"
version: "044337a4fb1c123a4cf5bc98e5a00efc1abaa213c4c9f92451bd2ced84f265f7"
build_date: "2021-03-31T05:44:39.524Z"
size_mb: 1490.3359375
size: 1562730496
sif: "https://datasets.datalad.org/shub/retogerber/singularity_diffcyt_base/latest/2021-03-31-c4fc1d74-044337a4/044337a4fb1c123a4cf5bc98e5a00efc1abaa213c4c9f92451bd2ced84f265f7.sif"
url: https://datasets.datalad.org/shub/retogerber/singularity_diffcyt_base/latest/2021-03-31-c4fc1d74-044337a4/
recipe: https://datasets.datalad.org/shub/retogerber/singularity_diffcyt_base/latest/2021-03-31-c4fc1d74-044337a4/Singularity
collection: retogerber/singularity_diffcyt_base
---

# retogerber/singularity_diffcyt_base:latest

```bash
$ singularity pull shub://retogerber/singularity_diffcyt_base:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/verse:4.0.0

%post

        R -e 'install.packages(c("BiocManager","lme4","multcomp","reshape2","circlize","MASS","mice","survival","stats","RhpcBLASctl","uwot","dirmult"), verbose=FALSE, quiet=TRUE)'

        R -e 'BiocManager::install(version="3.12",ask=FALSE);BiocManager::install(c("flowCore","FlowSOM","SummarizedExperiment","S4Vectors", "limma","edgeR","ComplexHeatmap","BiocParallel","BiocStyle", "CATALYST"), ask = FALSE, verbose=FALSE, quiet=TRUE)'
```

## Collection

 - Name: [retogerber/singularity_diffcyt_base](https://github.com/retogerber/singularity_diffcyt_base)
 - License: None

