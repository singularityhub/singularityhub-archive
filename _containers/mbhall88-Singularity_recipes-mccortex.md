---
id: 2027
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "mccortex"
commit: "127e15583f2a83c4ded0f3078bb330e9eb5563dd"
version: "9073f94a8aad34f1aa5dce57abda0f60"
build_date: "2018-11-07T17:43:25.551Z"
size_mb: 1171
size: 467419167
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/mccortex/2018-11-07-127e1558-9073f94a/9073f94a8aad34f1aa5dce57abda0f60.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mbhall88/Singularity_recipes/mccortex/2018-11-07-127e1558-9073f94a/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/mccortex/2018-11-07-127e1558-9073f94a/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:mccortex

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:mccortex
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL:  http://us.archive.ubuntu.com/ubuntu/

%environment
  PATH=/usr/local/bin:$PATH

%test
    cd ~/mccortex
    make test

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
    # INSTALL mccortex
    # ========================
    apt install -y \
      liblzma-dev \
      libbz2-dev \
      libz-dev \
      libncurses5-dev \
      zlib1g-dev \
      r-base-core

    cd ~/
    COMMIT="400c0e322aae2d3563b4f1fad270fd95a878ba15"
    git clone --recursive https://github.com/mcveanlab/mccortex
    cd mccortex
    git checkout "$COMMIT"
    make all MAXK=31
    make all MAXK=63
    cd bin
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

