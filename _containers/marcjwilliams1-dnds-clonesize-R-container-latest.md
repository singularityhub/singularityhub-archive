---
id: 10729
name: "marcjwilliams1/dnds-clonesize-R-container"
branch: "master"
tag: "latest"
commit: "299ad35d95e8a478dbb27ab92784d247593a23ee"
version: "282e13ea3090576c1de36743fc7fa6cf"
build_date: "2020-07-28T16:53:53.769Z"
size_mb: 3622.0
size: 1521274911
sif: "https://datasets.datalad.org/shub/marcjwilliams1/dnds-clonesize-R-container/latest/2020-07-28-299ad35d-282e13ea/282e13ea3090576c1de36743fc7fa6cf.sif"
url: https://datasets.datalad.org/shub/marcjwilliams1/dnds-clonesize-R-container/latest/2020-07-28-299ad35d-282e13ea/
recipe: https://datasets.datalad.org/shub/marcjwilliams1/dnds-clonesize-R-container/latest/2020-07-28-299ad35d-282e13ea/Singularity
collection: marcjwilliams1/dnds-clonesize-R-container
---

# marcjwilliams1/dnds-clonesize-R-container:latest

```bash
$ singularity pull shub://marcjwilliams1/dnds-clonesize-R-container:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: asachet/rocker-stan

%labels
  Maintainer Marc J Williams

%help
  Singularity image for following paper:

%post
  # add R packages from CRAN
  Rscript -e "install.packages(pkgs = c('devtools', 'cowplot', 'gtools', 'argparse','jcolors', 'ggthemes', 'viridis','Hmisc','ggridges', 'readxl',
  'bayesplot', 'modelr', 'ggforce', 'ggfortify', 'bayestestR'), \
      repos='https://cran.revolutionanalytics.com/', \
      dependencies=TRUE, \
      clean = TRUE)"

   #add R packages from bioconductor
   Rscript -e "install.packages('BiocManager')"
   Rscript -e "library(BiocManager); install('GenomicRanges')"
   Rscript -e "library(BiocManager); install('IRanges')"
   Rscript -e "library(BiocManager); install('Biostrings')"
   Rscript -e "library(BiocManager); install('Rsamtools')"
   Rscript -e "library(BiocManager); install('seqinr')"
   Rscript -e "library(BiocManager); install('rtracklayer')"

  # add R packages from github
   Rscript -e "library(devtools); install_github('marcjwilliams1/dndscv', ref = 'dev')"
```

## Collection

 - Name: [marcjwilliams1/dnds-clonesize-R-container](https://github.com/marcjwilliams1/dnds-clonesize-R-container)
 - License: None

