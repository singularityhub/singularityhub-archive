---
id: 5460
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "bcftools"
commit: "8df7771a981a19074c76bc57b1074f5381e3e8f8"
version: "c403791db8a14b00d536adca8e8e04fc"
build_date: "2019-08-01T23:48:42.517Z"
size_mb: 669
size: 235917343
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/bcftools/2019-08-01-8df7771a-c403791d/c403791db8a14b00d536adca8e8e04fc.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/bcftools/2019-08-01-8df7771a-c403791d/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/bcftools/2019-08-01-8df7771a-c403791d/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:bcftools

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:bcftools
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
    # INSTALL bcftools
    #================================
    VERSION="1.9"
    URL=https://github.com/samtools/bcftools/releases/download/"$VERSION"/bcftools-"$VERSION".tar.bz2
    apt install -y libbz2-dev \
        zlib1g-dev \
        libncurses5-dev \
        libncursesw5-dev \
        liblzma-dev

    wget "$URL" -O - | tar -jxf -
    cd bcftools*
    ./configure --prefix=/usr/local
    make
    make install
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

