---
id: 8224
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "imagej_1.50e"
commit: "ae1e34c3df3961368dc67433692320e170741acd"
version: "275b29642153f9af421411476190a4a2"
build_date: "2019-04-05T06:18:03.576Z"
size_mb: 3467
size: 1422344223
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/imagej_1.50e/2019-04-05-ae1e34c3-275b2964/275b29642153f9af421411476190a4a2.simg"
url: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/imagej_1.50e/2019-04-05-ae1e34c3-275b2964/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/imagej_1.50e/2019-04-05-ae1e34c3-275b2964/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:imagej_1.50e

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:imagej_1.50e
```

## Singularity Recipe

```singularity
Bootstrap: shub
From:      Characterisation-Virtual-Laboratory/CharacterisationVL-Software:1804

%labels
    MAINTAINER_NAME  Jay van Schyndel
    MAINTAINER_EMAIL jay.vanschyndel@monash.edu

    APPLICATION_NAME ubuntu
    APPLICATION_VERSION 18.04

    HARDWARE CPU

    LAST_UPDATED 27-MAR-2019

%environment
    IMAGEJPATH=/opt/imagej/ImageJ.app
    export PATH=$IMAGEJPATH:$PATH

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
    echo "Installing Java                  "
    echo "================================="
    sudo apt install -y openjdk-8-jre

    echo "================================="
    echo "Downloading ImageJ Linux 64bit     "
    echo "================================="
    cd /tmp
    wget https://downloads.imagej.net/ImageJ2-20160205.zip

    echo "================================="
    echo "Extracting ImageJ Linux 64 bit "
    echo "================================="    
    unzip -d /opt/imagej/ ImageJ2-20160205.zip
    cd /opt
    chmod -R u+rwx,o+rx,g+rx imagej

%runscript
    $*
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

