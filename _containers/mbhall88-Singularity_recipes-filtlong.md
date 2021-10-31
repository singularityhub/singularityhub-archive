---
id: 5463
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "filtlong"
commit: "8df7771a981a19074c76bc57b1074f5381e3e8f8"
version: "bc99083472beb5ea8cc25e0d5b035b3b"
build_date: "2019-09-19T12:30:04.184Z"
size_mb: 615
size: 225845279
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/filtlong/2019-09-19-8df7771a-bc990834/bc99083472beb5ea8cc25e0d5b035b3b.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/filtlong/2019-09-19-8df7771a-bc990834/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/filtlong/2019-09-19-8df7771a-bc990834/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:filtlong

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:filtlong
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
    apt install -y git wget build-essential zlib1g-dev
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT

    # ================================
    # INSTALL filtlong
    # ================================
    VERSION="0.2.0"
    URL=https://github.com/rrwick/Filtlong/archive/v${VERSION}.tar.gz
    wget -O - "$URL" | tar xzf -
    cd Filtlong*
    make -j
    cd bin
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

