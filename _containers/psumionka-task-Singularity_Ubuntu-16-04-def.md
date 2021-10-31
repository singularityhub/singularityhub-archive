---
id: 11405
name: "psumionka-task/Singularity_Ubuntu-16-04"
branch: "master"
tag: "def"
commit: "617da1e39c5df440075d6ff39513395daf7fe12d"
version: "497bb247a433149dc91d6af7ef00220e5ffb02ae6ed20989f1039200c93d6c0b"
build_date: "2019-10-29T15:52:30.591Z"
size_mb: 335.05859375
size: 351334400
sif: "https://datasets.datalad.org/shub/psumionka-task/Singularity_Ubuntu-16-04/def/2019-10-29-617da1e3-497bb247/497bb247a433149dc91d6af7ef00220e5ffb02ae6ed20989f1039200c93d6c0b.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/psumionka-task/Singularity_Ubuntu-16-04/def/2019-10-29-617da1e3-497bb247/
recipe: https://datasets.datalad.org/shub/psumionka-task/Singularity_Ubuntu-16-04/def/2019-10-29-617da1e3-497bb247/Singularity
collection: psumionka-task/Singularity_Ubuntu-16-04
---

# psumionka-task/Singularity_Ubuntu-16-04:def

```bash
$ singularity pull shub://psumionka-task/Singularity_Ubuntu-16-04:def
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels
    
    Author Piotr Sumionka : Politechnika Gdańska, CI TASK - dział KDM [kdm.task.gda.pl]

%help
    
    # Uruchomienie zadania w kontenerze
    singularity exec <nazwa_obrazu> <polecenie>

    W razie problemów, proszę o wiadomość na adres:
    kdm@task.gda.pl

%post
    echo "Witaj wewnątrz kontenera, trwa konfiguracja środowiska..."
    apt-get -y update
    apt-get -y upgrade
    #
    ln -fs /usr/share/zoneinfo/Europe/Warsaw /etc/localtime
    export DEBIAN_FRONTEND=noninteractive
    apt-get install -y tzdata
    dpkg-reconfigure --frontend noninteractive tzdata
    #
    # add-apt-repository : command not found
    apt-get -y install software-properties-common
    #
    #apt-get -y install linux-headers-*
    apt-get -y install build-essential
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
    apt-get -y install apt-transport-https libib*
    #apt-get -y install gdm3
    #Used to install libxp6 for chemkin and ansys to work ==> /etc/apt/sources.list.d/libxp-source.list
    #install full libx* <==> libxm4 libxp6
    echo "deb http://us.archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list.d/libxp-source.list
    apt-get -y update
    apt-get -y install libglu1 libxm4 libxp6 libcanberra-gtk-module packagekit-gtk3-module nano ntp default-jre wget tar gzip curl net-tools numactl libmlx4-1 librdmacm1 dapl2-utils ksh mc xterm perl-tk ssh ssh-askpass-fullscreen ssh-askpass
    rm /etc/apt/sources.list.d/libxp-source.list
    apt-get -y clean all

    # Puste katalogi
    cd /
    mkdir apl
    mkdir users
    mkdir scratch

%environment
    # X11
    TERM=xterm

%runscript
    echo "Uruchamianie zadania wewnatrz srodowiska..."
```

## Collection

 - Name: [psumionka-task/Singularity_Ubuntu-16-04](https://github.com/psumionka-task/Singularity_Ubuntu-16-04)
 - License: None

