---
id: 11827
name: "phgenomics-singularity/assemblers"
branch: "master"
tag: "latest"
commit: "83cfadb88e516299055552811c2d33b91b04d081"
version: "7b787f1da0db706e77ed27d14d3ce183"
build_date: "2020-02-18T00:00:14.368Z"
size_mb: 1997.0
size: 738373663
sif: "https://datasets.datalad.org/shub/phgenomics-singularity/assemblers/latest/2020-02-18-83cfadb8-7b787f1d/7b787f1da0db706e77ed27d14d3ce183.sif"
url: https://datasets.datalad.org/shub/phgenomics-singularity/assemblers/latest/2020-02-18-83cfadb8-7b787f1d/
recipe: https://datasets.datalad.org/shub/phgenomics-singularity/assemblers/latest/2020-02-18-83cfadb8-7b787f1d/Singularity
collection: phgenomics-singularity/assemblers
---

# phgenomics-singularity/assemblers:latest

```bash
$ singularity pull shub://phgenomics-singularity/assemblers:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.5.12

%help
A Singularity image for assemblers

%labels
Maintainer Kristy Horan
Build 1.0
assemblers

%environment
export VERSION=1.0

%post
 # set versions of software to install
  export VERSION=1.0
  export SPADES_VERSION=3.13.0
  export SHOVILL_VERSION=1.0.9
  export SKESA_VERSION=2.3.0
  
  export PATH=/opt/conda/bin:PATH
  conda upgrade -c defaults --override-channels conda
  conda config --add channels conda-forge
  conda config --add channels defaults
  conda config --add channels r
  conda config --add channels bioconda
 
  conda install -c bioconda spades=${SPADES_VERSION}
  conda install -c bioconda shovill=${SHOVILL_VERSION}
  conda install -c bioconda skesa=${SKESA_VERSION}

  pip install toml
  pip install biopython
  
  echo "Done"
```

## Collection

 - Name: [phgenomics-singularity/assemblers](https://github.com/phgenomics-singularity/assemblers)
 - License: None

