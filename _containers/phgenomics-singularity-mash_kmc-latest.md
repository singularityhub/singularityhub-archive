---
id: 11828
name: "phgenomics-singularity/mash_kmc"
branch: "master"
tag: "latest"
commit: "b16b98e30143a0f7dba6e2f791be323d2dbdbd91"
version: "88c231cbc4c8a4d19f6206e4d3a24c86"
build_date: "2020-02-18T00:00:09.228Z"
size_mb: 912.0
size: 311578655
sif: "https://datasets.datalad.org/shub/phgenomics-singularity/mash_kmc/latest/2020-02-18-b16b98e3-88c231cb/88c231cbc4c8a4d19f6206e4d3a24c86.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/phgenomics-singularity/mash_kmc/latest/2020-02-18-b16b98e3-88c231cb/
recipe: https://datasets.datalad.org/shub/phgenomics-singularity/mash_kmc/latest/2020-02-18-b16b98e3-88c231cb/Singularity
collection: phgenomics-singularity/mash_kmc
---

# phgenomics-singularity/mash_kmc:latest

```bash
$ singularity pull shub://phgenomics-singularity/mash_kmc:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.5.12

%help
A Singularity image for name

%labels
Maintainer Kristy Horan
Build 1.0
genome size tools

%environment
export VERSION=
export PATH=/opt/conda/bin:$PATH

%post
 # set versions of software to install
  export MASH_VERSION=2.2.2
  export KMC_VERSION=3.1.1

  export PATH=/opt/conda/bin:$PATH

  conda config --add channels conda-forge
  conda config --add channels defaults
  conda config --add channels r
  conda config --add channels bioconda
 
  conda install -c bioconda mash=${MASH_VERSION}
  conda install -c bioconda kmc=${KMC_VERSION}

  pip install toml

  echo "Done!"
```

## Collection

 - Name: [phgenomics-singularity/mash_kmc](https://github.com/phgenomics-singularity/mash_kmc)
 - License: None

