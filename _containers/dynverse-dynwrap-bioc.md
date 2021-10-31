---
id: 4258
name: "dynverse/dynwrap"
branch: "devel"
tag: "bioc"
commit: "97cb7b06d68bd0eae2c07570bdf837cd8e97f774"
version: "78fa64740cb03b5c9d2317f949215837"
build_date: "2019-03-28T15:14:02.974Z"
size_mb: 2141
size: 815562783
sif: "https://datasets.datalad.org/shub/dynverse/dynwrap/bioc/2019-03-28-97cb7b06-78fa6474/78fa64740cb03b5c9d2317f949215837.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dynverse/dynwrap/bioc/2019-03-28-97cb7b06-78fa6474/
recipe: https://datasets.datalad.org/shub/dynverse/dynwrap/bioc/2019-03-28-97cb7b06-78fa6474/Singularity
collection: dynverse/dynwrap
---

# dynverse/dynwrap:bioc

```bash
$ singularity pull shub://dynverse/dynwrap:bioc
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
    R -e 'options(echo = TRUE); install.packages("minqa")' # weird problem where minqa can't install when .Rprofile isn't empty
    echo 'utils::setRepositories(ind=1:4)' > ~/.Rprofile
    R -e 'devtools::install_cran("Rcpp")'
    R -e 'devtools::install_github("dynverse/dyndimred", dependencies = TRUE)'
    R -e 'devtools::install_github("dynverse/dynwrap", dependencies = TRUE)'
    R -e 'devtools::install_cran(c("RcppEigen", "RSpectra", "RcppArmadillo"))' # preinstall certain rcpp libraries
    R -e 'devtools::install_cran("SingleCellExperiment")'
```

## Collection

 - Name: [dynverse/dynwrap](https://github.com/dynverse/dynwrap)
 - License: None

