---
id: 11830
name: "phgenomics-singularity/roary"
branch: "master"
tag: "latest"
commit: "8d20b89f865321c35a9ec349fb445ff549046d82"
version: "e960263221fe745113ec4d7ec5728cbc"
build_date: "2020-05-30T04:44:20.647Z"
size_mb: 2185.0
size: 875601951
sif: "https://datasets.datalad.org/shub/phgenomics-singularity/roary/latest/2020-05-30-8d20b89f-e9602632/e960263221fe745113ec4d7ec5728cbc.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/phgenomics-singularity/roary/latest/2020-05-30-8d20b89f-e9602632/
recipe: https://datasets.datalad.org/shub/phgenomics-singularity/roary/latest/2020-05-30-8d20b89f-e9602632/Singularity
collection: phgenomics-singularity/roary
---

# phgenomics-singularity/roary:latest

```bash
$ singularity pull shub://phgenomics-singularity/roary:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.5.12

%help
A Singularity image for Roary

%labels
Maintainer Kristy Horan
Build 1.0
Genome annotation with Roary

%environment
export VERSION=3.13.0
export PATH=/opt/conda/bin:$PATH

%post

export PATH=/opt/conda/bin:$PATH

conda upgrade -c defaults --override-channels conda
conda config --add channels conda-forge
conda config --add channels defaults
conda config --add channels r
conda config --add channels bioconda

conda install -c conda-forge -c bioconda roary=3.13.0
```

## Collection

 - Name: [phgenomics-singularity/roary](https://github.com/phgenomics-singularity/roary)
 - License: None

