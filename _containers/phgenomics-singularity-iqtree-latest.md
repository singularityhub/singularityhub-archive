---
id: 11826
name: "phgenomics-singularity/iqtree"
branch: "master"
tag: "latest"
commit: "2cefa5c1bcfebb01ea26aefbd04419f96302db35"
version: "0effd285efb20bc8f1ddc3db5346ad2f"
build_date: "2020-03-02T23:51:46.044Z"
size_mb: 788.0
size: 260861983
sif: "https://datasets.datalad.org/shub/phgenomics-singularity/iqtree/latest/2020-03-02-2cefa5c1-0effd285/0effd285efb20bc8f1ddc3db5346ad2f.sif"
url: https://datasets.datalad.org/shub/phgenomics-singularity/iqtree/latest/2020-03-02-2cefa5c1-0effd285/
recipe: https://datasets.datalad.org/shub/phgenomics-singularity/iqtree/latest/2020-03-02-2cefa5c1-0effd285/Singularity
collection: phgenomics-singularity/iqtree
---

# phgenomics-singularity/iqtree:latest

```bash
$ singularity pull shub://phgenomics-singularity/iqtree:latest
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
iqtree_version 1.6.12

%environment
export VERSION=1.6.12
export PATH=/opt/conda/bin:$PATH

%post

apt-get update
apt-get -y install locales sudo

export PATH=/opt/conda/bin:$PATH

conda config --add channels conda-forge
conda config --add channels defaults
conda config --add channels r
conda config --add channels bioconda

conda install -c conda-forge -c bioconda iqtree=1.6.12

export LANGUAGE=en_US.UTF-8
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
```

## Collection

 - Name: [phgenomics-singularity/iqtree](https://github.com/phgenomics-singularity/iqtree)
 - License: None

