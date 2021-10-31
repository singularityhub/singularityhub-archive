---
id: 6102
name: "nguyemi5/vir-lift"
branch: "master"
tag: "cuda"
commit: "d7d560e72080366e67b1da5d33f84295f8baa926"
version: "5eb250d20823d057475fe4e391431db5"
build_date: "2019-01-04T07:48:36.721Z"
size_mb: 9235
size: 4352966687
sif: "https://datasets.datalad.org/shub/nguyemi5/vir-lift/cuda/2019-01-04-d7d560e7-5eb250d2/5eb250d20823d057475fe4e391431db5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/nguyemi5/vir-lift/cuda/2019-01-04-d7d560e7-5eb250d2/
recipe: https://datasets.datalad.org/shub/nguyemi5/vir-lift/cuda/2019-01-04-d7d560e7-5eb250d2/Singularity
collection: nguyemi5/vir-lift
---

# nguyemi5/vir-lift:cuda

```bash
$ singularity pull shub://nguyemi5/vir-lift:cuda
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.2-cudnn7-devel-ubuntu16.04

%environment

  # use bash as default shell
  SHELL=/bin/bash

  # add CUDA paths
  CPATH="/usr/local/cuda/include:$CPATH"
  PATH="/usr/local/cuda/bin:$PATH"
  LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"
  CUDA_HOME="/usr/local/cuda"

  # add Anaconda path
  PATH="/usr/local/anaconda3/bin:$PATH"

  export PATH LD_LIBRARY_PATH CPATH CUDA_HOME

  # add Ros path
  ROS_ROOT=/opt/ros/kinetic/share/ros
  export ROS_ROOT
  ROS_PACKAGE_PATH=/opt/ros/kinetic/share:/opt/ros/kinetic/stacks
  export ROS_PACKAGE_PATH
  ROS_MASTER_URI=http://localhost:11311
  export ROS_MASTER_URI
  LD_LIBRARY_PATH=/opt/ros/kinetic/lib:/.singularity.d/libs
  export LD_LIBRARY_PATH
  CPATH=/opt/ros/kinetic/include
  export CPATH
  PATH=/opt/ros/kinetic/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
  export PATH
  PYTHONPATH=/opt/ros/kinetic/lib/python2.7/dist-packages
  export PYTHONPATH
  PKG_CONFIG_PATH=/opt/ros/kinetic/lib/pkgconfig
  export PKG_CONFIG_PATH
  CMAKE_PREFIX_PATH=/opt/ros/kinetic
  export CMAKE_PREFIX_PATH
  ROS_ETC_DIR=/opt/ros/kinetic/etc/ros
  export ROS_ETC_DIR

%setup
  # runs on host
  # the path to the image is $SINGULARITY_ROOTFS

%post
  # post-setup script
 
  apt-get update && apt-get install -q -y \
    dirmngr \
    gnupg2 \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*
  
  # install ros
  sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
  apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
 
  apt-get update && apt-get install --no-install-recommends -y \
    python-rosdep \
    python-rosinstall \
    python-vcstools \
    python-rosinstall-generator \
    python-wstool \
    && rm -rf /var/lib/apt/lists/*
  
  rosdep init
  rosdep update
  
  apt-get update && apt-get install -y \
    ros-kinetic-ros-core=1.3.2-0* \
    && rm -rf /var/lib/apt/lists/*
  
  apt-get update
  apt-get install -y ros-kinetic-desktop-full
  
  apt-get update
  apt-get install -y build-essential

  # load environment variables
  . /environment

  # use bash as default shell
  echo "\n #Using bash as default shell \n" >> /environment
  echo 'SHELL=/bin/bash' >> /environment

  # make environment file executable
  chmod +x /environment

  # default mount paths
  mkdir /scratch /data 

  #Add CUDA paths
  echo "\n #Cuda paths \n" >> /environment
  echo 'export CPATH="/usr/local/cuda/include:$CPATH"' >> /environment
  echo 'export PATH="/usr/local/cuda/bin:$PATH"' >> /environment
  echo 'export LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"' >> /environment
  echo 'export CUDA_HOME="/usr/local/cuda"' >> /environment

  # updating and getting required packages
  apt-get update
  apt-get install -y wget git vim build-essential cmake

  # creates a build directory
  mkdir build
  cd build

  # download and install Anaconda
  CONDA_INSTALL_PATH="/usr/local/anaconda3"
  wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
  chmod +x Anaconda3-5.0.1-Linux-x86_64.sh
  ./Anaconda3-5.0.1-Linux-x86_64.sh -b -p $CONDA_INSTALL_PATH
  
%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [nguyemi5/vir-lift](https://github.com/nguyemi5/vir-lift)
 - License: None

