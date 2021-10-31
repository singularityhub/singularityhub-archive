---
id: 4256
name: "dynverse/dynwrap"
branch: "devel"
tag: "r"
commit: "97cb7b06d68bd0eae2c07570bdf837cd8e97f774"
version: "06349c6e607e917ca9284146322a5948"
build_date: "2019-03-28T15:14:02.967Z"
size_mb: 2138
size: 813994015
sif: "https://datasets.datalad.org/shub/dynverse/dynwrap/r/2019-03-28-97cb7b06-06349c6e/06349c6e607e917ca9284146322a5948.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dynverse/dynwrap/r/2019-03-28-97cb7b06-06349c6e/
recipe: https://datasets.datalad.org/shub/dynverse/dynwrap/r/2019-03-28-97cb7b06-06349c6e/Singularity
collection: dynverse/dynwrap
---

# dynverse/dynwrap:r

```bash
$ singularity pull shub://dynverse/dynwrap:r
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: rocker/tidyverse

%labels
    version 0.2.0.8

%environment
    OPENBLAS_NUM_THREADS=1
    NUMEXPR_NUM_THREADS=1
    MKL_NUM_THREADS=1
    OMP_NUM_THREADS=1

    export OPENBLAS_NUM_THREADS NUMEXPR_NUM_THREADS MKL_NUM_THREADS OMP_NUM_THREADS

%post
    apt-get update && apt-get install -y libhdf5-dev libssh-dev
    echo 'utils::setRepositories(ind=1:4)' > ~/.Rprofile
    R -e 'devtools::install_cran("Rcpp")'
    R -e 'devtools::install_github("dynverse/dyndimred", dependencies = TRUE)'
    R -e 'devtools::install_github("dynverse/dynwrap", dependencies = TRUE)'
    R -e 'devtools::install_cran(c("RcppEigen", "RSpectra", "RcppArmadillo"))' # preinstall certain rcpp libraries
```

## Collection

 - Name: [dynverse/dynwrap](https://github.com/dynverse/dynwrap)
 - License: None

