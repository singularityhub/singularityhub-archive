---
id: 2983
name: "ozanarkancan/lang-grounding-xworld"
branch: "master"
tag: "latest"
commit: "8c469c2d1ccc563f2d03451ce8822dcea943757d"
version: "2e46c77095994b7ba107d1489bf2ba09"
build_date: "2018-05-30T12:30:56.442Z"
size_mb: 1995
size: 611262495
sif: "https://datasets.datalad.org/shub/ozanarkancan/lang-grounding-xworld/latest/2018-05-30-8c469c2d-2e46c770/2e46c77095994b7ba107d1489bf2ba09.simg"
url: https://datasets.datalad.org/shub/ozanarkancan/lang-grounding-xworld/latest/2018-05-30-8c469c2d-2e46c770/
recipe: https://datasets.datalad.org/shub/ozanarkancan/lang-grounding-xworld/latest/2018-05-30-8c469c2d-2e46c770/Singularity
collection: ozanarkancan/lang-grounding-xworld
---

# ozanarkancan/lang-grounding-xworld:latest

```bash
$ singularity pull shub://ozanarkancan/lang-grounding-xworld:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial

%runscript
    echo "Run script"

%environment
    LANG=C.UTF-8
    LC_ALL=C.UTF-8
    export LANG LC_ALL
    export PYTHONPATH=/workdir/XWorld/python:$PYTHONPATH
    export LD_LIBRARY_PATH=/usr/lib:/usr/lib64:/usr/local/cuda/lib64:/usr/local/cuda/lib:/opt/cudnn/lib64:$LD_LIBRARY_PATH
    export PATH=/opt/julia-0.6/bin:/usr/local/cuda/bin:$PATH
    export JULIA_PKGDIR=/workdir/.julia

%post
    apt-get update && apt-get install -q -y --no-install-recommends \
        sudo \
        less \
        dirmngr \
        gnupg2 \
        build-essential \
        libzmq3-dev \
        pkg-config \
        python \
        python-dev \
        python-pip \
        git \
        vim \
        libxml2 \
        wget \
        curl \
        unzip \
        libboost-all-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libgtest-dev \
        cmake \
        xserver-xorg \
        libglu1-mesa-dev \
        freeglut3-dev \
        mesa-common-dev \
        libxmu-dev \
        libxi-dev \
        mesa-utils \
        pciutils \
        && rm -rf /var/lib/apt/lists/*

    cd /usr/src/gtest
    cmake CMakeLists.txt
    make
    cp *.a /usr/lib

    mkdir -p /opt/julia-0.6.2-dev && \
        curl -s -L https://julialang-s3.julialang.org/bin/linux/x64/0.6/julia-0.6.2-linux-x86_64.tar.gz | tar -C /opt/julia-0.6.2-dev -x -z --strip-components=1 -f -
        ln -fs /opt/julia-0.6.2-dev /opt/julia-0.6

    mkdir -p /workdir
    export JULIA_PKGDIR=/workdir/.julia

    /opt/julia-0.6/bin/julia -e 'Pkg.init()'
    /opt/julia-0.6/bin/julia -e 'Pkg.add("Knet")'
    /opt/julia-0.6/bin/julia -e 'Pkg.add("JLD")'
    /opt/julia-0.6/bin/julia -e 'Pkg.add("JLD2")'
    /opt/julia-0.6/bin/julia -e 'Pkg.add("Images")'
    /opt/julia-0.6/bin/julia -e 'Pkg.add("ArgParse")'
    /opt/julia-0.6/bin/julia -e 'Pkg.add("LightXML")'
    /opt/julia-0.6/bin/julia -e 'Pkg.add("PyCall")'
    /opt/julia-0.6/bin/julia -e 'Pkg.checkout("AutoGrad")'
    /opt/julia-0.6/bin/julia -e 'Pkg.checkout("Knet")'

    rm -rf /workdir/.julia/.cache
    rm -rf /workdir/.julia/lib
    cd /workdir
    git clone https://github.com/PaddlePaddle/XWorld
    cd XWorld
    mkdir build
    chmod -R 777 /workdir

    mkdir -p /opt/cudnn
    mkdir -p /usr/local/cuda
```

## Collection

 - Name: [ozanarkancan/lang-grounding-xworld](https://github.com/ozanarkancan/lang-grounding-xworld)
 - License: None

