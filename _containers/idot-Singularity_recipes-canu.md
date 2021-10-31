---
id: 3759
name: "idot/Singularity_recipes"
branch: "master"
tag: "canu"
commit: "17251dd3f863416f3f78af485ed6d25f1656adc1"
version: "fc390f53d92048c678e9c9d4eb603100"
build_date: "2018-07-30T16:14:05.775Z"
size_mb: 1261
size: 421568543
sif: "https://datasets.datalad.org/shub/idot/Singularity_recipes/canu/2018-07-30-17251dd3-fc390f53/fc390f53d92048c678e9c9d4eb603100.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/idot/Singularity_recipes/canu/2018-07-30-17251dd3-fc390f53/
recipe: https://datasets.datalad.org/shub/idot/Singularity_recipes/canu/2018-07-30-17251dd3-fc390f53/Singularity
collection: idot/Singularity_recipes
---

# idot/Singularity_recipes:canu

```bash
$ singularity pull shub://idot/Singularity_recipes:canu
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
  PATH=/usr/local/bin:$PATH

%post
    apt update
    apt install -y software-properties-common
    apt-add-repository universe
    apt update
    apt install -y wget build-essential 
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT


    #============================================
    # INSTALL CANU
    #============================================
    apt install -y openjdk-8-jre gnuplot
    VERSION="1.7.1"
    URL=https://github.com/marbl/canu/archive/v"$VERSION".tar.gz
    wget -qO- "$URL" | tar xvz
    cd canu-${VERSION}/src
    make -j 8
    cd ../Linux-amd64/bin/
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [idot/Singularity_recipes](https://github.com/idot/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

