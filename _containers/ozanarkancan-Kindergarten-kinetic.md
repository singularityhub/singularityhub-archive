---
id: 1890
name: "ozanarkancan/Kindergarten"
branch: "master"
tag: "kinetic"
commit: "54e8d1dd58580ebfd0dbee77548f15c4fc903d51"
version: "139c2cae979cf435a8628a445d6e14cf"
build_date: "2018-05-02T17:08:29.934Z"
size_mb: 4480
size: 1467654175
sif: "https://datasets.datalad.org/shub/ozanarkancan/Kindergarten/kinetic/2018-05-02-54e8d1dd-139c2cae/139c2cae979cf435a8628a445d6e14cf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ozanarkancan/Kindergarten/kinetic/2018-05-02-54e8d1dd-139c2cae/
recipe: https://datasets.datalad.org/shub/ozanarkancan/Kindergarten/kinetic/2018-05-02-54e8d1dd-139c2cae/Singularity
collection: ozanarkancan/Kindergarten
---

# ozanarkancan/Kindergarten:kinetic

```bash
$ singularity pull shub://ozanarkancan/Kindergarten:kinetic
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial

%runscript
    echo "Running tests"
    source /opt/ros/kinetic/setup.bash
    make test

%environment
   ROS_DISTRO=kinetic
   LANG=C.UTF-8
   LC_ALL=C.UTF-8
   export ROS_DISTRO LANG LC_ALL
   export LD_LIBRARY_PATH=/usr/lib:/usr/lib64:/usr/local/cuda/lib64:/usr/local/cuda/lib:/opt/cudnn/lib64:$LD_LIBRARY_PATH
   export PATH=/opt/julia-0.6/bin:/usr/local/cuda/bin:$PATH
   export JULIA_PKGDIR=/workdir/.julia
   export GAZEBO_MODEL_PATH=/usr/share/gazebo_models:$GAZEBO_MODEL_PATH

%post
    echo "Here we are installing software and other dependencies for the container!"
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
        cmake \
        && rm -rf /var/lib/apt/lists/*

    pip install --upgrade pip==9.0.3 setuptools wheel
    pip install astroid
    pip install isort
    pip install pylint
    pip install --upgrade pyflakes
    pip install lxml
    pip install -U mock
    pip install autoflake==0.7
    pip install autopep8==1.3.2
    pip install coverage==4.4.1
    pip install flake8==3.3.0
    pip install mock==2.0.0

    sudo rm -f /etc/ros/rosdep/sources.list.d/20-default.list
    echo "deb http://packages.ros.org/ros/ubuntu xenial main" > /etc/apt/sources.list.d/ros-latest.list
    apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
    apt-get update && apt-get install --no-install-recommends -y \
        python-rosdep \
        python-rosinstall \
        python-vcstools \
        && rm -rf /var/lib/apt/lists/*
    rosdep init
    rosdep update

    apt-get update && apt-get install -y \
        ros-kinetic-desktop \
        && rm -rf /var/lib/apt/lists/*
        
    apt-get update && apt-get install -q -y \
        libignition-math3 \
        && rm -rf /var/lib/apt/lists/*    
 
    apt-get update && apt-get install -q -y \
        binutils \
        mesa-utils \
        module-init-tools \
        x-window-system\
        && rm -rf /var/lib/apt/lists/*

    #curl -ssL http://get.gazebosim.org | sh
    apt-get update && apt-get install -q -y gazebo7
    apt-get install -q -y libgazebo7-dev

    #apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys D2486D2DD83DB69272AFE98867170598AF249743 ./etc/os-release \
    #    && ./etc/lsb-release \
    #    && echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable xenial main" > /etc/apt/sources.list.d/gazebo-latest.list

    apt-get install -q -y ros-kinetic-gazebo-ros-pkgs ros-kinetic-gazebo-ros-control
    
    apt-get install -q -y ros-kinetic-moveit
    apt-get install -q -y ros-kinetic-pr2-common

    apt-get install -q -y ros-kinetic-pr2-simulator 

    apt-get install ros-kinetic-xacro python-wstool ros-kinetic-tf-conversions ros-kinetic-kdl-parser


    wget https://bitbucket.org/osrf/gazebo_models/get/ea482a46e821.zip
    unzip ea482a46e821.zip
    mv osrf-gazebo_models-ea482a46e821 /usr/share/gazebo_models
    rm ea482a46e821.zip

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

    bash /opt/ros/kinetic/setup.bash
    mkdir -p /workdir/kindergarten_workspace/src
    chmod -R 777 /workdir

    mkdir -p /opt/cudnn
    mkdir -p /usr/local/cuda
```

## Collection

 - Name: [ozanarkancan/Kindergarten](https://github.com/ozanarkancan/Kindergarten)
 - License: None

