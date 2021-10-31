---
id: 9875
name: "granek/singularity-rstudio-tidyverse"
branch: "master"
tag: "3.6.0"
commit: "1659289ade2471942aef73dc12280c6167adf840"
version: "1f7206c4c46229d6886cdafe49e5813c"
build_date: "2020-01-21T17:39:56.905Z"
size_mb: 1552
size: 438222879
sif: "https://datasets.datalad.org/shub/granek/singularity-rstudio-tidyverse/3.6.0/2020-01-21-1659289a-1f7206c4/1f7206c4c46229d6886cdafe49e5813c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/granek/singularity-rstudio-tidyverse/3.6.0/2020-01-21-1659289a-1f7206c4/
recipe: https://datasets.datalad.org/shub/granek/singularity-rstudio-tidyverse/3.6.0/2020-01-21-1659289a-1f7206c4/Singularity
collection: granek/singularity-rstudio-tidyverse
---

# granek/singularity-rstudio-tidyverse:3.6.0

```bash
$ singularity pull shub://granek/singularity-rstudio-tidyverse:3.6.0
```

## Singularity Recipe

```singularity
BootStrap: shub
From: nickjer/singularity-rstudio:3.6.0

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

