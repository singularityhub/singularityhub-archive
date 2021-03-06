---
id: 8320
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "argos_3.0.0-beta52"
commit: "7404c120d63800f47cf9bdf01436e883e5c5d3a1"
version: "4d5c2ddc102fc4c5b1d3be548dcde178"
build_date: "2019-04-10T11:51:47.987Z"
size_mb: 7753
size: 3825016863
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/argos_3.0.0-beta52/2019-04-10-7404c120-4d5c2ddc/4d5c2ddc102fc4c5b1d3be548dcde178.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/argos_3.0.0-beta52/2019-04-10-7404c120-4d5c2ddc/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/argos_3.0.0-beta52/2019-04-10-7404c120-4d5c2ddc/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:argos_3.0.0-beta52

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:argos_3.0.0-beta52
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

    LAST_UPDATED 08-APR-2019

%environment
    ARGOS_LIB_PATH=/usr/local/lib/argos3:/opt/argos3/argos3-examples
    export LD_LIBRARY_PATH=$ARGOS_LIB_PATH:$LD_LIBRARY_PATH
    export PATH=/opt/argos3/argos3-examples:/opt/argos3/argos3-examples/experiments:$PATH

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
    echo " Installing Argos 3.0.0-beta52   "
    echo "================================="

    echo " ** Installing requirements ** "
    apt-get install -y cmake libfreeimage-dev libfreeimageplus-dev qt5-default freeglut3-dev \
            libxi-dev libxmu-dev liblua5.2-dev lua5.2 doxygen graphviz graphviz-dev asciidoc

    cd /opt
    git clone -b 3.0.0-beta52 https://github.com/ilpincy/argos3.git

    cd argos3
    mkdir build_simulator
    cd build_simulator
    cmake -DCMAKE_BUILD_TYPE=Release ../src
    make
    make doc
    make install    

    echo "================================="
    echo " Installing Argos examples   "
    echo "================================="
    cd /opt/argos3
    git clone https://github.com/ilpincy/argos3-examples.git argos3-examples

    cd argos3-examples
    mkdir build
    cd build
    cmake -DCMAKE_BUILD_TYPE=Release ..
    make
    cd ..
    cp -r build/ /usr/local/lib/argos3/

%runscript
    $*
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

