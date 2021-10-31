---
id: 11966
name: "motroy/Managing_batch_effects"
branch: "master"
tag: "latest"
commit: "103c4d8da760d0f088ef7b4cf237c68115504750"
version: "573e8f51cfbd16a28747babb14ac04d9"
build_date: "2020-01-15T12:08:41.549Z"
size_mb: 2227.0
size: 866693151
sif: "https://datasets.datalad.org/shub/motroy/Managing_batch_effects/latest/2020-01-15-103c4d8d-573e8f51/573e8f51cfbd16a28747babb14ac04d9.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/motroy/Managing_batch_effects/latest/2020-01-15-103c4d8d-573e8f51/
recipe: https://datasets.datalad.org/shub/motroy/Managing_batch_effects/latest/2020-01-15-103c4d8d-573e8f51/Singularity
collection: motroy/Managing_batch_effects
---

# motroy/Managing_batch_effects:latest

```bash
$ singularity pull shub://motroy/Managing_batch_effects:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: r-base:3.5.3

%post
apt update && apt install -y git curl wget less locate build-essential openssh-server apt-transport-https software-properties-common libssl-dev libcurl4-openssl-dev libmagick++-dev libgmp-dev

wget https://cran.r-project.org/src/contrib/Archive/glmnet/glmnet_2.0-18.tar.gz
wget https://cran.r-project.org/src/contrib/Archive/latticeExtra/latticeExtra_0.6-28.tar.gz
R Rscript -e 'install.packages("knitr")'
R Rscript -e 'install.packages("xtable")'
R Rscript -e 'install.packages("ggplot2")'
R Rscript -e 'install.packages("vegan")'
R Rscript -e 'install.packages("cluster")'
R Rscript -e 'install.packages("gridExtra")'
R Rscript -e 'install.packages("pheatmap")'
R Rscript -e 'install.packages("ruv")'
R Rscript -e 'install.packages("lmerTest")'
R Rscript -e 'install.packages("glmnet_2.0-18.tar.gz",type="source")'
R Rscript -e 'install.packages("foreach")'
R Rscript -e 'install.packages("glmnet_2.0-18.tar.gz",type="source")'
R Rscript -e 'install.packages("latticeExtra_0.6-28.tar.gz",type="source")'
R Rscript -e 'install.packages("BiocManager")'
R Rscript -e 'BiocManager::install("sva")'
R Rscript -e 'BiocManager::install("limma")'
R Rscript -e 'BiocManager::install("variancePartition")'
R Rscript -e 'BiocManager::install("pvca")'
R Rscript -e 'BiocManager::install("mixOmics")'
R Rscript -e 'BiocManager::install("AgiMicroRna")'
R Rscript -e 'BiocManager::install("bapred")'
R Rscript -e 'BiocManager::install("phyloseq")'
```

## Collection

 - Name: [motroy/Managing_batch_effects](https://github.com/motroy/Managing_batch_effects)
 - License: None

