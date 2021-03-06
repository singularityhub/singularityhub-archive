---
id: 7890
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "meshlab-2019.03-cuda-9.0"
commit: "e88be8e4eccc658e702b64c76ac9d65726d65cbb"
version: "d2537d664ff841c6b020c62b88d394c7"
build_date: "2020-09-16T23:57:52.353Z"
size_mb: 7421
size: 3559055391
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/meshlab-2019.03-cuda-9.0/2020-09-16-e88be8e4-d2537d66/d2537d664ff841c6b020c62b88d394c7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/meshlab-2019.03-cuda-9.0/2020-09-16-e88be8e4-d2537d66/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/meshlab-2019.03-cuda-9.0/2020-09-16-e88be8e4-d2537d66/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:meshlab-2019.03-cuda-9.0

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:meshlab-2019.03-cuda-9.0
```

## Singularity Recipe

```singularity
Bootstrap: shub
From:      Characterisation-Virtual-Laboratory/CharacterisationVL-Software:1804-cuda9

%labels
    MAINTAINER_NAME  Jay van Schyndel
    MAINTAINER_EMAIL jay.vanschyndel@monash.edu

    APPLICATION_NAME ubuntu
    APPLICATION_VERSION 18.04

    HARDWARE GPU

    LAST_UPDATED 20-MAR-2019

%environment
    MESHLABPATH=/opt/meshlab/src/distrib/
    export PATH=$MESHLABPATH:$PATH

%post
    echo "*********************************************************"
    echo "Setup and display environment"
    echo "*********************************************************"
    export LC_ALL=en_AU.UTF-8
    export LANGUAGE=en_AU.UTF-8
    export DEBIAN_FRONTEND=noninteractive
    echo $LC_ALL
    echo $LANGUAGE
    echo $DEBIAN_FRONTEND
    echo "*********************************************************"
    echo "Install repositories"
    echo "*********************************************************"
    apt-get install -y software-properties-common
    apt-add-repository -y 'deb http://us.archive.ubuntu.com/ubuntu/ bionic main restricted'
    apt-add-repository -y 'deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates main restricted'
    apt-add-repository -y 'deb http://us.archive.ubuntu.com/ubuntu/ bionic universe'
    apt-add-repository -y 'deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates universe'
    echo "*********************************************************"
    echo "Update repositories and install desktop"
    echo "*********************************************************"
    apt update
    apt upgrade -y
    apt install -y locales
    locale-gen en_AU.UTF-8
   
    echo "================================="
    echo " Installing MeshLab dependancies "
    echo "================================="
    apt -y install git qt5-qmake qtbase5-dev qtchooser qtcreator qtscript5-dev libqt5script5 qt5-default libqt5xmlpatterns5-dev g++ gcc

    echo "================================="
    echo " Clone and build MeshLab         "
    echo "================================="    
    mkdir -p /opt/
    cd /opt

    export MESHLABSHA1=42ef8f6c99e01bee9fd0152edba96dbba310fc29
    export VCGLIBSHA1=91947c0f7e4b634cd67d960acbad6549db50c912
    export QMAKE_FLAGS="-spec linux-g++ CONFIG+=release CONFIG+=qml_release CONFIG+=c++11 QMAKE_CXXFLAGS+=-fPIC QMAKE_CXXFLAGS+=-std=c++11 QMAKE_CXXFLAGS+=-fpermissive INCLUDEPATH+=/usr/include/eigen3 LIBS+=-L/opt/meshlab/lib/linux-g++"
    export MAKE_FLAGS="-j11"

    git clone https://github.com/cnr-isti-vclab/meshlab.git
    cd meshlab
    git checkout $MESHLABSAH1
    cd ..

    git clone https://github.com/cnr-isti-vclab/vcglib.git -b devel
    cd vcglib
    git checkout $VCGLIBSHA1

    #Patching 
    wget -O /tmp/meshlab-2016.12-remove-header.patch https://raw.githubusercontent.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/master/meshlab/meshlab-2016.12-remove-header.patch

    cd /opt
    patch --forward -p1 < /tmp/meshlab-2016.12-remove-header.patch 

    cd meshlab/src/external
    qmake external.pro $QMAKE_FLAGS && make $MAKE_FLAGS

    cd ../common
    qmake common.pro $QMAKE_FLAGS && make $MAKE_FLAGS

    cd ..
    qmake meshlab_mini.pro $QMAKE_FLAGS && make $MAKE_FLAGS

    ##Copy is to ensure files are found, they are in the wrong place.
    cp external/lib/linux/*.a external/lib/linux-g++/

    qmake meshlab_full.pro $QMAKE_FLAGS && make $MAKE_FLAGS

%runscript
    $*
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

