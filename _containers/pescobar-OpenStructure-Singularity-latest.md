---
id: 1741
name: "pescobar/OpenStructure-Singularity"
branch: "master"
tag: "latest"
commit: "a9e58280820058e06195506b7d7e72aceedcfb1e"
version: "3f2a8823b2f83e70be05dce0c4cdb970"
build_date: "2018-03-01T23:01:16.601Z"
size_mb: 1391
size: 421580831
sif: "https://datasets.datalad.org/shub/pescobar/OpenStructure-Singularity/latest/2018-03-01-a9e58280-3f2a8823/3f2a8823b2f83e70be05dce0c4cdb970.simg"
url: https://datasets.datalad.org/shub/pescobar/OpenStructure-Singularity/latest/2018-03-01-a9e58280-3f2a8823/
recipe: https://datasets.datalad.org/shub/pescobar/OpenStructure-Singularity/latest/2018-03-01-a9e58280-3f2a8823/Singularity
collection: pescobar/OpenStructure-Singularity
---

# pescobar/OpenStructure-Singularity:latest

```bash
$ singularity pull shub://pescobar/OpenStructure-Singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:7.4.1708

%post
    
    # DEFINE SOME ENV VARS USED DURING THE IMAGE BUILD
    ##########################
    export OPENSTRUCTURE_VERSION="1.7.1"
    export OST_ROOT=/usr/local
    export PYTHONPATH=/usr/local/lib64/python2.7/site-packages
    export EIGEN_VERSION="3.3.4"
    export OPENMM_VERSION="6.1"
    export OPENMM_INCLUDE_PATH=/usr/local/openmm/include/
    export OPENMM_LIB_PATH=/usr/local/openmm/lib/
    export SRC_FOLDER="/usr/local/src"
    export CPUS_FOR_MAKE=1

    # INSTALL SYSTEM DEPS
    ##########################
    yum makecache fast
    yum -y install epel-release
    yum -y install \
    boost-devel \
    bzip2 \
    cmake \
    doxygen \
    fftw-devel \
    fftw-static \
    file \
    freetype-devel \
    gcc \
    gcc-c++ \
    gcc-gfortran \
    glibc-common \
    glibc-devel \
    libjpeg-turbo-devel \
    libpng-devel \
    libtiff-devel \
    make \
    mesa-libGL-devel \
    mesa-libGLU-devel \
    numpy \
    PyQt4 \
    python-devel \
    qt-devel \
    strace \
    swig \
    wget

    # COPY EIGEN HEADER FILES TO /usr/local/include/Eigen
    #########################
    cd ${SRC_FOLDER}
    if [ ! -f eigen-${EIGEN_VERSION}.tar.bz2 ]; then
        wget -O eigen-${EIGEN_VERSION}.tar.bz2 -nc http://bitbucket.org/eigen/eigen/get/${EIGEN_VERSION}.tar.bz2
        mkdir -p ${SRC_FOLDER}/eigen-${EIGEN_VERSION}
        tar xf eigen-${EIGEN_VERSION}.tar.bz2 -C ${SRC_FOLDER}/eigen-${EIGEN_VERSION} --strip-components=1
        cp -r ${SRC_FOLDER}/eigen-${EIGEN_VERSION}/Eigen/ /usr/local/include/
    fi
   
    # COMPILE OPENMM FROM SOURCES. INSTALL TO /usr/local
    ############################ 
    cd ${SRC_FOLDER}
    if [ ! -f openmm-${OPENMM_VERSION}.tar.gz ]; then
        wget -O openmm-${OPENMM_VERSION}.tar.gz -nc https://github.com/pandegroup/openmm/archive/${OPENMM_VERSION}.tar.gz
        mkdir ${SRC_FOLDER}/openmm-${OPENMM_VERSION}
        tar xf openmm-${OPENMM_VERSION}.tar.gz -C ${SRC_FOLDER}/openmm-${OPENMM_VERSION} --strip-components=1
        mkdir -p ${SRC_FOLDER}/openmm-${OPENMM_VERSION}/build && cd ${SRC_FOLDER}/openmm-${OPENMM_VERSION}/build
        cmake .. && make -j $CPUS_FOR_MAKE && make install
        cd ${SRC_FOLDER}/openmm-${OPENMM_VERSION}/build/python && python setup.py build && python setup.py install
    fi

    # COMPILE OST FROM SOURCES. INSTALL TO /usr/local
    ###########################
    cd ${SRC_FOLDER}
    if [ ! -f openstructure-${OPENSTRUCTURE_VERSION}.tar.gz ]; then
        wget -O openstructure-${OPENSTRUCTURE_VERSION}.tar.gz -nc https://git.scicore.unibas.ch/schwede/openstructure/repository/${OPENSTRUCTURE_VERSION}/archive.tar.gz
        mkdir openstructure-${OPENSTRUCTURE_VERSION}
        tar xf openstructure-${OPENSTRUCTURE_VERSION}.tar.gz -C ${SRC_FOLDER}/openstructure-${OPENSTRUCTURE_VERSION} --strip-components=1
        mkdir -p ${SRC_FOLDER}/openstructure-${OPENSTRUCTURE_VERSION}/build && cd ${SRC_FOLDER}/openstructure-${OPENSTRUCTURE_VERSION}/build
        cmake .. \
        -DENABLE_MM=1 \
        -DOPEN_MM_LIBRARY=/usr/local/openmm/lib/libOpenMM.so \
        -DOPEN_MM_PLUGIN_DIR=/usr/local/openmm/lib/plugins/ \
        -DOPEN_MM_INCLUDE_DIR=/usr/local/openmm/include/ \
        -DCOMPILE_TMTOOLS=1 \
        -DENABLE_GFX=ON \
        -DENABLE_GUI=OFF \
        -DUSE_NUMPY=1 \
        -DUSE_RPATH=1 \
        -DEIGEN3_INCLUDE_DIR=/usr/local/include/Eigen/ \
        -DFFTW_LIBRARY=/usr/lib64/libfftw3f.a \
        -DQT_QMAKE_EXECUTABLE=/usr/lib64/qt4/bin/qmake \
        -DOPTIMIZE=1
        make -j ${CPUS_FOR_MAKE}
        make check
        make install
    fi

    yum clean all
    rm -rf /var/cache/yum

%environment
    export OST_ROOT=/usr/local
    export PYTHONPATH=/usr/local/lib64/python2.7/site-packages
    export LC_ALL="en_US.UTF-8"

%apprun chemdict_tool
    /usr/local/bin/chemdict_tool

%apprun lddt
    /usr/local/bin/lddt

%apprun molck
    /usr/local/bin/molck

%apprun ost
    /usr/local/bin/ost

%apprun tmalign
    /usr/local/bin/tmalign

%apprun tmscore
    /usr/local/bin/tmscore

%runscript
    /usr/local/bin/ost
```

## Collection

 - Name: [pescobar/OpenStructure-Singularity](https://github.com/pescobar/OpenStructure-Singularity)
 - License: None

