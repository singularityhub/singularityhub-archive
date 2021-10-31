---
id: 5465
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "ngm"
commit: "c45bed96c50e230a37fe94bda3d991b41c41620f"
version: "b90ff1e4827eb3f36ca37475fe5b0075"
build_date: "2018-11-05T14:28:46.666Z"
size_mb: 904
size: 289624095
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/ngm/2018-11-05-c45bed96-b90ff1e4/b90ff1e4827eb3f36ca37475fe5b0075.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/ngm/2018-11-05-c45bed96-b90ff1e4/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/ngm/2018-11-05-c45bed96-b90ff1e4/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:ngm

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:ngm
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%environment
  PATH=/usr/local/bin:$PATH

%post
    apt update
    apt install -y software-properties-common
    apt-add-repository universe
    apt update
    apt install -y git wget build-essential
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT

    #================================
    # INSTALL NGM 
    #================================
    VERSION="0.5.5"
    URL=https://github.com/Cibiv/NextGenMap/archive/v"$VERSION".tar.gz
    apt install -y cmake
    wget -O - "$URL" | tar xzf -
    cd NextGenMap*
    mkdir -p build/
    cd build/
    cmake ..
    make
    cd ../bin/ngm*
    chmod 777 ngm
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

