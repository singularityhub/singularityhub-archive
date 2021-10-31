---
id: 10379
name: "phgenomics-singularity/snippy"
branch: "master"
tag: "latest"
commit: "61c2c44829af4e1907d63557ec18cb8e0a96513f"
version: "d7c8521b20f68c3453811a9a85511b4f"
build_date: "2020-03-02T23:51:43.945Z"
size_mb: 3357.0
size: 1422536735
sif: "https://datasets.datalad.org/shub/phgenomics-singularity/snippy/latest/2020-03-02-61c2c448-d7c8521b/d7c8521b20f68c3453811a9a85511b4f.sif"
url: https://datasets.datalad.org/shub/phgenomics-singularity/snippy/latest/2020-03-02-61c2c448-d7c8521b/
recipe: https://datasets.datalad.org/shub/phgenomics-singularity/snippy/latest/2020-03-02-61c2c448-d7c8521b/Singularity
collection: phgenomics-singularity/snippy
---

# phgenomics-singularity/snippy:latest

```bash
$ singularity pull shub://phgenomics-singularity/snippy:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.5.12

%help
A Singularity image for Snippy

%labels
Maintainer Kristy Horan
Build 1.0
snippy_version 4.4.5

%environment
export VERSION=1.0
export PATH=/opt/conda/bin:$PATH

%post

apt-get update
apt-get -y install locales sudo

export PATH=/opt/conda/bin:$PATH
conda upgrade -c defaults --override-channels conda
conda config --add channels conda-forge
conda config --add channels defaults
conda config --add channels r
conda config --add channels bioconda

conda install -c conda-forge -c bioconda snippy=4.4.5
conda install -c conda-forge -c bioconda snp-dists=0.6.3
conda install -c bioconda samtools=1.9

export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
```

## Collection

 - Name: [phgenomics-singularity/snippy](https://github.com/phgenomics-singularity/snippy)
 - License: None

