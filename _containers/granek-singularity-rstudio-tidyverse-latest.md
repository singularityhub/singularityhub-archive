---
id: 6182
name: "granek/singularity-rstudio-tidyverse"
branch: "master"
tag: "latest"
commit: "cfcac13e8c960885fce37ad99253f709c987d72b"
version: "42f6d03482be83d1bcb5fa275ebc5739"
build_date: "2021-04-13T15:12:19.647Z"
size_mb: 1307
size: 385433631
sif: "https://datasets.datalad.org/shub/granek/singularity-rstudio-tidyverse/latest/2021-04-13-cfcac13e-42f6d034/42f6d03482be83d1bcb5fa275ebc5739.simg"
url: https://datasets.datalad.org/shub/granek/singularity-rstudio-tidyverse/latest/2021-04-13-cfcac13e-42f6d034/
recipe: https://datasets.datalad.org/shub/granek/singularity-rstudio-tidyverse/latest/2021-04-13-cfcac13e-42f6d034/Singularity
collection: granek/singularity-rstudio-tidyverse
---

# granek/singularity-rstudio-tidyverse:latest

```bash
$ singularity pull shub://granek/singularity-rstudio-tidyverse:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: nickjer/singularity-rstudio

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

