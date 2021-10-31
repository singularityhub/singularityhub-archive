---
id: 1320
name: "bilke/singularity-recipes"
branch: "master"
tag: "ubuntu"
commit: "ab1c4aa8c3f2326bf9b20ddac0e05908fb6b617b"
version: "0ac43815ea03eb2e3092f8341ae8958a"
build_date: "2018-01-16T09:35:20.230Z"
size_mb: 793
size: 328859679
sif: "https://datasets.datalad.org/shub/bilke/singularity-recipes/ubuntu/2018-01-16-ab1c4aa8-0ac43815/0ac43815ea03eb2e3092f8341ae8958a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bilke/singularity-recipes/ubuntu/2018-01-16-ab1c4aa8-0ac43815/
recipe: https://datasets.datalad.org/shub/bilke/singularity-recipes/ubuntu/2018-01-16-ab1c4aa8-0ac43815/Singularity
collection: bilke/singularity-recipes
---

# bilke/singularity-recipes:ubuntu

```bash
$ singularity pull shub://bilke/singularity-recipes:ubuntu
```

## Singularity Recipe

```singularity
#Bootstrap: debootstrap
#OSVersion: xenial
#MirrorURL:  http://us.archive.ubuntu.com/ubuntu/
Bootstrap: docker
From: ubuntu:16.04

%environment
    CC=gcc-4.9
    CXX=g++-4.9
    export CC CXX
    
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
```

## Collection

 - Name: [bilke/singularity-recipes](https://github.com/bilke/singularity-recipes)
 - License: None

