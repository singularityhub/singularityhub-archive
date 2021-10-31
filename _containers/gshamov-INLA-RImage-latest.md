---
id: 12185
name: "gshamov/INLA-RImage"
branch: "master"
tag: "latest"
commit: "923c7e79e6cbce87619cd8986a057ed6fedfe2f7"
version: "373480495dd2cd81c9dea56a69aebe48"
build_date: "2020-06-16T01:32:36.960Z"
size_mb: 2248.0
size: 745082911
sif: "https://datasets.datalad.org/shub/gshamov/INLA-RImage/latest/2020-06-16-923c7e79-37348049/373480495dd2cd81c9dea56a69aebe48.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/gshamov/INLA-RImage/latest/2020-06-16-923c7e79-37348049/
recipe: https://datasets.datalad.org/shub/gshamov/INLA-RImage/latest/2020-06-16-923c7e79-37348049/Singularity
collection: gshamov/INLA-RImage
---

# gshamov/INLA-RImage:latest

```bash
$ singularity pull shub://gshamov/INLA-RImage:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From:  rocker/r-ver:latest

%post
        apt-get update
        apt-get install -y libssl-dev libsasl2-dev jags
        apt-get install -y curl  httpie libudunits2-dev
        #apt-get install -y gdal-bin gdal-data libgdal-dev libgdal-grass libgdal-java

        R -e "install.packages('ggplot')"
        R -e "install.packages('jsonlite')"
        R -e "install.packages('dplyr')"
        R -e "install.packages('ggplot2')"
        R -e "install.packages('igraph')"
        R -e "install.packages('Matrix')"
        R -e "install.packages('shiny')"
        R -e "install.packages('rjags')"
        R -e "install.packages('dclone')"
        R -e "install.packages('sp')"
        R -e "install.packages('lme4')"
        R -e "install.packages('MASS')"
        R -e "install.packages('psych')"

       #echo "DONE with dependencies?"
       #sleep 10

        R -e 'install.packages("INLA", repos="https://inla.r-inla-download.org/R/stable")'
        R -e 'update.packages("INLA", dep=TRUE)'
        mkdir /global
        mkdir /global/scratch
        mkdir /scratch
        mkdir /project

%runscript
        R --version
```

## Collection

 - Name: [gshamov/INLA-RImage](https://github.com/gshamov/INLA-RImage)
 - License: None

