---
id: 7182
name: "pmitev/Teoroo-singularity"
branch: "master"
tag: "gromacs"
commit: "c17db735f1781c563784cb2cc53b8128af8bf374"
version: "10ab4acbe2c785d1cbe6e41269aacacd"
build_date: "2019-09-23T12:41:15.994Z"
size_mb: 439
size: 154562591
sif: "https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/gromacs/2019-09-23-c17db735-10ab4acb/10ab4acbe2c785d1cbe6e41269aacacd.simg"
url: https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/gromacs/2019-09-23-c17db735-10ab4acb/
recipe: https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/gromacs/2019-09-23-c17db735-10ab4acb/Singularity
collection: pmitev/Teoroo-singularity
---

# pmitev/Teoroo-singularity:gromacs

```bash
$ singularity pull shub://pmitev/Teoroo-singularity:gromacs
```

## Singularity Recipe

```singularity
Bootstrap:  docker
From: ubuntu:18.04

%runscript
  export PATH=/usr/local/bin:$PATH
  export XDG_RUNTIME_DIR=/tmp/.run_$(uuidgen)
  /bin/bash

%setup
  

%files

%environment
  export PYTHONNOUSERSITE=True

%labels
  AUTHOR pavlin.mitev@kemi.uu.se

%post
  apt-get update && apt-get install -y \
    bash-completion \
    bc \
    curl \
    gawk \
    git \
    htop \
    locales \
    lsof \
    mc \
    ncdu \
    rsh-client \
    openssh-client \
    units \
    uuid-runtime \
    vim \
    wget \
    gromacs gromacs-openmpi \
&& rm -rf /var/lib/apt/lists/*

  locale-gen en_US.UTF-8 &&  update-locale
```

## Collection

 - Name: [pmitev/Teoroo-singularity](https://github.com/pmitev/Teoroo-singularity)
 - License: None

