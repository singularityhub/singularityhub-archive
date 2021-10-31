---
id: 11407
name: "psumionka-task/Singularity_Debian-9"
branch: "master"
tag: "def"
commit: "9d47d76a0500143a1580db122aca6793faee030a"
version: "36d76e57567b4283b4e7e258765e0fd5130c4c53664597c9e038389d1d9b5e98"
build_date: "2019-10-29T15:51:46.142Z"
size_mb: 388.11328125
size: 406966272
sif: "https://datasets.datalad.org/shub/psumionka-task/Singularity_Debian-9/def/2019-10-29-9d47d76a-36d76e57/36d76e57567b4283b4e7e258765e0fd5130c4c53664597c9e038389d1d9b5e98.sif"
url: https://datasets.datalad.org/shub/psumionka-task/Singularity_Debian-9/def/2019-10-29-9d47d76a-36d76e57/
recipe: https://datasets.datalad.org/shub/psumionka-task/Singularity_Debian-9/def/2019-10-29-9d47d76a-36d76e57/Singularity
collection: psumionka-task/Singularity_Debian-9
---

# psumionka-task/Singularity_Debian-9:def

```bash
$ singularity pull shub://psumionka-task/Singularity_Debian-9:def
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:9

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
    echo "deb http://ftp.us.debian.org/debian jessie main" > /etc/apt/sources.list.d/libxp-source.list
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

 - Name: [psumionka-task/Singularity_Debian-9](https://github.com/psumionka-task/Singularity_Debian-9)
 - License: None

