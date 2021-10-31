---
id: 3567
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "pandora"
commit: "54c141a214e113dfa7366affc7afcdcbf819508b"
version: "ac594f67db8a2f66e1c5cc049cfe1968"
build_date: "2020-12-05T20:16:59.649Z"
size_mb: 2678
size: 801996831
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/pandora/2020-12-05-54c141a2-ac594f67/ac594f67db8a2f66e1c5cc049cfe1968.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/pandora/2020-12-05-54c141a2-ac594f67/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/pandora/2020-12-05-54c141a2-ac594f67/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:pandora

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:pandora
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
    apt-get install -y man time
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
    git clone https://github.com/rmcolq/pandora.git
    cd pandora
    mkdir -p build
    cd build
    cmake ..
    make
    ctest -VV
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

