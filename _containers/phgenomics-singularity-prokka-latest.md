---
id: 10397
name: "phgenomics-singularity/prokka"
branch: "master"
tag: "latest"
commit: "0dfd1f88f08a0076b4c679318b6e29298e92e745"
version: "bb32f2b56bc23adc224e53b0c46a1378"
build_date: "2020-04-22T22:43:09.248Z"
size_mb: 3175.0
size: 1523933215
sif: "https://datasets.datalad.org/shub/phgenomics-singularity/prokka/latest/2020-04-22-0dfd1f88-bb32f2b5/bb32f2b56bc23adc224e53b0c46a1378.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/phgenomics-singularity/prokka/latest/2020-04-22-0dfd1f88-bb32f2b5/
recipe: https://datasets.datalad.org/shub/phgenomics-singularity/prokka/latest/2020-04-22-0dfd1f88-bb32f2b5/Singularity
collection: phgenomics-singularity/prokka
---

# phgenomics-singularity/prokka:latest

```bash
$ singularity pull shub://phgenomics-singularity/prokka:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.5.12

%help
A Singularity image for Prokka

%labels
Maintainer Kristy Horan
Build 1.0
Genome annotation with Prokka

%environment
export VERSION=1.0
export PATH=/opt/conda/bin:$PATH

%post

export PATH=/opt/conda/bin:$PATH

conda config --add channels conda-forge
conda config --add channels defaults
conda config --add channels r
conda config --add channels bioconda

conda install -c conda-forge -c bioconda prokka
```

## Collection

 - Name: [phgenomics-singularity/prokka](https://github.com/phgenomics-singularity/prokka)
 - License: None

