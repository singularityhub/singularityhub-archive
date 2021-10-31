---
id: 3969
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "dragondisk_v1_0_5"
commit: "dd8338643f5c9167f49453a86fc355ac7f67e69d"
version: "8e11918b6c92e25085ba4ae33bed4ebb"
build_date: "2018-08-14T08:40:39.557Z"
size_mb: 414
size: 166264863
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/dragondisk_v1_0_5/2018-08-14-dd833864-8e11918b/8e11918b6c92e25085ba4ae33bed4ebb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/dragondisk_v1_0_5/2018-08-14-dd833864-8e11918b/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/dragondisk_v1_0_5/2018-08-14-dd833864-8e11918b/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:dragondisk_v1_0_5

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:dragondisk_v1_0_5
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
    echo "DragonDisk container built for CVL"
    echo "For new versions please contact help@cvl.org.au"
    dragondisk

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
    echo "Install repositories and dependencies"
    echo "*********************************************************"
    sed -i 's/main/main restricted universe multiverse/g' /etc/apt/sources.list
    echo "*********************************************************"
    echo "Update repositories and install desktop"
    apt update
    apt upgrade -y
    apt install -y locales
    locale-gen en_AU.UTF-8
    apt install -y wget vim libqt4-dbus libqt4-network libqt4-xml libqtcore4 libqtgui4
    echo "*********************************************************"
    echo "Installing software"
    wget http://download.dragondisk.com/dragondisk_1.0.5-0ubuntu_amd64.deb
    dpkg -i dragondisk_1.0.5-0ubuntu_amd64.deb
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

