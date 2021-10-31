---
id: 3879
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "imod_v4_9_9"
commit: "0dc75873d3c835e21134dd362f1e0d13f0e94d1d"
version: "3396f39b5bace4df0e32444318de9bdd"
build_date: "2019-12-12T06:54:02.781Z"
size_mb: 6080
size: 2877567007
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/imod_v4_9_9/2019-12-12-0dc75873-3396f39b/3396f39b5bace4df0e32444318de9bdd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/imod_v4_9_9/2019-12-12-0dc75873-3396f39b/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/imod_v4_9_9/2019-12-12-0dc75873-3396f39b/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:imod_v4_9_9

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:imod_v4_9_9
```

## Singularity Recipe

```singularity
# Copyright (c) 2015-2016, Gregory M. Kurtzer. All rights reserved.
# 
# "Singularity" Copyright (c) 2016, The Regents of the University of California,
# through Lawrence Berkeley National Laboratory (subject to receipt of any
# required approvals from the U.S. Dept. of Energy).  All rights reserved.

BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://au.archive.ubuntu.com/ubuntu/


%runscript
    echo "IMOD container built for CVL"
    echo "For new versions please contact help@cvl.org.au"
    $*

%environment
    export IMOD_DIR=/usr/local/IMOD
    export IMOD_QTLIBDIR=/usr/local/IMOD/qtlib
    export PATH=/usr/local/IMOD/bin:/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin
    export IMOD_PLUGIN_DIR=/usr/local/IMOD/lib/imodplug
    export IMOD_JAVADIR=/usr/local/java
    export IMOD_CALIB_DIR=/usr/local/ImodCalib

%post
    echo "*********************************************************"
    echo "Setup and display environment"
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
    apt update
    apt upgrade -y
    apt install -y locales wget
    wget https://swift.rc.nectar.org.au:8888/v1/AUTH_810/CVL-Singularity-External-Files/turbovnc_2.1.2_amd64.deb
    dpkg -i turbovnc_2.1.2_amd64.deb
    wget https://swift.rc.nectar.org.au:8888/v1/AUTH_810/CVL-Singularity-External-Files/virtualgl_2.5.2_amd64.deb
    dpkg -i virtualgl_2.5.2_amd64.deb
    apt update
    apt -y upgrade
    locale-gen en_AU.UTF-8
    apt install -y wget ubuntu-desktop vim software-properties-common git cmake default-jre 
    echo "*********************************************************"
    echo "Installing CUDA"
    apt install -y cuda-8-0
    echo "*********************************************************"
    echo "*********************************************************"
    echo "Installing python dependencies"
    apt install -y python-pip python-pyqt5 pyqt5-dev python-tk
    echo "*********************************************************"
    echo "Installing libjpeg dependencies"
    apt install -y libjpeg-turbo8-*
    apt install -y libjpeg-dev
    apt install -y libjpeg8*
    apt install -y libjpeg62*
    echo "*********************************************************"
    echo "Installing software"
    wget https://bio3d.colorado.edu/imod/AMD64-RHEL5/imod_4.9.9_RHEL6-64_CUDA8.0.sh
    chmod +x imod_4.9.9_RHEL6-64_CUDA8.0.sh
    ./imod_4.9.9_RHEL6-64_CUDA8.0.sh -yes
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

