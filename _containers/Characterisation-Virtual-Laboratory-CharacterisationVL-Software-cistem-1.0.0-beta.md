---
id: 8997
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "cistem-1.0.0-beta"
commit: "fdb426a7b3fe1e943520984885c3b5b31b44e3b7"
version: "3ecc91c4e4e0397d10e22f461c131f06"
build_date: "2020-09-16T23:38:32.334Z"
size_mb: 4656
size: 2125987871
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/cistem-1.0.0-beta/2020-09-16-fdb426a7-3ecc91c4/3ecc91c4e4e0397d10e22f461c131f06.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/cistem-1.0.0-beta/2020-09-16-fdb426a7-3ecc91c4/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/cistem-1.0.0-beta/2020-09-16-fdb426a7-3ecc91c4/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:cistem-1.0.0-beta

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:cistem-1.0.0-beta
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

    LAST_UPDATED 10-MAY-2019

%environment
    CISTEM_PATH="/opt/cistem-1.0.0-beta"
    export PATH="$CISTEM_PATH:$PATH"

%post -c /bin/bash
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

    echo "########################################"
    echo "# Installing cisTEM - 1.0.0-beta-intel #"
    echo "########################################"

    echo "Installing dependencies"
    apt install -y libgtk2.0-0 libgtk2.0-dev libcanberra-gtk-module

    cd /opt
    #The website URL is https://cistem.org/system/tdf/upload3/cistem-1.0.0-beta-intel-linux.tar.gz?file=1&type=cistem_details&id=37&force=0&s3fs=1 It redirects to AWS. Using the direct link
    wget https://cistem.s3.amazonaws.com/cistem-1.0.0-beta-intel-linux.tar.gz
   
    tar -zxvf cistem-1.0.0-beta-intel-linux.tar.gz


%runscript
    $*
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

