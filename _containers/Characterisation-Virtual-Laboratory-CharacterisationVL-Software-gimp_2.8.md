---
id: 6193
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "gimp_2.8"
commit: "0dc75873d3c835e21134dd362f1e0d13f0e94d1d"
version: "ad692d44443dcacf2f754951e5eb5ce8"
build_date: "2019-12-12T06:54:02.723Z"
size_mb: 6083
size: 2936332319
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/gimp_2.8/2019-12-12-0dc75873-ad692d44/ad692d44443dcacf2f754951e5eb5ce8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/gimp_2.8/2019-12-12-0dc75873-ad692d44/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/gimp_2.8/2019-12-12-0dc75873-ad692d44/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:gimp_2.8

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:gimp_2.8
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
MirrorURL: http://us.archive.ubuntu.com/ubuntu/
OSVersion:  xenial
Include: apt wget sudo vim build-essential git sudo software-properties-common
 
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

    echo "================================"
    echo "Installing Gimp                 "
    echo "================================"
    apt -y update
    apt -y upgrade
    apt -y install gimp

%runscript
    $*
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

