---
id: 2605
name: "arccontainers/recipes"
branch: "master"
tag: "r_sf"
commit: "d0d51f09ff14d7815dcde6ce01c3796cb41df47a"
version: "bf45f60f1a6ff39ccf2726be9c1eb657"
build_date: "2018-04-20T16:55:26.693Z"
size_mb: 1864
size: 604913695
sif: "https://datasets.datalad.org/shub/arccontainers/recipes/r_sf/2018-04-20-d0d51f09-bf45f60f/bf45f60f1a6ff39ccf2726be9c1eb657.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/arccontainers/recipes/r_sf/2018-04-20-d0d51f09-bf45f60f/
recipe: https://datasets.datalad.org/shub/arccontainers/recipes/r_sf/2018-04-20-d0d51f09-bf45f60f/Singularity
collection: arccontainers/recipes
---

# arccontainers/recipes:r_sf

```bash
$ singularity pull shub://arccontainers/recipes:r_sf
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post

apt-get -y update && apt-get install -y apt-utils

apt-get install -y build-essential

apt-get install -y gfortran
apt-get install -y libopenblas-base
apt-get install -y wget
apt-get install -y ed
apt-get install -y nano
apt-get install -y git-all
apt-get install -y software-properties-common #required for apt-add-repository
apt-get -y update


#Set correct locale for R
apt-get -y update && apt-get install -y locales
locale-gen en_GB.UTF-8
export LANG=en_GB.UTF-8
export LANGUAGE=en_GB.UTF-8
export LC_ALL=en_GB.UTF-8


#Add required libraries for R sf package.
#See vignette: https://cran.r-project.org/web/packages/sf/sf.pdf
#and recommended repo for dependencies- see https://github.com/r-spatial/sf
#sf had problems building against standard repo of these libs

add-apt-repository ppa:ubuntugis/ubuntugis-unstable
apt-get -y update
apt-get install -y libudunits2-dev libgdal-dev libgeos-dev libproj-dev

# Install R
echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a /etc/apt/sources.list
gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9
gpg -a --export E084DAB9 | apt-key add -
apt-get -y update
apt-get -y install r-base r-base-dev

#Install R packages
Rscript -e "install.packages('parallel')"
Rscript -e "install.packages('sp')"
Rscript -e "install.packages('rgeos')"
Rscript -e "install.packages('rgdal')"
Rscript -e "install.packages('raster')"
Rscript -e "install.packages('tidyverse')"
Rscript -e "install.packages('dplyr')"
Rscript -e "install.packages('tidyr')"
Rscript -e "install.packages('tibble')"
Rscript -e "install.packages('readr')"
Rscript -e "install.packages('forcats')"
Rscript -e "install.packages('stringr')"
Rscript -e "install.packages('purrr')"             
Rscript -e "install.packages('ggplot2')"
Rscript -e "install.packages('sf')"

#Set stub /nobackup directory for Singularity

mkdir -p /nobackup
```

## Collection

 - Name: [arccontainers/recipes](https://github.com/arccontainers/recipes)
 - License: None

