---
id: 12620
name: "akojamil/singularity_chroma3"
branch: "master"
tag: "latest"
commit: "095c5cc22078e25a778e4877f4d808ac0150516d"
version: "ff981bc31f7e70fdc0f78091bdd1e412"
build_date: "2020-03-28T20:47:31.114Z"
size_mb: 8566.0
size: 3551227935
sif: "https://datasets.datalad.org/shub/akojamil/singularity_chroma3/latest/2020-03-28-095c5cc2-ff981bc3/ff981bc31f7e70fdc0f78091bdd1e412.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/akojamil/singularity_chroma3/latest/2020-03-28-095c5cc2-ff981bc3/
recipe: https://datasets.datalad.org/shub/akojamil/singularity_chroma3/latest/2020-03-28-095c5cc2-ff981bc3/Singularity
collection: akojamil/singularity_chroma3
---

# akojamil/singularity_chroma3:latest

```bash
$ singularity pull shub://akojamil/singularity_chroma3:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.1-devel-ubuntu18.04 

%labels
    AUTHOR ako.jamil@yale.edu
    VERSION 1.0

%environment
    export APP_DIR=/chroma/chroma_env
    . /setup-chroma.sh  
 
%post
    export DEBIAN_FRONTEND=noninteractive

    #INSTALL PACKAGES
    apt-get -y update && apt-get -y install python3.7 python3-pip wget cmake nano git
    apt-get -y update && apt-get install -y libboost-all-dev

    #DOWNLOAD FILES
    git clone https://cd1806ae4efa9ae63df806cbbff374fe5e14b0a9@github.com/akojamil/singularity_chroma3.git
    cp singularity_chroma3/setup-chroma.sh /
    cp singularity_chroma3/g4py.4.10.05.p01.patch /
    rm -rf singularity_chroma3

    #SWITCH TO PYTHON 3
    rm /usr/bin/python-config
    ln -s /usr/bin/python3.6-config /usr/bin/python-config
    rm /usr/bin/python
    ln -s /usr/bin/python3 /usr/bin/python

    rm -f /usr/lib/x86_64-linux-gnu/libboost_python-py27.so.1.65.1
    ln -s /usr/lib/x86_64-linux-gnu/libboost_python3-py36.so.1.65.1 /usr/lib/x86_64-linux-gnu/libboost_python-py27.so.1.65.1
    rm -f /usr/lib/x86_64-linux-gnu/libboost_numpy-py27.so.1.65.1
    ln -s /usr/lib/x86_64-linux-gnu/libboost_numpy3-py36.so.1.65.1 /usr/lib/x86_64-linux-gnu/libboost_numpy-py27.so.1.65.1

    rm /usr/lib/x86_64-linux-gnu/libboost_python.a
    rm /usr/lib/x86_64-linux-gnu/libboost_python.so
    ln -s /usr/lib/x86_64-linux-gnu/libboost_python3-py36.a /usr/lib/x86_64-linux-gnu/libboost_python.a
    ln -s /usr/lib/x86_64-linux-gnu/libboost_python3-py36.so /usr/lib/x86_64-linux-gnu/libboost_python.so

    #INSTALL PACKAGES CONTINUED
    pip3 install tables uncertainties numpy matplotlib scipy h5py sphinx pytest pyyaml pygame
    apt-get -y install python3-dev python3-tk build-essential xorg-dev libglu1-mesa-dev uuid-dev liblapack-dev libatlas-base-dev libbz2-dev freeglut3-dev
    apt-get -y install libsdl1.2-dev libxerces-c-dev mesa-common-dev 
    apt-get -y install libx11-dev libxpm-dev libxft-dev libxext-dev libgsl-dev libpng-dev libjpeg-dev gcc g++    

    #SETUP ENVIRONMENT
    echo "[ui]\ntls = False" > $HOME/.hgrc
    export APP_DIR=/chroma/chroma_env
    mkdir -p $APP_DIR
    mkdir -p $APP_DIR/bin/
    mkdir -p $APP_DIR/local/
    mkdir -p $APP_DIR/src/
    export PATH=/usr/local/cuda/bin:/chroma/chroma_env/bin:$PATH
    export LD_LIBRARY_PATH=/usr/local/cuda/lib64/:$LD_LIBRARY_PATH

    touch .aksetup-defaults.py
    echo "BOOST_INC_DIR = ['/usr/include/boost']" >> .aksetup-defaults.py
    echo "BOOST_LIB_DIR = ['/usr/lib/x86_64-linux-gnu']" >> .aksetup-defaults.py
    echo "BOOST_PYTHON_LIBNAME = ['boost_python3-py36']" >> .aksetup-defaults.py 

    # Install ROOT
    # cd $APP_DIR/src/
    # wget https://root.cern/download/root_v6.18.04.source.tar.gz
    # tar xf root_v6.18.04.source.tar.gz
    # rm root_v6.18.04.source.tar.gz
    # mkdir -p $APP_DIR/src/build-root
    # cd $APP_DIR/src/build-root
    # cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$APP_DIR/lib/python/site-packages -Dminuit2=ON -Droofit=ON $APP_DIR/src/root-6.18.04
    # make -j8
    # make -j8 install
    # rm -rf $APP_DIR/src/root-6.18.04

    #Install GEANT4
    cd $APP_DIR/src/
    wget https://geant4-data.web.cern.ch/geant4-data/releases/geant4.10.05.p01.tar.gz
    tar xvf geant4.10.05.p01.tar.gz
    rm -f geant4.10.05.p01.tar.gz
    mkdir -p $APP_DIR/src/geant4.10.05.p01-build
    cd $APP_DIR/src/geant4.10.05.p01-build
    cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$APP_DIR -DGEANT4_INSTALL_DATA=ON -DGEANT4_USE_GDML=ON -DGEANT4_USE_RAYTRACER_X11=OFF -DGEANT4_USE_SYSTEM_EXPAT=OFF  -DGEANT4_USE_OPENGL_X11=ON ../geant4.10.05.p01
    make -j8
    make -j8 install

    #Install g4py 
    cd $APP_DIR/src/geant4.10.05.p01
    cp /g4py.4.10.05.p01.patch ./
    git apply g4py.4.10.05.p01.patch
    mkdir -p $APP_DIR/src/g4py-build
    cd $APP_DIR/src/g4py-build
    cmake -DCMAKE_BUILD_TYPE=Release -DGEANT4_INSTALL=$APP_DIR/src -DCMAKE_INSTALL_PREFIX=$APP_DIR $APP_DIR/src/geant4.10.05.p01/environments/g4py
    make -j8
    sed -i 's/install: preinstall/install:/' Makefile
    find . -name '*.cmake' -exec sed -i -n -E '/\.pyc|\.pyo/!p' {} \;
    sed -i -E 's/(.*G4LossTableManager.Instance.*)/#\1/' source/python3/__init__.py
    make -j8 install
    rm -rf $APP_DIR/src/geant4.10.05.p01

    #Install Chroma 
    ln -s $APP_DIR/lib $APP_DIR/local/lib
    cd $APP_DIR 
    pip3 install -e git+https://github.com/BenLand100/chroma.git#egg=Chroma
```

## Collection

 - Name: [akojamil/singularity_chroma3](https://github.com/akojamil/singularity_chroma3)
 - License: None

