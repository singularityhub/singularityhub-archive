---
id: 5464
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "minimap2"
commit: "fc132841cea261394da0b6c6f4faf8e530ac0f33"
version: "6c6677602765b02316ea579894054c7a"
build_date: "2019-06-02T17:47:33.062Z"
size_mb: 571
size: 206602271
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/minimap2/2019-06-02-fc132841-6c667760/6c6677602765b02316ea579894054c7a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mbhall88/Singularity_recipes/minimap2/2019-06-02-fc132841-6c667760/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/minimap2/2019-06-02-fc132841-6c667760/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:minimap2

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:minimap2
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
    apt install -y wget build-essential
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT

    # ================================
    # INSTALL minimap2
    # ================================
    VERSION="2.13"
    URL=https://github.com/lh3/minimap2/releases/download/v${VERSION}/minimap2-${VERSION}_x64-linux.tar.bz2
    wget "$URL" -O - | tar -jxf -
    cd minimap2-${VERSION}_x64-linux/ || exit 1
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

