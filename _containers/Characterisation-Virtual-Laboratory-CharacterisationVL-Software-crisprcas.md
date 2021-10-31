---
id: 8733
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "crisprcas"
commit: "a4a84554049a0f8f6b26b896c36795895eafa287"
version: "1747ee596ed819d2cc99376911a2c189"
build_date: "2020-09-16T23:54:02.552Z"
size_mb: 4692
size: 1922924575
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/crisprcas/2020-09-16-a4a84554-1747ee59/1747ee596ed819d2cc99376911a2c189.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/crisprcas/2020-09-16-a4a84554-1747ee59/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/crisprcas/2020-09-16-a4a84554-1747ee59/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:crisprcas

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:crisprcas
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

    LAST_UPDATED 26-APR-2019

%environment
    VIEWER_PATH=/opt/CRISPRCasViewer
    FINDER_PATH=/opt/CRISPRCasFinder/bin
    export PATH=$VIEWER_PATH:$FINDER_PATH:$PATH

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
    apt install -y locales apt-utils
    locale-gen en_AU.UTF-8

    echo "================================="
    echo " Installing CRISPRCasFinder      "
    echo "================================="
    cd /opt
    wget -O CRISPRCasFinder.zip  https://crisprcas.i2bc.paris-saclay.fr/Home/DownloadFile?filename=CRISPRCasFinder.zip
    unzip CRISPRCasFinder.zip

    cd CRISPRCasFinder
    ./installer_UBUNTU.sh

    #Note: Following came from install script. Added to resolve issues with Perl script.
    cp /opt/CRISPRCasFinder/src/vmatch-2.3.0-Linux_x86_64-64bit/vmatch /opt/CRISPRCasFinder/bin/vmatch2
    cp /opt/CRISPRCasFinder/src/vmatch-2.3.0-Linux_x86_64-64bit/mkvtree /opt/CRISPRCasFinder/bin/mkvtree2
    cp /opt/CRISPRCasFinder/src/vmatch-2.3.0-Linux_x86_64-64bit/vsubseqselect /opt/CRISPRCasFinder/bin/vsubseqselect2


    echo "================================="
    echo " Installing CRISPRCasViewer      "
    echo "================================="
    cd /opt
    wget -O CRISPRCasViewer.zip  https://crisprcas.i2bc.paris-saclay.fr/Home/DownloadFile?filename=CRISPRCasViewer.zip
    unzip CRISPRCasViewer.zip
    chmod -R g+rx,o+rx CRISPRCasViewer

%runscript
    $*
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

