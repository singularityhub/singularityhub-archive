---
id: 6807
name: "tpall/geo-rnaseq"
branch: "master"
tag: "latest"
commit: "cbbb4555249e6953a318dc068d95b21fdf2e1e50"
version: "80210c381b28932a0140aee78450a34e"
build_date: "2020-01-17T08:29:05.425Z"
size_mb: 3104.0
size: 1029046303
sif: "https://datasets.datalad.org/shub/tpall/geo-rnaseq/latest/2020-01-17-cbbb4555-80210c38/80210c381b28932a0140aee78450a34e.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/tpall/geo-rnaseq/latest/2020-01-17-cbbb4555-80210c38/
recipe: https://datasets.datalad.org/shub/tpall/geo-rnaseq/latest/2020-01-17-cbbb4555-80210c38/Singularity
collection: tpall/geo-rnaseq
---

# tpall/geo-rnaseq:latest

```bash
$ singularity pull shub://tpall/geo-rnaseq:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: tpall/singularity-tidyverse

%labels
  Maintainer tpall

%help
  This container will run geo-rnaseq workflow R scripts. Includes Rstudio server.

%post
  # Install dependencies
  apt-get update
  apt-get install -y \
    unzip \
    xorg \
    libx11-dev \
    libglu1-mesa-dev \
    libfreetype6-dev
  
  # Install CRAN packages
  Rscript -e "install.packages(c('bookdown','XML','formattable','gridExtra','gridBase','viridis','knitr','ape','data.table','kableExtra','sparkline','evaluate','hexbin','broom','digest'), repos = 'https://cloud.r-project.org', dependencies = TRUE)"
  
  # Install Bioconductor packages
  Rscript -e "BiocManager::install(update = FALSE, ask = FALSE)"
  Rscript -e "BiocManager::install(c('GEOquery', 'Biobase', 'limma', 'ggtree'), update = FALSE, ask = FALSE)"

  # Install Github packages
  Rscript -e "devtools::install_github('tpall/SRP')"
  Rscript -e "devtools::install_github('tpall/entrezquery')"
  
  # Install gridDiagram
  Rscript -e  "install.packages('https://www.stat.auckland.ac.nz/~paul/R/Diagram/gridDiagram_0.2-1.tar.gz', repos = NULL, type = 'source')" 

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [tpall/geo-rnaseq](https://github.com/tpall/geo-rnaseq)
 - License: [Other](None)

