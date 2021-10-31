---
id: 7176
name: "mherkazandjian/ismcpak"
branch: "alpha-master"
tag: "latest"
commit: "5450170763a62a29af77e95c91421680b98836f6"
version: "8d45fc5a4d06798b99ceca7958d60edf"
build_date: "2019-02-14T21:05:11.723Z"
size_mb: 2423
size: 713211935
sif: "https://datasets.datalad.org/shub/mherkazandjian/ismcpak/latest/2019-02-14-54501707-8d45fc5a/8d45fc5a4d06798b99ceca7958d60edf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mherkazandjian/ismcpak/latest/2019-02-14-54501707-8d45fc5a/
recipe: https://datasets.datalad.org/shub/mherkazandjian/ismcpak/latest/2019-02-14-54501707-8d45fc5a/Singularity
collection: mherkazandjian/ismcpak
---

# mherkazandjian/ismcpak:latest

```bash
$ singularity pull shub://mherkazandjian/ismcpak:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%runscript
    bash

%environment
    export PATH=/prerequisites/bin:${PATH}
    export LD_LIBRARY_PATH=/prerequisites/lib:${LD_LIBRARY_PATH}
    export PYTHONPATH=/prerequisites/python2.7/site-packages:/ism/amuse-11.2/test:/ism/amuse-11.2/src:${PYTHONPATH}
    export AMUSE_DIR=/ism/amuse-11.2

%post
    sed -i 's/$/ universe/' /etc/apt/sources.list
    apt-get update
    apt-get install -y --no-install-recommends locales
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    locale-gen en_US.utf8
    /usr/sbin/update-locale LANG=en_US.UTF-8
    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8
    apt-get install -y wget bzip2 zip
    apt-get -y install emacs vim
    apt-get -y install build-essential checkinstall
    apt-get install -y \
         libreadline-gplv2-dev \
         libncursesw5-dev \
         libssl-dev \
         libsqlite3-dev \
         tk-dev \
         libgdbm-dev \
         libc6-dev \
         libbz2-dev

    mkdir -p /prerequisites/install

    # download and install python
    cd /prerequisites/install
    wget https://www.python.org/ftp/python/2.7.15/Python-2.7.15.tgz
    tar -xzvf Python-2.7.15.tgz
    cd Python-2.7.15
    ./configure --prefix=/prerequisites --enable-shared  --enable-unicode=ucs4
    make -j8
    make install
    rm -fr Python-2.7.15

    export PATH=/prerequisites/bin:${PATH}
    export LD_LIBRARY_PATH=/prerequisites/lib:${LD_LIBRARY_PATH}
    export AMUSE_DIR=/ism/amuse-11.2

    # download and install easy_install, pip, pipenv
    cd /prerequisites/install
    wget https://files.pythonhosted.org/packages/c2/f7/c7b501b783e5a74cf1768bc174ee4fb0a8a6ee5af6afa92274ff964703e0/setuptools-40.8.0.zip
    unzip setuptools-40.8.0.zip
    cd setuptools-40.8.0
    python setup.py install
    easy_install pip==19.0.2
    pip install pipenv==2018.11.26
    cd /

    rm -fr /prerequisites/install/*

    # install the amuse prerequisites
    apt-get install -y \
         git \
         curl \
         gfortran \
         mpich \
         libmpich-dev \
         libgsl-dev \
         cmake \
         libfftw3-3 \
         libfftw3-dev \
         libgmp3-dev \
         libmpfr4 \
         libmpfr-dev \
         libhdf5-serial-dev \
         hdf5-tools \
         gettext

    apt-get clean

    pip install nose==1.3.7
    pip install numpy==1.16.1
    pip install docutils==0.14
    pip install h5py==2.9.0
    pip install mpi4py==3.0.0
    pip install cython==0.29.5
    pip install ipython==5.8.0
    pip install matplotlib==2.2.3

    # download and configure and build amuse
    mkdir /ism
    chmod 777 /ism
    cd /ism
    wget http://www.amusecode.org/releases/amuse-11.2.tar.gz
    tar -xzvf amuse-11.2.tar.gz
    rm -f amuse-11.2.tar.gz
    cd amuse-11.2
    ./configure
    make clean
    make

    # download the ismcpak project
    cd /ism
    git clone https://github.com/mherkazandjian/ismcpak.git
    cd ismcpak
    git checkout alpha-master
    cd ..
    ln -s $PWD/ismcpak/oneSided $PWD/amuse-11.2/src/amuse/community/pdr
    cd /ism/amuse-11.2/src/amuse/community/pdr
    make all

    # setup the dirs for a first quick run
    mkdir -p /ism/runs/tests/oneSided/single_mesh/meshes

    # to test the build/config
    #cd /ism/ismcpak/tests
    #mpiexec python run_singleMesh.py
```

## Collection

 - Name: [mherkazandjian/ismcpak](https://github.com/mherkazandjian/ismcpak)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

