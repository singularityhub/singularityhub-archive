---
id: 9492
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "medaka"
commit: "fc132841cea261394da0b6c6f4faf8e530ac0f33"
version: "120cf5e0782611095c716747692ac9f2"
build_date: "2019-06-02T17:47:33.068Z"
size_mb: 1610
size: 646836255
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/medaka/2019-06-02-fc132841-120cf5e0/120cf5e0782611095c716747692ac9f2.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/medaka/2019-06-02-fc132841-120cf5e0/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/medaka/2019-06-02-fc132841-120cf5e0/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:medaka

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:medaka
```

## Singularity Recipe

```singularity
Bootstrap: shub
from: mbhall88/Singularity_recipes:template

%post
    apt install -y curl zlib1g-dev libbz2-dev liblzma-dev libffi-dev libncurses5-dev \
        libcurl4-gnutls-dev libssl-dev python3-all-dev python-virtualenv python3-pip

    # install samtools
    VERSION="1.9"
    URL="https://github.com/samtools/samtools/releases/download/${VERSION}/samtools-${VERSION}.tar.bz2"
    wget "$URL" -O - | tar -jxf -
    cd samtools* || exit 1
    ./configure --prefix=/usr/local
    make
    make install
    cd "$HOME" || exit 1

    # install minimap2
    VERSION="2.11"
    URL=https://github.com/lh3/minimap2/releases/download/v${VERSION}/minimap2-${VERSION}_x64-linux.tar.bz2
    wget "$URL" -O - | tar -jxf -
    cd minimap2-${VERSION}_x64-linux/ || exit 1
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT

    # install medaka
    VERSION="0.7.1"
    pip3 install medaka=="$VERSION"
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

