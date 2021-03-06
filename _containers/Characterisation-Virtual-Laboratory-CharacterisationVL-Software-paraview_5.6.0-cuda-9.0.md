---
id: 7822
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "paraview_5.6.0-cuda-9.0"
commit: "1ee407889ebd5150f332e91051f99c6501383589"
version: "a983768a967db9167b95e6b65821b331"
build_date: "2019-03-18T10:36:39.485Z"
size_mb: 8148
size: 3929473055
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/paraview_5.6.0-cuda-9.0/2019-03-18-1ee40788-a983768a/a983768a967db9167b95e6b65821b331.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/paraview_5.6.0-cuda-9.0/2019-03-18-1ee40788-a983768a/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/paraview_5.6.0-cuda-9.0/2019-03-18-1ee40788-a983768a/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:paraview_5.6.0-cuda-9.0

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:paraview_5.6.0-cuda-9.0
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

    LAST_UPDATED 13-MAR-2019

%environment
    PARAVIEWPATH=/opt/ParaView-5.6.0-MPI-Linux-64bit/bin
    export PATH=$PARAVIEWPATH:$PATH

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
    apt install -y locales
    locale-gen en_AU.UTF-8
   
    #Dependencies obtained from apt-get install paraview (5.4) as wget/tar install of 5.6 fails to work without them.
    apt-get install -y python-cbor python-cffi-backend python-click python-colorama python-concurrent.futures python-constantly python-cryptography python-cycler python-dateutil python-dev python-enum34 python-hyperlink python-idna python-incremental python-ipaddress python-lz4 python-matplotlib python-matplotlib-data python-minimal python-mpi4py python-nacl python-numpy python-olefile python-openssl python-pam python-pil python-pkg-resources python-pyasn1 python-pyasn1-modules python-pyparsing python-qrcode python-serial python-service-identity python-six python-snappy python-subprocess32 python-tk python-trie python-trollius python-twisted python-twisted-bin python-twisted-core python-txaio python-tz python-u-msgpack python-ubjson python-vtk6 python-wsaccel python-zope.interface python2.7 python2.7-dev python2.7-minimal qdbus qt-at-spi qt5-gtk-platformtheme qtchooser qtcore4-l10n qttranslations5-l10n tcl8.5 tk8.6-blt2.5 ttf-bitstream-vera

    #xdg-utils - for Paraview to display pdf help files
    apt-get install -y xdg-utils firefox evince libcanberra-gtk-module

    echo "================================="
    echo " Downloading Paraview 5.6.0      "
    echo "================================="
    #cd /tmp
    wget -O paraview.tar.gz "https://www.paraview.org/paraview-downloads/download.php?submit=Download&version=v5.6&type=binary&os=Linux&downloadFile=ParaView-5.6.0-MPI-Linux-64bit.tar.gz"

    echo "================================="
    echo "Extracting  Paraview 5.6.0       "
    echo "================================="    
    tar -C /opt/ -zxvf paraview.tar.gz

%runscript
    $*
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

