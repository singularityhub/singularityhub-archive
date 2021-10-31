---
id: 3858
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "cryolo_v1_0_0"
commit: "4c5cafc67b9206973fa66aa2faebb4f99dd321e0"
version: "8c38412a9713b1ab180a88ca067fd0dd"
build_date: "2018-08-06T09:55:01.805Z"
size_mb: 8099
size: 4199952415
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/cryolo_v1_0_0/2018-08-06-4c5cafc6-8c38412a/8c38412a9713b1ab180a88ca067fd0dd.simg"
url: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/cryolo_v1_0_0/2018-08-06-4c5cafc6-8c38412a/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/cryolo_v1_0_0/2018-08-06-4c5cafc6-8c38412a/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:cryolo_v1_0_0

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:cryolo_v1_0_0
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://au.archive.ubuntu.com/ubuntu/

%labels
MAINTAINER lance.wilson@monash.edu
HARDWARE gpu


%runscript
    echo "This is what happens when you run the container..."


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
    echo "Installing software"
    echo "*********************************************************"
    wget ftp://ftp.gwdg.de/pub/misc/sphire/crYOLO_V1_0_0/cryolo-1.0.0.tar.gz 
    wget ftp://ftp.gwdg.de/pub/misc/sphire/crYOLO_V1_0_0/cryoloBM-1.0.0.tar.gz
    wget ftp://ftp.gwdg.de/pub/misc/sphire/crYOLO_V1_0_0/gmodel_cryolo_20180621_0734_loss_0102.h5
    pip install numpy
    pip install cryolo-1.0.0.tar.gz
    pip install cryoloBM-1.0.0.tar.gz
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

