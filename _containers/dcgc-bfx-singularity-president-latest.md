---
id: 15782
name: "dcgc-bfx/singularity-president"
branch: "main"
tag: "latest"
commit: "9ea39aedd66d4349617a4a13cee7b85c5fdaec24"
version: "b8ef3e157c074e3a4572142794ba0db40e9b5233224e0bf762526d6d81386642"
build_date: "2021-03-22T12:34:53.167Z"
size_mb: 215.60546875
size: 226078720
sif: "https://datasets.datalad.org/shub/dcgc-bfx/singularity-president/latest/2021-03-22-9ea39aed-b8ef3e15/b8ef3e157c074e3a4572142794ba0db40e9b5233224e0bf762526d6d81386642.sif"
url: https://datasets.datalad.org/shub/dcgc-bfx/singularity-president/latest/2021-03-22-9ea39aed-b8ef3e15/
recipe: https://datasets.datalad.org/shub/dcgc-bfx/singularity-president/latest/2021-03-22-9ea39aed-b8ef3e15/Singularity
collection: dcgc-bfx/singularity-president
---

# dcgc-bfx/singularity-president:latest

```bash
$ singularity pull shub://dcgc-bfx/singularity-president:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:latest

%labels
    Author fabian.rost@tu-dresden.de
    Organisation DcGC
    Version v0.1

%help
    Base container based on conda docker container with basic python and R
    packages installed.

%environment
  DEBIAN_FRONTEND=noninteractive

%post
  export PATH=/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

  conda update --quiet --yes conda
  conda config --add channels defaults
  conda config --add channels bioconda
  conda config --add channels conda-forge

  conda install --quiet --yes mamba

  mamba update --quiet --yes --all

  mamba install --quiet --yes president

  mamba clean --quiet --yes --all

%runscript
  president "${@}"
```

## Collection

 - Name: [dcgc-bfx/singularity-president](https://github.com/dcgc-bfx/singularity-president)
 - License: None

