---
id: 8287
name: "alikerr/INLA-RImage"
branch: "master"
tag: "latest"
commit: "ddfd15bbe64b6443bcc4f6f78db6501d30a0dc43"
version: "abe5498602344776f7429878c0264dfb"
build_date: "2020-01-17T16:12:02.923Z"
size_mb: 1660
size: 528609311
sif: "https://datasets.datalad.org/shub/alikerr/INLA-RImage/latest/2020-01-17-ddfd15bb-abe54986/abe5498602344776f7429878c0264dfb.simg"
url: https://datasets.datalad.org/shub/alikerr/INLA-RImage/latest/2020-01-17-ddfd15bb-abe54986/
recipe: https://datasets.datalad.org/shub/alikerr/INLA-RImage/latest/2020-01-17-ddfd15bb-abe54986/Singularity
collection: alikerr/INLA-RImage
---

# alikerr/INLA-RImage:latest

```bash
$ singularity pull shub://alikerr/INLA-RImage:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From:  rocker/r-ver:latest

%post
        apt-get update
        apt-get install -y libssl-dev libsasl2-dev jags wget
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

        # echo "DONE with dependencies?"
        # sleep 10

        R -e 'install.packages("INLA", repos="https://inla.r-inla-download.org/R/stable")'
        R -e 'update.packages("INLA", dep=TRUE)'
        
        R -e 'download.file("https://i-pri.org/special/Biostatistics/Software/gINLAnd/gINLAnd_0.0.0.tar.gz", "gINLAnd")'

        R -e 'install.packages("gINLAnd", repos = NULL, type = "source")'
                
        mkdir /global
        mkdir /global/scratch
        mkdir /scratch
        mkdir /project

%run
        R --version
```

## Collection

 - Name: [alikerr/INLA-RImage](https://github.com/alikerr/INLA-RImage)
 - License: None

