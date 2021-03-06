---
id: 5224
name: "dfernandezperez/bioinformatics-singularity"
branch: "master"
tag: "seurat_monocle"
commit: "d4e3b4e25f7c08cab8893765cec95a90de8aadb0"
version: "9d46e73cee84799fde760136c530c062"
build_date: "2019-01-17T07:32:53.415Z"
size_mb: 3699
size: 1376768031
sif: "https://datasets.datalad.org/shub/dfernandezperez/bioinformatics-singularity/seurat_monocle/2019-01-17-d4e3b4e2-9d46e73c/9d46e73cee84799fde760136c530c062.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dfernandezperez/bioinformatics-singularity/seurat_monocle/2019-01-17-d4e3b4e2-9d46e73c/
recipe: https://datasets.datalad.org/shub/dfernandezperez/bioinformatics-singularity/seurat_monocle/2019-01-17-d4e3b4e2-9d46e73c/Singularity
collection: dfernandezperez/bioinformatics-singularity
---

# dfernandezperez/bioinformatics-singularity:seurat_monocle

```bash
$ singularity pull shub://dfernandezperez/bioinformatics-singularity:seurat_monocle
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
apt-get install -y libhdf5-dev hdf5-helpers libmariadb-client-lgpl-dev python3-pip python-pip  python-virtualenv

# Dependencies for rgl package
apt-get install -y xorg libglu1-mesa-dev libx11-dev libfreetype6-dev

# Dependencies for umap, monocle, phate (included into Seurat) and Magic.
pip install umap-learn 
pip install louvain
pip3 install phate
pip3 install magic-impute

# Install Rstudio
#apt-get install gdebi-core
#wget https://download1.rstudio.org/rstudio-xenial-1.1.463-amd64.deb
#gdebi rstudio-xenial-1.1.463-amd64.deb
#rm rstudio-xenial-1.1.463-amd64.deb

# installing packages from cran
R --slave -e 'install.packages("devtools",repos="https://cran.rstudio.com/")'
R --slave -e 'install.packages("dplyr",repos="https://cran.rstudio.com/")'
R --slave -e 'install.packages("Seurat",repos="https://cran.rstudio.com/")'
R --slave -e 'install.packages("reticulate",repos="https://cran.rstudio.com/")'
R --slave -e 'install.packages("rgl",repos="https://cran.rstudio.com/")'
R --slave -e 'install.packages("shinythemes",repos="https://cran.rstudio.com/")'
R --slave -e 'install.packages("phateR",repos="https://cran.rstudio.com/")'
R --slave -e 'install.packages("Rmagic",repos="https://cran.rstudio.com/")'

# installing from bioc
R --slave -e 'source("https://bioconductor.org/biocLite.R"); biocLite("monocle")'
R --slave -e 'source("https://bioconductor.org/biocLite.R"); biocLite("scran")'
R --slave -e 'source("https://bioconductor.org/biocLite.R"); biocLite("destiny")'

# installing from github
R --slave -e 'devtools::install_github("ggjlab/scMCA")'
R --slave -e 'source("http://cf.10xgenomics.com/supp/cell-exp/rkit-install-2.0.0.R")'

# Some monocle3 dependencies
R --slave -e 'devtools::install_github("cole-trapnell-lab/DDRTree", ref="simple-ppt-like")'
R --slave -e 'devtools::install_github("cole-trapnell-lab/L1-graph")'
R --slave -e 'source("https://bioconductor.org/biocLite.R"); biocLite("DelayedMatrixStats")'
R --slave -e 'install.packages(c("spdep", "glmnet", "doParallel", "pbmcapply"))'
R --slave -e 'library(monocle);devtools::install_github("cole-trapnell-lab/monocle-release", ref="monocle3_alpha", dependencies = FALSE)'
```

## Collection

 - Name: [dfernandezperez/bioinformatics-singularity](https://github.com/dfernandezperez/bioinformatics-singularity)
 - License: None

