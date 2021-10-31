---
id: 9339
name: "motroy/singularity-R-fastbaps"
branch: "master"
tag: "bkup"
commit: "9cb9c0447014641be0973d45d24f16b58f9d6318"
version: "b2a102b118955a1279f18fc27ad5e6c3"
build_date: "2019-05-27T02:23:41.864Z"
size_mb: 1246
size: 430542879
sif: "https://datasets.datalad.org/shub/motroy/singularity-R-fastbaps/bkup/2019-05-27-9cb9c044-b2a102b1/b2a102b118955a1279f18fc27ad5e6c3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/motroy/singularity-R-fastbaps/bkup/2019-05-27-9cb9c044-b2a102b1/
recipe: https://datasets.datalad.org/shub/motroy/singularity-R-fastbaps/bkup/2019-05-27-9cb9c044-b2a102b1/Singularity
collection: motroy/singularity-R-fastbaps
---

# motroy/singularity-R-fastbaps:bkup

```bash
$ singularity pull shub://motroy/singularity-R-fastbaps:bkup
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
apt update && apt install -y git curl wget less locate build-essential openssh-server apt-transport-https software-properties-common libssl-dev libcurl4-openssl-dev libmagick++-dev
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
```

## Collection

 - Name: [motroy/singularity-R-fastbaps](https://github.com/motroy/singularity-R-fastbaps)
 - License: [MIT License](https://api.github.com/licenses/mit)

