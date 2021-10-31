---
id: 11744
name: "jacobhepkema/scanem-r"
branch: "master"
tag: "latest"
commit: "b3a9904f2c02118ac45617a5bc366d60a95c12e6"
version: "fe5406cae559ddc46ad733deec7ee27d"
build_date: "2021-03-11T15:21:29.124Z"
size_mb: 1228.0
size: 425115679
sif: "https://datasets.datalad.org/shub/jacobhepkema/scanem-r/latest/2021-03-11-b3a9904f-fe5406ca/fe5406cae559ddc46ad733deec7ee27d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/jacobhepkema/scanem-r/latest/2021-03-11-b3a9904f-fe5406ca/
recipe: https://datasets.datalad.org/shub/jacobhepkema/scanem-r/latest/2021-03-11-b3a9904f-fe5406ca/Singularity
collection: jacobhepkema/scanem-r
---

# jacobhepkema/scanem-r:latest

```bash
$ singularity pull shub://jacobhepkema/scanem-r:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: rocker/r-ver:3.6.0

%labels
    Maintainer @jacobhepkema
    Version v0.1
  
%post
    apt-get update && apt-get install -y --no-install-recommends procps lbzip2 libhdf4-alt-dev libhdf5-dev libxml-parser-perl && install2.r --error BiocManager optparse stringr pracma hashmap reshape2 ggplot2 dplyr viridis gridExtra igraph ade4 && R -e "BiocManager::install(c('rhdf5', 'pheatmap', 'Biostrings', 'ggseqlogo', 'ggrepel', 'DelayedMatrixStats', 'xtable'), update=FALSE, ask=FALSE)"

# smoke test
R --version

%runscript
    exec Rscript "$@"
```

## Collection

 - Name: [jacobhepkema/scanem-r](https://github.com/jacobhepkema/scanem-r)
 - License: None

