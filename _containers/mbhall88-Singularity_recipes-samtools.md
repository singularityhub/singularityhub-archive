---
id: 5468
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "samtools"
commit: "99a5ed2cf05b7d61351570515e22d024b786cefe"
version: "fa53d7d0f9d4b7089c2e19a0aa555119"
build_date: "2019-01-15T14:08:05.534Z"
size_mb: 635
size: 223711263
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/samtools/2019-01-15-99a5ed2c-fa53d7d0/fa53d7d0f9d4b7089c2e19a0aa555119.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mbhall88/Singularity_recipes/samtools/2019-01-15-99a5ed2c-fa53d7d0/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/samtools/2019-01-15-99a5ed2c-fa53d7d0/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:samtools

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:samtools
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%environment
    export PATH=/usr/local/bin:$PATH
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8

%post
    apt update
    apt install -y software-properties-common
    apt-add-repository universe
    apt update
    apt install -y wget build-essential
    
    # ================================
    # INSTALL samtools
    # ================================
    VERSION="1.9"
    URL=https://github.com/samtools/samtools/releases/download/${VERSION}/samtools-${VERSION}.tar.bz2
    apt install -y libncurses5-dev \
        libbz2-dev \
        liblzma-dev \
        zlib1g-dev
    wget "$URL" -O - | tar -jxf -
    cd samtools*
    ./configure --prefix=/usr/local
    make
    make install
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

