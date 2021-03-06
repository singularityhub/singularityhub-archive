---
id: 3363
name: "mikemhenry/cme-lab-images"
branch: "master"
tag: "base"
commit: "f510d17b5d0321d152d1bd562734ecd0ec9df2e9"
version: "b545442d332e079e6c288d1048318061"
build_date: "2018-07-02T22:28:01.278Z"
size_mb: 385
size: 183648287
sif: "https://datasets.datalad.org/shub/mikemhenry/cme-lab-images/base/2018-07-02-f510d17b-b545442d/b545442d332e079e6c288d1048318061.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mikemhenry/cme-lab-images/base/2018-07-02-f510d17b-b545442d/
recipe: https://datasets.datalad.org/shub/mikemhenry/cme-lab-images/base/2018-07-02-f510d17b-b545442d/Singularity
collection: mikemhenry/cme-lab-images
---

# mikemhenry/cme-lab-images:base

```bash
$ singularity pull shub://mikemhenry/cme-lab-images:base
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
Base image used in CME-Lab workflows.
This image sets up conda/python

http://coen.boisestate.edu/cmelab/

%setup

%files

%labels
  Maintainer Mike Henry
  Maintainer_Email mikehenry@boisestate.edu
  Version v0.01

%environment
  CONDA_DIR="/opt/conda"
  PATH="$CONDA_DIR/bin:$PATH"
  
  export PATH  

%post
  # Build envs
  CONDA_VERSION="4.5.4"
  CONDA_DIR="/opt/conda"
  CONDA_MD5_CHECKSUM="a946ea1d0c4a642ddf0c3a26a18bb16d"

  # conda deps
  apt update
  apt install --no-install-recommends -y wget tar ca-certificates bzip2
  apt clean
  rm -rf /var/lib/apt/lists/*
  
  # install conda
  mkdir -p "$CONDA_DIR"
  wget "http://repo.continuum.io/miniconda/Miniconda3-${CONDA_VERSION}-Linux-x86_64.sh" -O miniconda.sh
  echo "$CONDA_MD5_CHECKSUM  miniconda.sh" | md5sum -c
  bash miniconda.sh -f -b -p "$CONDA_DIR"
  echo "export PATH=$CONDA_DIR/bin:\$PATH" > /etc/profile.d/conda.sh
  rm miniconda.sh

%runscript

%test
 CONDA_DIR="/opt/conda"
 PATH="$CONDA_DIR/bin:$PATH"
 command -v conda
 command -v python
 conda list
```

## Collection

 - Name: [mikemhenry/cme-lab-images](https://github.com/mikemhenry/cme-lab-images)
 - License: None

