---
id: 4620
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "chimerax_06"
commit: "81a8ecdf6c8a2459891e3148d0da07351ef94b58"
version: "9c0fa20945cf5e767263d4b65d617031"
build_date: "2020-09-16T23:30:08.628Z"
size_mb: 6075
size: 2926747679
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/chimerax_06/2020-09-16-81a8ecdf-9c0fa209/9c0fa20945cf5e767263d4b65d617031.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/chimerax_06/2020-09-16-81a8ecdf-9c0fa209/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/chimerax_06/2020-09-16-81a8ecdf-9c0fa209/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:chimerax_06

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:chimerax_06
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
MirrorURL: http://us.archive.ubuntu.com/ubuntu/
OSVersion:  xenial
Include: apt wget sudo vim build-essential git sudo software-properties-common

%labels
MAINTAINER jafar.lie@monash.edu
HARDWARE gpu


%runscript
    echo "This is what happens when you run the container..."
    $*

%environment
    DRISTHI_PATH=/opt/drishti/bin
    export PATH=$DRISTHI_PATH:$PATH

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
    sed -i 's/main/main restricted universe multiverse/g' /etc/apt/sources.list
    echo "deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/cuda.list
    apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
    echo "*********************************************************"
    echo "Update repositories and install desktop"
    echo "*********************************************************"
    apt update
    apt upgrade -y
    apt install -y locales
    locale-gen en_AU.UTF-8
    apt install -y wget ubuntu-desktop vim software-properties-common git cmake 
    echo "*********************************************************"
    echo "Installing CUDA"
    echo "*********************************************************"
    apt install -y cuda-9-0
    echo "*********************************************************"
    echo "Installing python dependencies"
    echo "*********************************************************"
    apt install -y python-pip python-pyqt5 pyqt5-dev python-tk
    echo "*********************************************************"
    echo "Installing vglrun and TurboVNC"
    echo "*********************************************************"
    wget https://swift.rc.nectar.org.au:8888/v1/AUTH_810/CVL-Singularity-External-Files/turbovnc_2.1.2_amd64.deb
    dpkg -i turbovnc_2.1.2_amd64.deb
    wget https://swift.rc.nectar.org.au:8888/v1/AUTH_810/CVL-Singularity-External-Files/virtualgl_2.5.2_amd64.deb
    dpkg -i virtualgl_2.5.2_amd64.deb
    apt update
    apt -y upgrade
    echo "*********************************************************"
    echo "Installing dristhi requirement"
    echo "*********************************************************"
    apt -y install qt5-qmake
    apt -y install qtmultimedia5-dev libqt5multimediawidgets5 libqt5multimedia5-plugins libqt5multimedia5
    apt -y install libglew-dev glew-utils
    apt -y install libqglviewer-dev
    apt -y install libnetcdf-dev
    apt -y install libnetcdf-cxx-legacy-dev
    apt -y install freeglut3-dev
    echo "*********************************************************"
    echo "Installing drishti requirement"
    echo "*********************************************************"
    mkdir -p /opt/
    cd /opt/
    git clone https://github.com/nci/drishti.git
    cd drishti/drishti
    qmake -qt=5
    make -j 4
    echo "*********************************************************"
    echo "All Done"
    echo "*********************************************************"
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

