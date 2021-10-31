---
id: 6506
name: "rmcolq/Singularity_recipes"
branch: "master"
tag: "alignqc"
commit: "b1354460f4366050da43834f1776d57b78b2d02b"
version: "017ffdeaaaf0e14dae0561c13f385b59"
build_date: "2020-03-23T19:00:37.470Z"
size_mb: 1555
size: 759791647
sif: "https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/alignqc/2020-03-23-b1354460-017ffdea/017ffdeaaaf0e14dae0561c13f385b59.simg"
url: https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/alignqc/2020-03-23-b1354460-017ffdea/
recipe: https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/alignqc/2020-03-23-b1354460-017ffdea/Singularity
collection: rmcolq/Singularity_recipes
---

# rmcolq/Singularity_recipes:alignqc

```bash
$ singularity pull shub://rmcolq/Singularity_recipes:alignqc
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%help
  A container to hold the read simulator nanosim.
  Run `singularity exec nanosim.simg nanosim`

%environment
  PATH=/usr/local/bin:$PATH

%post
    apt-get update
    apt-get install -y --no-install-recommends apt-utils
    apt-get update
    apt-get install -y software-properties-common
    apt-add-repository universe
    apt-get update
    apt-get install -y \
      automake \
      build-essential \
      cmake \
      git \
      gnuplot \
      graphviz \
      libbz2-dev \
      libfreetype6-dev \
      libhts-dev \
      liblzma-dev \
      libncurses5-dev \
      libncursesw5-dev \
      pkg-config \
      python-dev \
      python-pip \
      python-setuptools \
      r-base \
      samtools \
      vim \
      wget \
      zlib1g-dev
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT

    #================================
    # INSTALL ALIGNQC
    #================================
    pip install seq-tools==1.0.10
    pip install AlignQC==2.0.5
```

## Collection

 - Name: [rmcolq/Singularity_recipes](https://github.com/rmcolq/Singularity_recipes)
 - License: None

