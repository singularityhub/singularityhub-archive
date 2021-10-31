---
id: 14017
name: "ResearchComputing/rstudiojh2"
branch: "master"
tag: "latest"
commit: "6f08ac690dde52bade423101318abe4ee15a0660"
version: "f7978e5b1ddc1d045eb5dd561290343b"
build_date: "2020-08-23T23:56:31.053Z"
size_mb: 6813.0
size: 2467934239
sif: "https://datasets.datalad.org/shub/ResearchComputing/rstudiojh2/latest/2020-08-23-6f08ac69-f7978e5b/f7978e5b1ddc1d045eb5dd561290343b.sif"
url: https://datasets.datalad.org/shub/ResearchComputing/rstudiojh2/latest/2020-08-23-6f08ac69-f7978e5b/
recipe: https://datasets.datalad.org/shub/ResearchComputing/rstudiojh2/latest/2020-08-23-6f08ac69-f7978e5b/Singularity
collection: ResearchComputing/rstudiojh2
---

# ResearchComputing/rstudiojh2:latest

```bash
$ singularity pull shub://ResearchComputing/rstudiojh2:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:jupyter/r-notebook:29e069665f5f

%files

%post

export PATH=/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/rstudio/bin:/usr/lib/rstudio-server/bin

apt-get update -y
apt-get upgrade -y --no-install-recommends
apt-get install -y --no-install-recommends libcairo2-dev libpq-dev r-cran-rcpp


conda install --yes --quiet -c conda-forge nbgitpuller nbrsessionproxy jupyter-rsession-proxy openjdk r-webp gdal tesseract leptonica
rm -rf /opt/conda/pkgs/*.bz2

jupyter serverextension enable --py nbgitpuller --sys-prefix


cd  /opt
wget https://download2.rstudio.org/server/bionic/amd64/rstudio-server-1.2.5033-amd64.deb
apt-get install -y --no-install-recommends /opt/rstudio-server-1.2.5033-amd64.deb
rm /opt/*.deb

PATH=$PATH:/usr/lib/rstudio-server/bin
JAVA_HOME=/opt/conda/pkgs/openjdk-11.0.1-h600c080_1018
PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/opt/conda/lib/pkgconfig
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$JAVA_HOME/lib:$JAVA_HOME/lib/server

R --vanilla CMD javareconf


R --vanilla -e "install.packages('rJava',dependencies=TRUE, repos='http://cran.rstudio.com/')" 
R --vanilla -e "install.packages('gutenbergr',dependencies=TRUE, repos='http://cran.rstudio.com/')" 
R --vanilla -e "install.packages('RcppParallel',dependencies=TRUE, repos='http://cran.rstudio.com/')" 
R --vanilla -e "install.packages('tidytext',dependencies=TRUE, repos='http://cran.rstudio.com/')"
R --vanilla -e "install.packages('textdata',dependencies=TRUE, repos='http://cran.rstudio.com/')" 
R --vanilla -e "install.packages('widyr',dependencies=TRUE, repos='http://cran.rstudio.com/')" 
R --vanilla -e "install.packages('pdftools',dependencies=TRUE, repos='http://cran.rstudio.com/')" 
R --vanilla -e "install.packages('ggpubr',dependencies=TRUE, repos='http://cran.rstudio.com/')"
R --vanilla -e "install.packages('tm',dependencies=TRUE, repos='http://cran.rstudio.com/')"
R --vanilla -e "install.packages('eply',dependencies=TRUE, repos='http://cran.rstudio.com/')"

R --vanilla -e "install.packages('caTools',dependencies=TRUE, repos='http://cran.rstudio.com/')"
R --vanilla -e "install.packages('latex2exp',dependencies=TRUE, repos='http://cran.rstudio.com/')"
R --vanilla -e "install.packages('plotly',dependencies=TRUE, repos='http://cran.rstudio.com/')"
R --vanilla -e "install.packages('testthat',dependencies=TRUE, repos='http://cran.rstudio.com/')"
R --vanilla -e "install.packages('swirl',dependencies=TRUE, repos='http://cran.rstudio.com/')"
R --vanilla -e "install.packages('deSolve',dependencies=TRUE, repos='http://cran.rstudio.com/')"

apt-get clean
rm -rf /var/lib/apt/lists/*
rm -rf /tmp/*

%environment

export PATH=/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/rstudio/bin:/usr/lib/rstudio-server/bin
export JAVA_HOME=/opt/conda/pkgs/openjdk-11.0.1-h600c080_1018
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$JAVA_HOME/lib:$JAVA_HOME/lib/server
export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/opt/conda/lib/pkgconfig
```

## Collection

 - Name: [ResearchComputing/rstudiojh2](https://github.com/ResearchComputing/rstudiojh2)
 - License: None

