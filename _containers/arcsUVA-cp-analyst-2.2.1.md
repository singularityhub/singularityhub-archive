---
id: 6863
name: "arcsUVA/cp-analyst"
branch: "master"
tag: "2.2.1"
commit: "d692951fcd0d78e4d1fb5d7a2499a9df0edcc7cf"
version: "9aa61ea85aaa38616427be9aa418c760"
build_date: "2019-02-04T16:33:11.315Z"
size_mb: 1464
size: 562909215
sif: "https://datasets.datalad.org/shub/arcsUVA/cp-analyst/2.2.1/2019-02-04-d692951f-9aa61ea8/9aa61ea85aaa38616427be9aa418c760.simg"
url: https://datasets.datalad.org/shub/arcsUVA/cp-analyst/2.2.1/2019-02-04-d692951f-9aa61ea8/
recipe: https://datasets.datalad.org/shub/arcsUVA/cp-analyst/2.2.1/2019-02-04-d692951f-9aa61ea8/Singularity
collection: arcsUVA/cp-analyst
---

# arcsUVA/cp-analyst:2.2.1

```bash
$ singularity pull shub://arcsUVA/cp-analyst:2.2.1
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
        libpng-dev         \
        openjdk-8-jdk      \
        python-dev         \
        python-pip         \
        python-matplotlib  \
        python-sqlite      \
        python-mysqldb     \
        python-wxgtk3.0    \
        libcanberra-gtk-module \
        packagekit-gtk3-module

    # CellProfiler-Analyst
    VERSION=2.2.1
    TARBALL=${VERSION}.tar.gz
    cd /opt
    wget https://github.com/CellProfiler/CellProfiler-Analyst/archive/${TARBALL}
    tar xzvf ${TARBALL}
    unset JAVA_TOOL_OPTIONS
    cd CellProfiler-Analyst-${VERSION}
    pip install \
        mock \
        zmq \
        h5py \
        scipy \
        pandas \
        seaborn \
        scikit-learn \
        numpy==1.14.0
    pip install javabridge==1.0.14 \
        bioformats \
        verlib
    sed -i '1 i\#!/usr/bin/env python2' CellProfiler-Analyst.py 
    chmod +x CellProfiler-Analyst.py
    rm /opt/${TARBALL}

%runscript
    exec CellProfiler-Analyst.py

%help
This container provides the following applications:
    * CellProfiler Analyst 2.2.1
    * Python 2.7
    * Java JDK 8

%environment
    export PATH=/opt/CellProfiler-Analyst-2.2.1:$PATH
    export JAVA_TOOL_OPTIONS="-Xss1280k $JAVA_TOOL_OPTIONS"

%labels
    AUTHOR khs3z@virginia.edu
```

## Collection

 - Name: [arcsUVA/cp-analyst](https://github.com/arcsUVA/cp-analyst)
 - License: None

