---
id: 7905
name: "ArjitM/CellMorphology"
branch: "master"
tag: "cellprof.def"
commit: "2b6e24228bcad44d2d159e79a1c1014a2a73d6ff"
version: "32f7e86ebc7939ad37b68c372f954ac0"
build_date: "2019-03-23T22:36:00.932Z"
size_mb: 2004
size: 949452831
sif: "https://datasets.datalad.org/shub/ArjitM/CellMorphology/cellprof.def/2019-03-23-2b6e2422-32f7e86e/32f7e86ebc7939ad37b68c372f954ac0.simg"
url: https://datasets.datalad.org/shub/ArjitM/CellMorphology/cellprof.def/2019-03-23-2b6e2422-32f7e86e/
recipe: https://datasets.datalad.org/shub/ArjitM/CellMorphology/cellprof.def/2019-03-23-2b6e2422-32f7e86e/Singularity
collection: ArjitM/CellMorphology
---

# ArjitM/CellMorphology:cellprof.def

```bash
$ singularity pull shub://ArjitM/CellMorphology:cellprof.def
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:xenial
IncludeCmd: yes

%post
    apt-get update
    apt-get -y upgrade
    apt-get -y install     \
        build-essential    \
        cython             \
        git                \
        wget               \
        libmysqlclient-dev \
        libhdf5-dev        \
        libxml2-dev        \
        libxslt1-dev       \
        openjdk-8-jdk      \
        python-dev         \
        python-pip         \
        python-vigra       \
        python-wxgtk3.0    \
        python-zmq         \
        python-pytest      \
        libcanberra-gtk-module \
        packagekit-gtk3-module
    
    # CellProfiler
    VERSION=3.1.8
    TARBALL=v${VERSION}.tar.gz
    cd /opt
    wget https://github.com/CellProfiler/CellProfiler/archive/${TARBALL}
    tar xzvf ${TARBALL}
    unset JAVA_TOOL_OPTIONS
    cd CellProfiler-${VERSION}

    pip install \
        boto3==1.9.60 \
        centrosome==1.1.6 \
        docutils==0.14 \
        h5py==2.8.0 \
        inflect==2.1.0 \
        javabridge==1.0.18 \
        joblib==0.13.0 \
        mahotas==1.4.5 \
        matplotlib==2.2.3 \
        mysqlclient==1.3.13 \
        numpy==1.15.4 \
        prokaryote==2.4.1 \
        python-bioformats==1.5.2 \
        pyzmq==15.3.0 \
        raven==6.9.0 \
        requests==2.20.1 \
        scikit-image==0.14.0 \
        scikit-learn==0.20.1 \
        scipy==1.1.0 \
        six==1.11.0 \
        pillow==4.3

    pip install --editable .
    rm /opt/${TARBALL}

    #pip install \
    #    javabridge==1.0.14 \
    #    numpy==1.12

%runscript
    exec cellprofiler

%help
This container provides the following applications:
    * CellProfiler 3.0.0
    * Python 2.7
    * Java JDK 8

%environment
    mkdir /global
    mkdir /global/scratch
    mkdir /global/home
    mkdir /global/home/users
    mkdir /global/home/users/arjitmisra
    export PATH=/opt/CellProfiler-3.0.0:$PATH
    export JAVA_TOOL_OPTIONS="-Xss1280k $JAVA_TOOL_OPTIONS"
    export LC_ALL=C
```

## Collection

 - Name: [ArjitM/CellMorphology](https://github.com/ArjitM/CellMorphology)
 - License: None

