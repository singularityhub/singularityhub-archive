---
id: 10663
name: "marcjwilliams1/dnds-clonesize-container"
branch: "master"
tag: "latest"
commit: "510900b47009b71818eb479e2bb55a63f657ad17"
version: "1e97c691d6df7e7a1e0d49012e12fd27"
build_date: "2019-10-24T14:11:14.306Z"
size_mb: 5015.0
size: 1814319135
sif: "https://datasets.datalad.org/shub/marcjwilliams1/dnds-clonesize-container/latest/2019-10-24-510900b4-1e97c691/1e97c691d6df7e7a1e0d49012e12fd27.sif"
url: https://datasets.datalad.org/shub/marcjwilliams1/dnds-clonesize-container/latest/2019-10-24-510900b4-1e97c691/
recipe: https://datasets.datalad.org/shub/marcjwilliams1/dnds-clonesize-container/latest/2019-10-24-510900b4-1e97c691/Singularity
collection: marcjwilliams1/dnds-clonesize-container
---

# marcjwilliams1/dnds-clonesize-container:latest

```bash
$ singularity pull shub://marcjwilliams1/dnds-clonesize-container:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: jupyter/datascience-notebook


  # add R packages from CRAN
  Rscript -e "install.packages(pkgs = c('devtools', 'ggplot2', 'dplyr', 'tidyr', 'stringr', 'cowplot', 'gtools', 'argparse','jcolors', 'ggthemes', 'viridis', 'forcats', 'Hmisc', 'readr', 'ggridges', 'readxl', 'purrr', 'bayestestR'), \
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
   Rscript -e "library(BiocManager); install('TCGAbiolinks')"

  # add R packages from github
   Rscript -e "library(devtools); install_github('im3sanger/dndscv')"

  #add julia packages
  julia -e "import Pkg; Pkg.add(\"Distributions\")"
  julia -e "import Pkg; Pkg.add(\"DataFrames\")"
  julia -e "import Pkg; Pkg.add(\"Optim\")"
  julia -e "import Pkg; Pkg.add(\"ArgParse\")"
  julia -e "import Pkg; Pkg.add(\"Distances\")"
  julia -e "import Pkg; Pkg.add(\"CSV\")"
  julia -e "import Pkg; Pkg.add(\"Plots\")"
  julia -e "import Pkg; Pkg.add(\"Flux\")"
  julia -e "import Pkg; Pkg.add(\"Revise\")"
  julia -e "import Pkg; Pkg.add(\"StatsBase\")"
  julia -e "import Pkg; Pkg.add(\"LinearAlgebra\")"
  julia -e "import Pkg; Pkg.add(\"ProgressMeter\")"
  julia -e "import Pkg; Pkg.add(\"NLSolversBase\")"
  julia -e "import Pkg; Pkg.add(\"RCall\")
```

## Collection

 - Name: [marcjwilliams1/dnds-clonesize-container](https://github.com/marcjwilliams1/dnds-clonesize-container)
 - License: None

