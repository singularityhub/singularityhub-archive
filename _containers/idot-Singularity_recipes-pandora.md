---
id: 3760
name: "idot/Singularity_recipes"
branch: "master"
tag: "pandora"
commit: "534adc3c74f4b5b3a86b6e396deefb3782678f55"
version: "3342260c4ea72187db5f5161b9f7b5ff"
build_date: "2018-07-30T16:14:05.768Z"
size_mb: 2194
size: 509923359
sif: "https://datasets.datalad.org/shub/idot/Singularity_recipes/pandora/2018-07-30-534adc3c-3342260c/3342260c4ea72187db5f5161b9f7b5ff.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/idot/Singularity_recipes/pandora/2018-07-30-534adc3c-3342260c/
recipe: https://datasets.datalad.org/shub/idot/Singularity_recipes/pandora/2018-07-30-534adc3c-3342260c/Singularity
collection: idot/Singularity_recipes
---

# idot/Singularity_recipes:pandora

```bash
$ singularity pull shub://idot/Singularity_recipes:pandora
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
    apt install -y git wget build-essential cmake
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
    ./bootstrap.sh --prefix=/usr/ --with-libraries=system,filesystem,iostreams
    ./b2 install
    cd ..

    #============================================
    # INSTALL PANDORA
    #============================================
    git clone -b dev --single-branch https://github.com/rmcolq/pandora.git
    cd pandora
    mkdir -p build
    cd build
    cmake ..
    make
    ctest -VV
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [idot/Singularity_recipes](https://github.com/idot/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

