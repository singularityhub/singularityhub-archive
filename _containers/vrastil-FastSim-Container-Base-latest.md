---
id: 5700
name: "vrastil/FastSim-Container-Base"
branch: "master"
tag: "latest"
commit: "2985f5156c4e686c56c757f03d73f7b3507dac40"
version: "a16e575ffabb3d92aced53b40042acd2"
build_date: "2019-02-26T17:00:36.919Z"
size_mb: 1258
size: 493195295
sif: "https://datasets.datalad.org/shub/vrastil/FastSim-Container-Base/latest/2019-02-26-2985f515-a16e575f/a16e575ffabb3d92aced53b40042acd2.simg"
url: https://datasets.datalad.org/shub/vrastil/FastSim-Container-Base/latest/2019-02-26-2985f515-a16e575f/
recipe: https://datasets.datalad.org/shub/vrastil/FastSim-Container-Base/latest/2019-02-26-2985f515-a16e575f/Singularity
collection: vrastil/FastSim-Container-Base
---

# vrastil/FastSim-Container-Base:latest

```bash
$ singularity pull shub://vrastil/FastSim-Container-Base:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:stretch

%help
    Contains necessary packages and libraries to build image FastSim-Container (https://github.com/vrastil/FastSim-Container).

%post
    # get libraries from package manager
    apt-get -y update && apt-get install -y --no-install-recommends apt-utils
    apt-get -y install build-essential
    apt-get -y install gcc-6 g++-6 libstdc++6 python python-pip
    apt-get -y install cmake git swig wget vim valgrind tar
    apt-get -y install libgsl-dev libfftw3-dev pkg-config libbz2-dev
    pip install numpy

    # data directory -- all building should be done here
    mkdir /data

    # install boost manually (need new version)
    cd /data
    wget https://dl.bintray.com/boostorg/release/1.69.0/source/boost_1_69_0.tar.bz2
    tar --bzip2 -xf boost_1_69_0.tar.bz2 && cd boost_1_69_0
    ./bootstrap.sh --with-libraries=program_options,filesystem,system,log,timer,thread
    ./b2 install
    cd .. && rm -rf boost_1_69_0
```

## Collection

 - Name: [vrastil/FastSim-Container-Base](https://github.com/vrastil/FastSim-Container-Base)
 - License: None

