---
id: 15783
name: "dcgc-bfx/singularity-president"
branch: "main"
tag: "0.6.0"
commit: "bd55d167bce9ef92424c284650bd62bd46a8434e"
version: "63a3f99208418ba390e601f943e7337ffd0e885df11808ec11d65a6ff52d0447"
build_date: "2021-03-22T12:27:54.625Z"
size_mb: 215.60546875
size: 226078720
sif: "https://datasets.datalad.org/shub/dcgc-bfx/singularity-president/0.6.0/2021-03-22-bd55d167-63a3f992/63a3f99208418ba390e601f943e7337ffd0e885df11808ec11d65a6ff52d0447.sif"
url: https://datasets.datalad.org/shub/dcgc-bfx/singularity-president/0.6.0/2021-03-22-bd55d167-63a3f992/
recipe: https://datasets.datalad.org/shub/dcgc-bfx/singularity-president/0.6.0/2021-03-22-bd55d167-63a3f992/Singularity
collection: dcgc-bfx/singularity-president
---

# dcgc-bfx/singularity-president:0.6.0

```bash
$ singularity pull shub://dcgc-bfx/singularity-president:0.6.0
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

  mamba install --quiet --yes president=0.6.0

  mamba clean --quiet --yes --all

%runscript
  president "${@}"
```

## Collection

 - Name: [dcgc-bfx/singularity-president](https://github.com/dcgc-bfx/singularity-president)
 - License: None

