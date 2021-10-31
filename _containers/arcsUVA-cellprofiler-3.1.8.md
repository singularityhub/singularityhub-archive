---
id: 7205
name: "arcsUVA/cellprofiler"
branch: "master"
tag: "3.1.8"
commit: "abf5bad48f285ac6fef5eb3b16afd98d88ea52e6"
version: "518d2cef91454e323dd16d24d99ca01d"
build_date: "2020-06-16T23:23:59.119Z"
size_mb: 2000
size: 948002847
sif: "https://datasets.datalad.org/shub/arcsUVA/cellprofiler/3.1.8/2020-06-16-abf5bad4-518d2cef/518d2cef91454e323dd16d24d99ca01d.simg"
url: https://datasets.datalad.org/shub/arcsUVA/cellprofiler/3.1.8/2020-06-16-abf5bad4-518d2cef/
recipe: https://datasets.datalad.org/shub/arcsUVA/cellprofiler/3.1.8/2020-06-16-abf5bad4-518d2cef/Singularity
collection: arcsUVA/cellprofiler
---

# arcsUVA/cellprofiler:3.1.8

```bash
$ singularity pull shub://arcsUVA/cellprofiler:3.1.8
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
        pillow==4.3 \
        networkx==2.2 # has to be <2.3 for Python 2.7

    pip install --editable .
    rm /opt/${TARBALL}

    #pip install \
    #    javabridge==1.0.14 \
    #    numpy==1.12

%runscript
    exec cellprofiler

%help
This container provides the following applications:
    * CellProfiler 3.1.8
    * Python 2.7
    * Java JDK 8

%environment
    export PATH=/opt/CellProfiler-3.1.8:$PATH
    export JAVA_TOOL_OPTIONS="-Xss1280k $JAVA_TOOL_OPTIONS"
    export LC_ALL=C

%labels
    AUTHOR khs3z@virginia.edu
```

## Collection

 - Name: [arcsUVA/cellprofiler](https://github.com/arcsUVA/cellprofiler)
 - License: None

