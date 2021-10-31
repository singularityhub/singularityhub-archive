---
id: 6092
name: "nguyemi5/vir-lift"
branch: "master"
tag: "kinetic"
commit: "a9ff5de08fb4632ef6755fb1ae4e4d9b8bb7e4ac"
version: "6e98470fa23dfafee4af7b84d16f909c"
build_date: "2019-01-04T07:48:36.727Z"
size_mb: 7106
size: 2990448671
sif: "https://datasets.datalad.org/shub/nguyemi5/vir-lift/kinetic/2019-01-04-a9ff5de0-6e98470f/6e98470fa23dfafee4af7b84d16f909c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/nguyemi5/vir-lift/kinetic/2019-01-04-a9ff5de0-6e98470f/
recipe: https://datasets.datalad.org/shub/nguyemi5/vir-lift/kinetic/2019-01-04-a9ff5de0-6e98470f/Singularity
collection: nguyemi5/vir-lift
---

# nguyemi5/vir-lift:kinetic

```bash
$ singularity pull shub://nguyemi5/vir-lift:kinetic
```

## Singularity Recipe

```singularity
bootstrap:docker
From:ros:kinetic-robot

%labels

AUTHOR Yasasvy Nanyam ynanyam@iastate.edu

%environment

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

%post

    sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
    apt-get update

    apt-get install -y ros-kinetic-desktop-full
    apt-get install -y libalglib-dev
    apt-get install -y gnuplot
    apt-get install -y python-pip
    apt-get install -y python-flufl.lock
    apt-get install -y python-opencv
    python -m pip install h5py
    python -m pip install scipy
    python -m pip install parse
    pip install git+https://github.com/Theano/Theano.git#egg=Theano
    pip install --upgrade https://github.com/Lasagne/Lasagne/archive/master.zip
           
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
        
        export PATH="/usr/local/anaconda3/bin:$PATH"
        CMAKE_PREFIX_PATH=/opt/ros/kinetic
        export CMAKE_PREFIX_PATH
        conda install -y -c mila-udem -c mila-udem/label/pre theano pygpu
```

## Collection

 - Name: [nguyemi5/vir-lift](https://github.com/nguyemi5/vir-lift)
 - License: None

