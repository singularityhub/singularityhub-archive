---
id: 11824
name: "phgenomics-singularity/seqtk"
branch: "master"
tag: "latest"
commit: "d1f218cfe56ea6857266c86145a63c2584fde418"
version: "44e3d5596226706ce18a6513d180eeb3"
build_date: "2020-02-12T05:12:02.871Z"
size_mb: 897.0
size: 300245023
sif: "https://datasets.datalad.org/shub/phgenomics-singularity/seqtk/latest/2020-02-12-d1f218cf-44e3d559/44e3d5596226706ce18a6513d180eeb3.sif"
url: https://datasets.datalad.org/shub/phgenomics-singularity/seqtk/latest/2020-02-12-d1f218cf-44e3d559/
recipe: https://datasets.datalad.org/shub/phgenomics-singularity/seqtk/latest/2020-02-12-d1f218cf-44e3d559/Singularity
collection: phgenomics-singularity/seqtk
---

# phgenomics-singularity/seqtk:latest

```bash
$ singularity pull shub://phgenomics-singularity/seqtk:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.5.12

%help
A Singularity image for seqtk

%labels
Maintainer Kristy Horan
Build 1.0
seqtk version-1.3

%environment

%files


%post
  export SEQTK_VERSION=1.3
  
  export PATH=/opt/conda/bin:$PATH

  conda config --add channels conda-forge
  conda config --add channels defaults
  conda config --add channels r
  conda config --add channels bioconda

  conda install -c bioconda seqtk=${SEQTK_VERSION}
  pip install pandas
  pip install toml
  
  echo "Done"
```

## Collection

 - Name: [phgenomics-singularity/seqtk](https://github.com/phgenomics-singularity/seqtk)
 - License: None

