---
id: 9338
name: "motroy/singularity-R-fastbaps"
branch: "master"
tag: "latest"
commit: "b2d5afad6f8d775c280c91b48adb1d376fe71bec"
version: "d4065477e7427a655dcef29bee807d22"
build_date: "2019-05-27T02:23:41.859Z"
size_mb: 1283
size: 447926303
sif: "https://datasets.datalad.org/shub/motroy/singularity-R-fastbaps/latest/2019-05-27-b2d5afad-d4065477/d4065477e7427a655dcef29bee807d22.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/motroy/singularity-R-fastbaps/latest/2019-05-27-b2d5afad-d4065477/
recipe: https://datasets.datalad.org/shub/motroy/singularity-R-fastbaps/latest/2019-05-27-b2d5afad-d4065477/Singularity
collection: motroy/singularity-R-fastbaps
---

# motroy/singularity-R-fastbaps:latest

```bash
$ singularity pull shub://motroy/singularity-R-fastbaps:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%environment
export PATH="/miniconda/miniconda3/bin:$PATH"
export CONDARC=/.condarc

%post
export CONDARC=/.condarc
mkdir /miniconda && cd /miniconda
apt update && apt install -y git curl wget less locate build-essential openssh-server apt-transport-https software-properties-common libssl-dev libcurl4-openssl-dev libmagick++-dev libgmp-dev
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'
apt update && apt install -y r-base
#wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
#chmod +x Miniconda3-latest-Linux-x86_64.sh
#./Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda/miniconda3
#/miniconda/miniconda3/bin/conda update -n base conda && /miniconda/miniconda3/bin/conda config --set show_channel_urls True
#/miniconda/miniconda3/bin/conda config --file /.condarc --add channels defaults && /miniconda/miniconda3/bin/conda config --file /.condarc --add channels https://www.idiap.ch/software/bob/conda
#/miniconda/miniconda3/bin/conda install gridtk
R Rscript -e 'install.packages("ggplot2")'
R Rscript -e 'install.packages("devtools")'
R Rscript -e 'library("devtools"); install_github("gtonkinhill/fastbaps")'
R Rscript -e 'install.packages("ape")'
R Rscript -e 'install.packages("BiocManager");BiocManager::install("ggtree")'
R Rscript -e 'install.packages("phytools")'

R Rscript -e 'install.packages("rhierbaps")'
R Rscript -e 'install.packages("data.table")'
R Rscript -e 'install.packages("patchwork")'
R Rscript -e 'install.packages("stringr")'
R Rscript -e 'install.packages("dplyr")'
R Rscript -e 'install.packages("Matrix")'
R Rscript -e 'install.packages("ggbeeswarm")'
R Rscript -e 'install.packages("gplots")'
```

## Collection

 - Name: [motroy/singularity-R-fastbaps](https://github.com/motroy/singularity-R-fastbaps)
 - License: [MIT License](https://api.github.com/licenses/mit)

