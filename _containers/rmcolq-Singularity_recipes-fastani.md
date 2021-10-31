---
id: 7312
name: "rmcolq/Singularity_recipes"
branch: "master"
tag: "fastani"
commit: "c87889bd49179a38e047c5be5af2a09aa799fdcd"
version: "b6e6a4dbfa29cdc761f22b1f0ddfd4fa"
build_date: "2019-02-19T17:11:32.010Z"
size_mb: 1682
size: 405454879
sif: "https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/fastani/2019-02-19-c87889bd-b6e6a4db/b6e6a4dbfa29cdc761f22b1f0ddfd4fa.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rmcolq/Singularity_recipes/fastani/2019-02-19-c87889bd-b6e6a4db/
recipe: https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/fastani/2019-02-19-c87889bd-b6e6a4db/Singularity
collection: rmcolq/Singularity_recipes
---

# rmcolq/Singularity_recipes:fastani

```bash
$ singularity pull shub://rmcolq/Singularity_recipes:fastani
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%help
  To run: `singularity exec pandora.simg pandora`

%environment
  PATH=/usr/local/bin:$PATH

%post
    apt update
    apt install -y software-properties-common
    apt-add-repository universe
    apt update
    apt install -y git wget build-essential cmake seqtk
    apt-get install -y man time autoconf gsl-bin libgsl0-dev vim samtools
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT

    #============================================
    # INSTALL ZLIB
    #============================================
    VERSION="1.2.11"
    wget http://www.zlib.net/zlib-"$VERSION".tar.gz -O - | tar xzf -
    cd zlib-"$VERSION"
    ./configure --prefix=/usr/
    make
    make install
    cd ..

    #============================================
    # INSTALL BOOST 
    #============================================
    wget https://sourceforge.net/projects/boost/files/boost/1.62.0/boost_1_62_0.tar.gz -O - | tar xzf -
    cd boost_1_62_0
    ./bootstrap.sh --prefix=/usr/ --with-libraries=system,filesystem,iostreams,log,thread,date_time
    ./b2 install
    cd ..

    #============================================
    # INSTALL PANDORA
    #============================================
    wget https://github.com/ParBLiSS/FastANI/archive/v1.1.tar.gz
    tar xvf v*.tar.gz
    rm v*.tar.gz
    cd FastANI-*/
    ./bootstrap.sh
    ./configure
    make
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [rmcolq/Singularity_recipes](https://github.com/rmcolq/Singularity_recipes)
 - License: None

