---
id: 14382
name: "kavonrtep/SeqGrapheR"
branch: "master"
tag: "latest"
commit: "4c828754e2c2f9c97978f20abbbe816d7baba32f"
version: "256141241986c653d4cb04b3f6a97619"
build_date: "2021-04-13T15:53:41.511Z"
size_mb: 1919.0
size: 705200159
sif: "https://datasets.datalad.org/shub/kavonrtep/SeqGrapheR/latest/2021-04-13-4c828754-25614124/256141241986c653d4cb04b3f6a97619.sif"
url: https://datasets.datalad.org/shub/kavonrtep/SeqGrapheR/latest/2021-04-13-4c828754-25614124/
recipe: https://datasets.datalad.org/shub/kavonrtep/SeqGrapheR/latest/2021-04-13-4c828754-25614124/Singularity
collection: kavonrtep/SeqGrapheR
---

# kavonrtep/SeqGrapheR:latest

```bash
$ singularity pull shub://kavonrtep/SeqGrapheR:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04
%files
    ./R_install.R  /opt/R_install.R
    ./SeqGrapheR   /usr/local/bin/SeqGrapheR

%post
    export DEBIAN_FRONTEND=noninteractive
    apt-get -y update
    apt-get -y install ncbi-blast+-legacy acedb-other-dotter staden ggobi
    apt-get -y install r-base libcurl4-openssl-dev libxml2-dev libgtk2.0-dev libssl-dev
    apt-get -y install build-essential gfortran libblas-dev liblapack-dev r-cran-future
    apt-get -y install r-bioc-biostrings r-cran-rggobi r-cran-gwidgets r-cran-gwidgetsrgtk2
    apt-get -y install r-cran-devtools r-cran-cairodevice r-cran-igraph
    apt-get -y install libatk-adaptor 
    Rscript /opt/R_install.R
    

%environment
    export LC_ALL=C
    export PATH=/usr/games:$PATH
    export NO_AT_BRIDGE=1

%runscript
    SeqGrapheR
%labels
    Author petr@umbr.cas.cz
    Version v0.0.1
```

## Collection

 - Name: [kavonrtep/SeqGrapheR](https://github.com/kavonrtep/SeqGrapheR)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

