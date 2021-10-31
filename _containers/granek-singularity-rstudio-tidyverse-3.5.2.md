---
id: 6183
name: "granek/singularity-rstudio-tidyverse"
branch: "master"
tag: "3.5.2"
commit: "2a6c8b03b6e4fc812cf3cd373d91acdd796e5651"
version: "340040f680856249e67797e752f0f570"
build_date: "2021-02-01T17:36:20.844Z"
size_mb: 1307
size: 385450015
sif: "https://datasets.datalad.org/shub/granek/singularity-rstudio-tidyverse/3.5.2/2021-02-01-2a6c8b03-340040f6/340040f680856249e67797e752f0f570.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/granek/singularity-rstudio-tidyverse/3.5.2/2021-02-01-2a6c8b03-340040f6/
recipe: https://datasets.datalad.org/shub/granek/singularity-rstudio-tidyverse/3.5.2/2021-02-01-2a6c8b03-340040f6/Singularity
collection: granek/singularity-rstudio-tidyverse
---

# granek/singularity-rstudio-tidyverse:3.5.2

```bash
$ singularity pull shub://granek/singularity-rstudio-tidyverse:3.5.2
```

## Singularity Recipe

```singularity
BootStrap: shub
From: nickjer/singularity-rstudio:3.5.2

%labels
  Maintainer Josh Granek
#  RStudio_Version 1.1.463

%help
  This will run RStudio Server with tidyverse and support for knitting

%apprun rserver
  exec rserver "${@}"

%runscript
  exec rserver "${@}"

%environment
  export PATH=/usr/lib/rstudio-server/bin:${PATH}

%post
  # Install tidyverse and packages necessary for knitting to HTML 
   Rscript -e "install.packages(pkgs = c('tidyverse','caTools','rprojroot'), \
     repos='https://cran.revolutionanalytics.com/', \
     dependencies=TRUE, \
     clean = TRUE)"
```

## Collection

 - Name: [granek/singularity-rstudio-tidyverse](https://github.com/granek/singularity-rstudio-tidyverse)
 - License: [MIT License](https://api.github.com/licenses/mit)

