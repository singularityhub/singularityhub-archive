---
id: 3601
name: "rmcolq/Singularity_recipes"
branch: "master"
tag: "canu"
commit: "198bb4c802b56e49a150d0cb9d0b15b3cdc965c7"
version: "ace63073235013bc3d8fc27561880bbd"
build_date: "2018-07-21T00:28:23.734Z"
size_mb: 1401
size: 576516127
sif: "https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/canu/2018-07-21-198bb4c8-ace63073/ace63073235013bc3d8fc27561880bbd.simg"
url: https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/canu/2018-07-21-198bb4c8-ace63073/
recipe: https://datasets.datalad.org/shub/rmcolq/Singularity_recipes/canu/2018-07-21-198bb4c8-ace63073/Singularity
collection: rmcolq/Singularity_recipes
---

# rmcolq/Singularity_recipes:canu

```bash
$ singularity pull shub://rmcolq/Singularity_recipes:canu
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%help
  A container to hold the assembler canu.
  Run `singularity exec canu.simg canu`

%environment
  PATH=/usr/local/bin:/root/canu-1.7/Linux-amd64/bin:$PATH

%post
    apt-get update
    apt-get install -y software-properties-common
    apt-add-repository universe
    apt-get update
    apt-get install -y \
      wget build-essential \
      openjdk-8-jre \
      gnuplot
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT


    #============================================
    # INSTALL CANU
    #============================================
    VERSION="1.7"
    wget https://github.com/marbl/canu/archive/v"$VERSION".tar.gz
    tar xzf v$VERSION.tar.gz
    rm v$VERSION.tar.gz
    cd canu-${VERSION}/src
    make -j 8
    cd ../Linux-amd64/bin/
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [rmcolq/Singularity_recipes](https://github.com/rmcolq/Singularity_recipes)
 - License: None

