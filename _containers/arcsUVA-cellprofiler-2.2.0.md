---
id: 7213
name: "arcsUVA/cellprofiler"
branch: "master"
tag: "2.2.0"
commit: "28426a35b046a7ab6fca8ac156b273291ff125c9"
version: "9402401296ebfb4a07e8c53c8d76f4f2"
build_date: "2019-02-14T21:05:18.255Z"
size_mb: 1974
size: 925454367
sif: "https://datasets.datalad.org/shub/arcsUVA/cellprofiler/2.2.0/2019-02-14-28426a35-94024012/9402401296ebfb4a07e8c53c8d76f4f2.simg"
url: https://datasets.datalad.org/shub/arcsUVA/cellprofiler/2.2.0/2019-02-14-28426a35-94024012/
recipe: https://datasets.datalad.org/shub/arcsUVA/cellprofiler/2.2.0/2019-02-14-28426a35-94024012/Singularity
collection: arcsUVA/cellprofiler
---

# arcsUVA/cellprofiler:2.2.0

```bash
$ singularity pull shub://arcsUVA/cellprofiler:2.2.0
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
        python-h5py        \
        python-mysqldb     \
        python-scipy       \
        python-wxgtk3.0    \
        python-zmq         \
        python-pytest      \
        libcanberra-gtk-module \
        packagekit-gtk3-module

    # CellProfiler
    VERSION=2.2.0
    TARBALL=${VERSION}.tar.gz
    cd /opt
    wget https://github.com/CellProfiler/CellProfiler/archive/${TARBALL}
    tar xzvf ${TARBALL}
    unset JAVA_TOOL_OPTIONS
    cd CellProfiler-${VERSION}
    # python -m pip install --upgrade pip
    pip install \
        numpy==1.12.0 \
        javabridge==1.0.14 \
        matplotlib==2.2.3 \
        Pillow==4.3
    pip install --editable .
    rm /opt/${TARBALL}

%runscript
    exec cellprofiler

%help
This container provides the following applications:
    * CellProfiler 2.2.0
    * Python 2.7
    * Java JDK 8

%environment
    export PATH=/opt/CellProfiler-2.2.0:$PATH
    export JAVA_TOOL_OPTIONS="-Xss1280k $JAVA_TOOL_OPTIONS"

%labels
    AUTHOR khs3z@virginia.edu
```

## Collection

 - Name: [arcsUVA/cellprofiler](https://github.com/arcsUVA/cellprofiler)
 - License: None

