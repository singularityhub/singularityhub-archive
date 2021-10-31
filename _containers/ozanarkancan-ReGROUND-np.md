---
id: 1690
name: "ozanarkancan/ReGROUND"
branch: "master"
tag: "np"
commit: "cc8d1732aebd0fb8bf2966f52f6c90c753729633"
version: "ae7ee7085a8b0761e6bd9b03c82efeb3"
build_date: "2018-02-09T16:52:43.090Z"
size_mb: 5367
size: 2168655903
sif: "https://datasets.datalad.org/shub/ozanarkancan/ReGROUND/np/2018-02-09-cc8d1732-ae7ee708/ae7ee7085a8b0761e6bd9b03c82efeb3.simg"
url: https://datasets.datalad.org/shub/ozanarkancan/ReGROUND/np/2018-02-09-cc8d1732-ae7ee708/
recipe: https://datasets.datalad.org/shub/ozanarkancan/ReGROUND/np/2018-02-09-cc8d1732-ae7ee708/Singularity
collection: ozanarkancan/ReGROUND
---

# ozanarkancan/ReGROUND:np

```bash
$ singularity pull shub://ozanarkancan/ReGROUND:np
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%environment
   
   ROS_DISTRO=lunar
   LANG=C.UTF-8
   LC_ALL=C.UTF-8
   export ROS_DISTRO LANG LC_ALL
   export LD_LIBRARY_PATH=/usr/lib:/usr/lib64:/usr/local/cuda/lib64:/usr/local/cuda/lib:/opt/cudnn/lib64:$LD_LIBRARY_PATH
   export PATH=/opt/julia-0.6/bin:/usr/local/cuda/bin:$PATH
   export JULIA_PKGDIR=/workdir/.julia

%post
 
   echo "Here we are installing software and other dependencies for the container!"
   apt-get update
   apt-get install -y \
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
    cmake \
    
   apt-get update && apt-get install -y --no-install-recommends \
      dirmngr \
      gnupg2 \
      && rm -rf /var/lib/apt/lists/*
   apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 421C365BD9FF1F717815A3895523BAEEB01FA116
   echo "deb http://packages.ros.org/ros/ubuntu xenial main" > /etc/apt/sources.list.d/ros-latest.list
   apt-get update && apt-get install --no-install-recommends -y \
    python-rosdep \
    python-rosinstall \
    python-vcstools \
    && rm -rf /var/lib/apt/lists/*
   rosdep init
   rosdep update
   
   apt-get update && apt-get install -y \
    ros-lunar-desktop-full=1.3.1-0* \
    && rm -rf /var/lib/apt/lists/*

    mkdir -p /opt/julia-0.6.2-dev && \
    curl -s -L https://julialang-s3.julialang.org/bin/linux/x64/0.6/julia-0.6.2-linux-x86_64.tar.gz | tar -C /opt/julia-0.6.2-dev -x -z --strip-components=1 -f -
    ln -fs /opt/julia-0.6.2-dev /opt/julia-0.6

    mkdir -p /workdir
    
    export JULIA_PKGDIR=/workdir/.julia
    
    /opt/julia-0.6/bin/julia -e 'Pkg.init()'
    /opt/julia-0.6/bin/julia -e 'Pkg.add("Knet")'
    /opt/julia-0.6/bin/julia -e 'Pkg.add("RobotOS")'
    /opt/julia-0.6/bin/julia -e 'Pkg.add("JLD")'
    /opt/julia-0.6/bin/julia -e 'Pkg.add("ArgParse")'
    /opt/julia-0.6/bin/julia -e 'Pkg.add("LightXML")'
    /opt/julia-0.6/bin/julia -e 'Pkg.add("PyCall")'

    rm -rf /workdir/.julia/.cache
    rm -rf /workdir/.julia/lib

    bash /opt/ros/lunar/setup.bash
    mkdir -p /workdir/rg/src

    chmod -R 777 /workdir

    pip install spacy
    python -m spacy download en_core_web_lg

    mkdir -p /opt/cudnn
    mkdir -p /usr/local/cuda
```

## Collection

 - Name: [ozanarkancan/ReGROUND](https://github.com/ozanarkancan/ReGROUND)
 - License: None

