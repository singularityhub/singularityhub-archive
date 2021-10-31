---
id: 4618
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "quit_2.0.2"
commit: "0dc75873d3c835e21134dd362f1e0d13f0e94d1d"
version: "d518b0e405524d518cf91c6b13993775"
build_date: "2019-12-12T06:54:02.900Z"
size_mb: 6199
size: 2957131807
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/quit_2.0.2/2019-12-12-0dc75873-d518b0e4/d518b0e405524d518cf91c6b13993775.simg"
url: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/quit_2.0.2/2019-12-12-0dc75873-d518b0e4/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/quit_2.0.2/2019-12-12-0dc75873-d518b0e4/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:quit_2.0.2

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:quit_2.0.2
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

%environment

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
    echo "Installing python dependencies"
    echo "*********************************************************"
    cd /tmp/
    wget https://github.com/spinicist/QUIT/releases/download/v2.0.2/QUIT-2.0.1-Linux.deb
    dpkg -i QUIT-2.0.1-Linux.deb
    apt upgrade -y 

%runscript
    $*
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

