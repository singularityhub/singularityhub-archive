---
id: 4756
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "mantid_v_3_13_0"
commit: "6369a3ae3dc156c27a66e9107fc46cf340abadc0"
version: "8c23d9b7fb952f69c0aa12af1ddf7e43"
build_date: "2020-09-16T23:38:06.410Z"
size_mb: 4101
size: 1704415263
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/mantid_v_3_13_0/2020-09-16-6369a3ae-8c23d9b7/8c23d9b7fb952f69c0aa12af1ddf7e43.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/mantid_v_3_13_0/2020-09-16-6369a3ae-8c23d9b7/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/mantid_v_3_13_0/2020-09-16-6369a3ae-8c23d9b7/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:mantid_v_3_13_0

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:mantid_v_3_13_0
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://au.archive.ubuntu.com/ubuntu/
Include: apt wget sudo vim build-essential git cmake software-properties-common

%labels
MAINTAINER lance.wilson@monash.edu
HARDWARE cpu

%environment
    MANTIDPATH=/opt/Mantid/bin
    PV_PLUGIN_PATH=/opt/Mantid//
    PATH=$PATH:$MANTIDPATH
    export MANTIDPATH PV_PLUGIN_PATH PATH


%runscript
    echo "Mantid container built for CVL"
    echo "For new versions please contact help@cvl.org.au"
    MantidPlot

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
    apt-add-repository "deb [arch=amd64] http://apt.isis.rl.ac.uk xenial main"
    # add the signing key
    wget -O - http://apt.isis.rl.ac.uk/2E10C193726B7213.asc | apt-key add -
    apt-add-repository ppa:mantid/mantid
    echo "*********************************************************"
    echo "Update repositories and install desktop"
    echo "*********************************************************"
    apt update
    apt upgrade -y
    apt install -y locales
    locale-gen en_AU.UTF-8
    apt install -y ubuntu-desktop 
    echo "*********************************************************"
    echo "Installing software"
    echo "*********************************************************"
    apt install -y mantid
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

