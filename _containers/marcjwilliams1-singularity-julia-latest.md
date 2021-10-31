---
id: 8848
name: "marcjwilliams1/singularity-julia"
branch: "master"
tag: "latest"
commit: "5b7b2a65804537c9c9620024ff9bc0a70ada5529"
version: "53d4391f1fdba09f77d5f2ab1283177a"
build_date: "2020-03-02T15:47:04.003Z"
size_mb: 5283.0
size: 1903767583
sif: "https://datasets.datalad.org/shub/marcjwilliams1/singularity-julia/latest/2020-03-02-5b7b2a65-53d4391f/53d4391f1fdba09f77d5f2ab1283177a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/marcjwilliams1/singularity-julia/latest/2020-03-02-5b7b2a65-53d4391f/
recipe: https://datasets.datalad.org/shub/marcjwilliams1/singularity-julia/latest/2020-03-02-5b7b2a65-53d4391f/Singularity
collection: marcjwilliams1/singularity-julia
---

# marcjwilliams1/singularity-julia:latest

```bash
$ singularity pull shub://marcjwilliams1/singularity-julia:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: jupyter/datascience-notebook

%labels
  Maintainer Marc J Williams

%help
  Singularity image for following paper:

%post
  # add R packages from CRAN
  #Rscript -e "install.packages(pkgs = c('ggplot', 'cowplot', 'readr'))"

  # add R packages from github
  #Rscript -e "library(devtools); install_github('marcjwilliams1/dndscv', ref = 'dev')"

  #add julia packages
  julia -e "import Pkg; Pkg.add(\"Distributions\")"
```

## Collection

 - Name: [marcjwilliams1/singularity-julia](https://github.com/marcjwilliams1/singularity-julia)
 - License: None

