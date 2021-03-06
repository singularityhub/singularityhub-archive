---
id: 9257
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "libertem-21-may-2019"
commit: "a1ea471b6338fbea4d5627014073e0be50be9619"
version: "c4e10f5f60153456d4a7ee6b4c6110ed"
build_date: "2020-09-16T23:48:54.018Z"
size_mb: 8687
size: 4660187167
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/libertem-21-may-2019/2020-09-16-a1ea471b-c4e10f5f/c4e10f5f60153456d4a7ee6b4c6110ed.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/libertem-21-may-2019/2020-09-16-a1ea471b-c4e10f5f/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/libertem-21-may-2019/2020-09-16-a1ea471b-c4e10f5f/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:libertem-21-may-2019

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:libertem-21-may-2019
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

    LAST_UPDATED 22-MAY-2019

%environment

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
    echo "# Installing liberTEM - 21-May-2019    #"
    echo "########################################"

    #echo "Installing dependencies"
    apt install -y python3-venv python3-pip

    cd /opt
    #git clone -b v0.1.0 https://github.com/LiberTEM/LiberTEM.git

    #Using this version of LiberTEM as it contains a fix to run in a container.
    # A pull request for Issue80 fix as been submitted to LiberTEM.
    git clone -b issue80 https://github.com/ozej8y/LiberTEM.git

    cd LiberTEM
    pip3 install -e .[torch]

%runscript
    $*
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

