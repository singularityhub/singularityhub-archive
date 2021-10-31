---
id: 3885
name: "rmcolq/Singularity_recipes"
branch: "master"
tag: "pilon"
commit: "2e880b706631e3008de70d428584d22016c62469"
version: "4d378d53510d1d6395119c3cb00af03b"
build_date: "2020-04-28T08:53:21.106Z"
size_mb: 1105
size: 498290719
sif: "https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/pilon/2020-04-28-2e880b70-4d378d53/4d378d53510d1d6395119c3cb00af03b.simg"
url: https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/pilon/2020-04-28-2e880b70-4d378d53/
recipe: https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/pilon/2020-04-28-2e880b70-4d378d53/Singularity
collection: rmcolq/Singularity_recipes
---

# rmcolq/Singularity_recipes:pilon

```bash
$ singularity pull shub://rmcolq/Singularity_recipes:pilon
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%help
  A container to hold the polishing tool pilon.
  Run `singularity exec pilon.simg pilon`

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
    
    #================================
    # INSTALL SAMTOOLS
    #================================
    VERSION="1.9"
    wget https://github.com/samtools/samtools/releases/download/"$VERSION"/samtools-"$VERSION".tar.bz2
    tar xjf samtools-"$VERSION".tar.bz2 
    rm samtools*.tar.bz2
    cd samtools*
    ./configure 
    make 
    make install 
    cd .. 
    rm -rf samtools-*

    #================================
    # INSTALL BWA
    #================================
    VERSION="0.7.17"
    wget https://github.com/lh3/bwa/releases/download/"v"$VERSION/bwa-$VERSION.tar.bz2
    tar xf bwa-"$VERSION".tar.bz2
    rm bwa-"$VERSION".tar.bz2
    cd bwa-*
    make
    export PATH=$PWD:$PATH
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
    cd ..

    #============================================
    # INSTALL PILON
    #============================================
    wget https://github.com/broadinstitute/pilon/releases/download/v1.22/pilon-1.22.jar
    echo "alias pilon='java -Xmx16G -jar $PWD/pilon-1.22.jar'" >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [rmcolq/Singularity_recipes](https://github.com/rmcolq/Singularity_recipes)
 - License: None

