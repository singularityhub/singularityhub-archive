---
id: 5551
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "vcftools"
commit: "c0af79dc032d20c5ae72f756e67aa8e6e0015256"
version: "20f82cf296897e90b545200ad3c508e0"
build_date: "2018-11-12T16:21:13.071Z"
size_mb: 678
size: 234303519
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/vcftools/2018-11-12-c0af79dc-20f82cf2/20f82cf296897e90b545200ad3c508e0.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/vcftools/2018-11-12-c0af79dc-20f82cf2/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/vcftools/2018-11-12-c0af79dc-20f82cf2/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:vcftools

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:vcftools
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

    # ========================
    # INSTALL vcftools
    # ========================
    apt install -y pkg-config zlib1g-dev
    VERSION="0.1.16"
    URL=https://github.com/vcftools/vcftools/releases/download/v"$VERSION"/vcftools-"$VERSION".tar.gz
    wget -O - "$URL" | tar xzf -
    cd vcftools*
    ./configure --prefix=/usr/local
    make
    make install

    # install tabix dependency
    cd ~/
    wget -O - https://sourceforge.net/projects/samtools/files/tabix/tabix-0.2.6.tar.bz2/download | tar xjf -
    cd tabix*
    make
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
    cd ..
    chmod -R 777 tabix*
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

