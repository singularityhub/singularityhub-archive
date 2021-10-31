---
id: 9081
name: "bballew/NGS_singularity_recipes"
branch: "master"
tag: "glnexus"
commit: "e1847911aa37e349fe66036f33a18497a01b7189"
version: "d30e3c27bb66ae10648d5784e891aea1"
build_date: "2019-05-14T23:21:54.108Z"
size_mb: 1940
size: 545423391
sif: "https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/glnexus/2019-05-14-e1847911-d30e3c27/d30e3c27bb66ae10648d5784e891aea1.simg"
url: https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/glnexus/2019-05-14-e1847911-d30e3c27/
recipe: https://datasets.datalad.org/shub/bballew/NGS_singularity_recipes/glnexus/2019-05-14-e1847911-d30e3c27/Singularity
collection: bballew/NGS_singularity_recipes
---

# bballew/NGS_singularity_recipes:glnexus

```bash
$ singularity pull shub://bballew/NGS_singularity_recipes:glnexus
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu

%labels
    AUTHOR BBallew

%setup
    mkdir -p ${SINGULARITY_ROOTFS}/input
    mkdir -p ${SINGULARITY_ROOTFS}/output
    mkdir -p ${SINGULARITY_ROOTFS}/ref
    mkdir -p ${SINGULARITY_ROOTFS}/scratch
    mkdir -p ${SINGULARITY_ROOTFS}/exec

%post

    apt-get -qq update && \
         apt-get -qq install -y --no-install-recommends --no-install-suggests \
         curl wget ca-certificates git-core less netbase \
         g++ cmake autoconf make file valgrind \
         libjemalloc-dev libzip-dev libsnappy-dev libbz2-dev zlib1g-dev liblzma-dev libzstd-dev \
         python-pyvcf
    
    git clone https://github.com/dnanexus-rnd/GLnexus.git
    cd /GLnexus
    git fetch --tags origin && git checkout "$git_revision" && git submodule update --init --recursive
    cmake -DCMAKE_BUILD_TYPE=$build_type . && make -j4
    
    
    
    
# Dockerfile for building GLnexus. The resulting container image runs the unit tests
# by default. It has in its working directory the statically linked glnexus_cli
# executable which can be copied out.
#FROM ubuntu:18.04
#MAINTAINER DNAnexus
#ENV DEBIAN_FRONTEND noninteractive
#ARG git_revision=master
#ARG build_type=Release

# dependencies
#RUN apt-get -qq update && \
#     apt-get -qq install -y --no-install-recommends --no-install-suggests \
#     curl wget ca-certificates git-core less netbase \
#     g++ cmake autoconf make file valgrind \
#     libjemalloc-dev libzip-dev libsnappy-dev libbz2-dev zlib1g-dev liblzma-dev libzstd-dev \
#     python-pyvcf

# clone GLnexus repo on the desired git revision
#WORKDIR /
#RUN git clone https://github.com/dnanexus-rnd/GLnexus.git
#WORKDIR /GLnexus
#RUN git fetch --tags origin && git checkout "$git_revision" && git submodule update --init --recursive

# compile GLnexus
#RUN cmake -DCMAKE_BUILD_TYPE=$build_type . && make -j4

# set up default container start to run tests
#CMD ctest -V
```

## Collection

 - Name: [bballew/NGS_singularity_recipes](https://github.com/bballew/NGS_singularity_recipes)
 - License: None

