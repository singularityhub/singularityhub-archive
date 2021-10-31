---
id: 3740
name: "jhamer90811/singularity_imgs"
branch: "master"
tag: "ubuntu16.04-network_topology2"
commit: "46cbac27ffd6e7d70549b920eaf6d77bcae9c383"
version: "86cd67989ce9dae8c19acc94466522b2"
build_date: "2018-08-08T16:16:09.162Z"
size_mb: 3544
size: 1063682079
sif: "https://datasets.datalad.org/shub/jhamer90811/singularity_imgs/ubuntu16.04-network_topology2/2018-08-08-46cbac27-86cd6798/86cd67989ce9dae8c19acc94466522b2.simg"
url: https://datasets.datalad.org/shub/jhamer90811/singularity_imgs/ubuntu16.04-network_topology2/2018-08-08-46cbac27-86cd6798/
recipe: https://datasets.datalad.org/shub/jhamer90811/singularity_imgs/ubuntu16.04-network_topology2/2018-08-08-46cbac27-86cd6798/Singularity
collection: jhamer90811/singularity_imgs
---

# jhamer90811/singularity_imgs:ubuntu16.04-network_topology2

```bash
$ singularity pull shub://jhamer90811/singularity_imgs:ubuntu16.04-network_topology2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
Ubuntu16.04 with root v06.08.06 cuda9 cudnn7
DL/ML packages  : sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm
Development kit : g++/gcc cython nvcc libqt4-dev python-dev
Utility kit     : git wget emacs vim unzip

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

To use GPUs, try
singularity exec --nv THIS_CONTAINER.simg bash

Based on the recipe "Singularity.Ubuntu16.04-Basic" by drinkingkazu. Can be found on
https://github.com/DeepLearnPhysics/larcv2-singularity
    -All packages are installed using pip3 for compatibility with Python3.

#%files
#project-config.jam /tmp/project-config.jam
#build.sh /tmp/build.sh

%labels
Maintainer jhamer90811
Version 7/25/18

#------------
# Global installation
#------------
%environment
    # for system
    export XDG_RUNTIME_DIR=/tmp/$USER
    # for ROOT
    export ROOTSYS=/usr/local/root
    export PATH=${ROOTSYS}/bin:${PATH}
    export LD_LIBRARY_PATH=${ROOTSYS}/lib:${LD_LIBRARY_PATH}
    export PYTHONPATH=${ROOTSYS}/lib:${PYTHONPATH}
    export PATH=/usr/lib64/openmpi/bin/:$PATH

%post
    mkdir /scratch /data /lfstev

    # apt-get
    apt-get -y update
    apt-get -y install dpkg-dev g++ gcc binutils libqt4-dev python3-dev python3-tk python3-pip git wget emacs vim unzip pkg-config
    apt-get -y install protobuf-compiler

    # asciinema
    apt-get -y install software-properties-common python-software-properties
    apt-add-repository -y ppa:zanchey/asciinema
    apt-get -y update
    apt-get -y install asciinema
    apt-get -y install libhdf5-dev

    # ROOT
    wget https://root.cern.ch/download/root_v6.08.06.Linux-ubuntu16-x86_64-gcc5.4.tar.gz
    tar -xzf root_v6.08.06.Linux-ubuntu16-x86_64-gcc5.4.tar.gz
    rm root_v6.08.06.Linux-ubuntu16-x86_64-gcc5.4.tar.gz
    mv root /usr/local/root
    export ROOTSYS=/usr/local/root
    mkdir $ROOTSYS/tmp
    #mv /tmp/build.sh $ROOTSYS/tmp/build.sh
    #mv /tmp/project-config.jam $ROOTSYS/tmp/project-config.jam
    export PATH=${ROOTSYS}/bin:${PATH}
    export PATH=/usr/lib/python3.5/site-packages:/usr/local/lib/python3.5/dist-packages:${PATH}
    export LD_LIBRARY_PATH=${ROOTSYS}/lib:${LD_LIBRARY_PATH}
    export LD_LIBRARY_PATH=/usr/local/lib:/usr/lib:${LD_LIBRARY_PATH}
    export PYTHONPATH=${ROOTSYS}/lib:/usr/lib/python3.5/site-packages:/usr/local/lib/python3.5/dist-packages:${PYTHONPATH}

    #echo $LD_LIBRARY_PATH
    #echo $HOME

    # pip basics
    pip3 --no-cache-dir --disable-pip-version-check install --upgrade setuptools
    pip3 --no-cache-dir --disable-pip-version-check install numpy wheel zmq six pygments pyyaml cython gputil psutil humanize h5py tqdm scipy seaborn tables google cmake
    pip3 --no-cache-dir --disable-pip-version-check install python3-protobuf protobuf
    pip3 --no-cache-dir --disable-pip-version-check install root_numpy
    pip3 --no-cache-dir --disable-pip-version-check install matplotlib pandas scikit-image scikit-learn Pillow opencv-python
    pip3 --no-cache-dir --disable-pip-version-check install 'ipython<6.0'
    pip3 --no-cache-dir --disable-pip-version-check install jupyter notebook

    # install boost

    apt-get -y update
    apt-get -y install build-essential
    apt-get -y install boost*  && \
    apt-get -y remove  boost*
    apt-get -y install libicu-dev build-essential libbz2-dev bzip2 texinfo zlib1g openmpi-bin openmpi-doc libopenmpi-dev mpich autotools-dev
    apt-get -y install libboost-all-dev

    #chmod +x /tmp/build.sh
    #chmod +x /tmp/project-config.jam
    #mkdir /tmp/boost
    #/tmp/build.sh
    #ldconfig

    #apt-get -y install libcgal-dev libeigen3-dev libcgal-qt5-dev
    apt-get -y install libgmp-dev libgmp10 libgmp10-doc libgmp3-dev libgmpxx4ldbl
    apt-get -y install libmpfr-dev libmpfr-doc libmpfr4 libmpfr4-dbg

    apt-get -y build-dep cgal
    apt-get -y install libqt5svg5-dev qtscript5-dev libqt5opengl5-dev

    mkdir CGAL_4_11
    cd CGAL_4_11
    wget https://github.com/CGAL/cgal/releases/download/releases%2FCGAL-4.11/CGAL-4.11.zip
    unzip CGAL-4.11.zip
    rm CGAL-4.11.zip
    cd CGAL-4.11
    cmake .
    make

    export CMAKE_MODULE_PATH=/CGAL_4_11/CGAL-4.11:${CMAKE_MODULE_PATH}
    export CGAL_DIR=/CGAL_4_11/CGAL-4.11

    #apt-get -y install  libcgal11v5 libcgal-dev libcgal-qt5-11 libcgal-qt5-dev libcgal-demo libcgal-ipelets


    apt-get -y install libeigen3-dev libeigen3-doc libmrpt-dev

    #install GUDHI
    mkdir /gudhi
    cd /gudhi
    wget https://gforge.inria.fr/frs/download.php/latestzip/5253/library-latest.zip
    unzip library-latest.zip
    rm library-latest.zip
    tar -xf 2018-06-14-13-32-49_GUDHI_2.2.0.tar.gz
    rm 2018-06-14-13-32-49_GUDHI_2.2.0.tar.gz
    cd 2018-06-14-13-32-49_GUDHI_2.2.0
    mkdir build
    cd build
    cmake -DPython_ADDITIONAL_VERSIONS=3 ..
    make cython

    pip3 install --upgrade python3-protobuf

    cp -r /gudhi /usr/lib/python3.5/site-packages/gudhi
    cp -r /gudhi /usr/local/lib/python3.5/dist-packages/gudhi

    cp cython/gudhi.cpython-35m-x86_64-linux-gnu.so /usr/lib/python3.5/lib-dynload

    rm -rf /gudhi
```

## Collection

 - Name: [jhamer90811/singularity_imgs](https://github.com/jhamer90811/singularity_imgs)
 - License: None

