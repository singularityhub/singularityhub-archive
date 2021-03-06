---
id: 7921
name: "ArjitM/CellMorphology"
branch: "master"
tag: "cellprof2"
commit: "e65d26cd4ce36f696b89b754fef33a68bb985244"
version: "ced1fc4c2506ca0c6e18ba4ef14ad967"
build_date: "2020-07-14T13:59:54.321Z"
size_mb: 2008
size: 949112863
sif: "https://datasets.datalad.org/shub/ArjitM/CellMorphology/cellprof2/2020-07-14-e65d26cd-ced1fc4c/ced1fc4c2506ca0c6e18ba4ef14ad967.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ArjitM/CellMorphology/cellprof2/2020-07-14-e65d26cd-ced1fc4c/
recipe: https://datasets.datalad.org/shub/ArjitM/CellMorphology/cellprof2/2020-07-14-e65d26cd-ced1fc4c/Singularity
collection: ArjitM/CellMorphology
---

# ArjitM/CellMorphology:cellprof2

```bash
$ singularity pull shub://ArjitM/CellMorphology:cellprof2
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

