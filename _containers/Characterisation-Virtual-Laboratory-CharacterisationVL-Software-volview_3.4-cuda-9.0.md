---
id: 7835
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "volview_3.4-cuda-9.0"
commit: "11166864ca4503b4288fbbc4fd372731536289e3"
version: "a85a72c012f57b3cd74ad0fc9957bba0"
build_date: "2019-03-19T05:26:46.835Z"
size_mb: 6413
size: 3084419103
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/volview_3.4-cuda-9.0/2019-03-19-11166864-a85a72c0/a85a72c012f57b3cd74ad0fc9957bba0.simg"
url: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/volview_3.4-cuda-9.0/2019-03-19-11166864-a85a72c0/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/volview_3.4-cuda-9.0/2019-03-19-11166864-a85a72c0/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:volview_3.4-cuda-9.0

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:volview_3.4-cuda-9.0
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

    LAST_UPDATED 19-MAR-2019

%environment
    VOLVIEWPATH=/opt/VolView/bin
    export PATH=$VOLVIEWPATH:$PATH

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
    echo " Downloading VolView 3.4         "
    echo "================================="
    mkdir -p /opt/VolView
    cd /opt/VolView
    wget -O VolView-3.4-Linux-x86_64.sh "https://www.kitware.com/VolView/files/VolView-3.4-Linux-x86_64.sh"

    echo "================================="
    echo " Installing VolView 3.4          "
    echo "================================="    
    chmod 755 VolView-3.4-Linux-x86_64.sh
    ./VolView-3.4-Linux-x86_64.sh --skip-license

%runscript
    $*
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

