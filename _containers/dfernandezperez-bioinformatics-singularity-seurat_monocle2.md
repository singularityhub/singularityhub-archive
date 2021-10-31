---
id: 5533
name: "dfernandezperez/bioinformatics-singularity"
branch: "master"
tag: "seurat_monocle2"
commit: "e9d7c85e3e4407372736a8af77e819b4cff9a719"
version: "20a85b874f573f58aa96ca3243718821"
build_date: "2018-11-07T20:20:33.155Z"
size_mb: 3205
size: 1169301535
sif: "https://datasets.datalad.org/shub/dfernandezperez/bioinformatics-singularity/seurat_monocle2/2018-11-07-e9d7c85e-20a85b87/20a85b874f573f58aa96ca3243718821.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dfernandezperez/bioinformatics-singularity/seurat_monocle2/2018-11-07-e9d7c85e-20a85b87/
recipe: https://datasets.datalad.org/shub/dfernandezperez/bioinformatics-singularity/seurat_monocle2/2018-11-07-e9d7c85e-20a85b87/Singularity
collection: dfernandezperez/bioinformatics-singularity
---

# dfernandezperez/bioinformatics-singularity:seurat_monocle2

```bash
$ singularity pull shub://dfernandezperez/bioinformatics-singularity:seurat_monocle2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bioconductor/release_core2

%apprun R
exec R --vanilla "$@"

%apprun Rscript
exec Rscript --vanilla "$@"

%runscript
exec R --vanilla "$@"

%post
apt-get update

# Basic dependencies for Seurat and most R packages
apt-get install -y apt-transport-https apt-utils software-properties-common
apt-get install -y curl wget nano libboost-all-dev libudunits2-dev gawk
apt-get install -y libblas3 libblas-dev liblapack-dev liblapack3 curl
apt-get install -y gcc fort77 aptitude
apt-get install -y g++
apt-get install -y xorg-dev
apt-get install -y libreadline-dev
apt-get install -y gfortran
gfortran --version
apt-get install -y libssl-dev libxml2-dev libpcre3-dev liblzma-dev libbz2-dev libcurl4-openssl-dev 
apt-get install -y libhdf5-dev hdf5-helpers libmariadb-client-lgpl-dev python-pip  python-virtualenv

# Dependencies for rgl package
apt-get install -y xorg libglu1-mesa-dev libx11-dev libfreetype6-dev

# Dependencies for umap and monocle
pip install umap-learn 
pip install louvain

# installing packages from cran
R --slave -e 'install.packages("devtools",repos="https://cran.rstudio.com/")'
R --slave -e 'install.packages("dplyr",repos="https://cran.rstudio.com/")'
R --slave -e 'install.packages("Seurat",repos="https://cran.rstudio.com/")'
R --slave -e 'install.packages("reticulate",repos="https://cran.rstudio.com/")'
R --slave -e 'install.packages("rgl",repos="https://cran.rstudio.com/")'
R --slave -e 'install.packages("shinythemes",repos="https://cran.rstudio.com/")'

# installing from bioc
R --slave -e 'source("https://bioconductor.org/biocLite.R"); biocLite("monocle")'
R --slave -e 'source("https://bioconductor.org/biocLite.R"); biocLite("scran")'
R --slave -e 'source("http://cf.10xgenomics.com/supp/cell-exp/rkit-install-2.0.0.R")'

# Packages from github
R --slave -e 'devtools::install_github("ggjlab/scMCA")'
```

## Collection

 - Name: [dfernandezperez/bioinformatics-singularity](https://github.com/dfernandezperez/bioinformatics-singularity)
 - License: None

