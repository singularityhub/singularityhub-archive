---
id: 6211
name: "rmcolq/Singularity_recipes"
branch: "master"
tag: "nanosimh"
commit: "9ad025c10ab23e5da73a7661f0aff6ffebce2836"
version: "69a5428353c2cd1cdda300f809879ea0"
build_date: "2019-01-31T21:34:12.219Z"
size_mb: 1441
size: 632369183
sif: "https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/nanosimh/2019-01-31-9ad025c1-69a54283/69a5428353c2cd1cdda300f809879ea0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rmcolq/Singularity_recipes/nanosimh/2019-01-31-9ad025c1-69a54283/
recipe: https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/nanosimh/2019-01-31-9ad025c1-69a54283/Singularity
collection: rmcolq/Singularity_recipes
---

# rmcolq/Singularity_recipes:nanosimh

```bash
$ singularity pull shub://rmcolq/Singularity_recipes:nanosimh
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
      openjdk-8-jre \
      libbz2-dev \
      libfreetype6-dev \
      libhts-dev \
      liblzma-dev \
      libncurses5-dev \
      libncursesw5-dev \
      pkg-config \
      python3-dev \
      python3-pip \
      python3-setuptools \
      python3-tk \
      python3-venv \
      samtools \
      tabix \
      vcftools \
      wget \
      zlib1g-dev
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    
    #============================================
    # INSTALL MINIMAP2
    #============================================
    VERSION="2.15"
    wget https://github.com/lh3/minimap2/archive/v"$VERSION".tar.gz
    tar xzf v"$VERSION".tar.gz
    rm v"$VERSION".tar.gz
    cd minimap2-*
    make
    export PATH=$PWD:$PATH
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
    cd ..
    
    #============================================
    # INSTALL NANOSIM
    #============================================
    git clone https://github.com/karel-brinda/nanosim-h
    cd nanosim-h
    python3 setup.py install
```

## Collection

 - Name: [rmcolq/Singularity_recipes](https://github.com/rmcolq/Singularity_recipes)
 - License: None

