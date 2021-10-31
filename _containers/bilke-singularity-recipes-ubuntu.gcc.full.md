---
id: 1318
name: "bilke/singularity-recipes"
branch: "master"
tag: "ubuntu.gcc.full"
commit: "3df159f0660a2ed37eef796c9a7e78b393e5e17f"
version: "2439cb80c1e6af3936fcf11eee04aa4d"
build_date: "2018-01-16T09:35:20.252Z"
size_mb: 1540
size: 640446495
sif: "https://datasets.datalad.org/shub/bilke/singularity-recipes/ubuntu.gcc.full/2018-01-16-3df159f0-2439cb80/2439cb80c1e6af3936fcf11eee04aa4d.simg"
url: https://datasets.datalad.org/shub/bilke/singularity-recipes/ubuntu.gcc.full/2018-01-16-3df159f0-2439cb80/
recipe: https://datasets.datalad.org/shub/bilke/singularity-recipes/ubuntu.gcc.full/2018-01-16-3df159f0-2439cb80/Singularity
collection: bilke/singularity-recipes
---

# bilke/singularity-recipes:ubuntu.gcc.full

```bash
$ singularity pull shub://bilke/singularity-recipes:ubuntu.gcc.full
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
    CC=gcc-4.9
    CXX=g++-4.9
    CCACHE_MAXSIZE=15G
    CCACHE_SLOPPINESS=pch_defines,time_macros
    export CC CXX CCACHE_MAXSIZE CCACHE_SLOPPINESS

%post
    apt-get update
    apt-get install -y software-properties-common curl
    add-apt-repository -y ppa:ubuntu-toolchain-r/test
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
    apt-get update
    apt-get -y install \
      ccache \
      gcc-4.9 g++-4.9 gcc-4.9-base \
      git git-lfs \
      python-pip \
      sudo \
      unzip

    python -m pip install --upgrade pip
    python -m pip install cmake conan>=1.0.0

    curl -L -o ninja-linux.zip https://github.com/ninja-build/ninja/releases/download/v1.8.2/ninja-linux.zip
    unzip ninja-linux.zip
    mv ninja /usr/local/bin/ninja
    rm ninja-linux.zip

    ### END gcc.minimal ###

    apt-get -y install apt-transport-https
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
    echo "deb https://dl.yarnpkg.com/debian/ stable main" \
      | tee /etc/apt/sources.list.d/yarn.list
    curl -s https://deb.nodesource.com/setup_8.x | bash
    apt-get update
    apt-get install -y \
      biber \
      doxygen \
      graphviz \
      libxml2-utils \
      nodejs \
      pandoc-citeproc \
      yarn

    update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10

    curl -L -o hugo.tar.gz https://github.com/gohugoio/hugo/releases/download/v0.32.3/hugo_0.32.3_Linux-64bit.tar.gz
    tar xf hugo.tar.gz
    mv hugo /usr/local/bin/hugo
    rm -rf hugo.tar.gz LICENSE.md README.md

    ### END gcc.full

    ### Conan hack, as sudo is not available in container
    apt-get install -y \
      freeglut3-dev \
      mesa-common-dev \
      mesa-utils-extra \
      libgl1-mesa-dev \
      libglapi-mesa \
      libsm-dev \
      libx11-dev \
      libxext-dev \
      libxt-dev \
      libglu1-mesa-dev
```

## Collection

 - Name: [bilke/singularity-recipes](https://github.com/bilke/singularity-recipes)
 - License: None

