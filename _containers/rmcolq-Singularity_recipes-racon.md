---
id: 3635
name: "rmcolq/Singularity_recipes"
branch: "master"
tag: "racon"
commit: "2426fcf36d8426c0195223d88f045590d35bf59a"
version: "d443f5a9c83a45070233be77e1cc19dc"
build_date: "2018-08-08T03:56:31.872Z"
size_mb: 1207
size: 522330143
sif: "https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/racon/2018-08-08-2426fcf3-d443f5a9/d443f5a9c83a45070233be77e1cc19dc.simg"
url: https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/racon/2018-08-08-2426fcf3-d443f5a9/
recipe: https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/racon/2018-08-08-2426fcf3-d443f5a9/Singularity
collection: rmcolq/Singularity_recipes
---

# rmcolq/Singularity_recipes:racon

```bash
$ singularity pull shub://rmcolq/Singularity_recipes:racon
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%help
  A container to hold the polishing tool racon.
  Run `singularity exec racon.simg racon`

%environment
  PATH=/usr/local/bin:$PATH

%post
    apt-get update
    apt-get install -y software-properties-common
    apt-add-repository universe
    apt-get update
    apt-get install -y \
      build-essential \
      cmake \
      git \
      libbz2-dev \
      liblzma-dev \
      libncurses-dev \
      openjdk-8-jre \
      wget \
      zlib1g-dev
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT

    #============================================
    # INSTALL MINIMAP2
    #============================================
    VERSION="2.11"
    wget https://github.com/lh3/minimap2/archive/v"$VERSION".tar.gz
    tar xzf v"$VERSION".tar.gz
    rm v"$VERSION".tar.gz
    cd minimap2-*
    make
    echo "export PATH=$PWD:$PATH" >> $SINGULARITY_ENVIRONMENT
    cd ..

    #============================================
    # INSTALL RACON
    #============================================
    git clone --recursive https://github.com/isovic/racon.git racon
    cd racon
    mkdir build
    cd build
    cmake -DCMAKE_BUILD_TYPE=Release ..
    make
    make install
```

## Collection

 - Name: [rmcolq/Singularity_recipes](https://github.com/rmcolq/Singularity_recipes)
 - License: None

