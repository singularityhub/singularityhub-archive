---
id: 11435
name: "psumionka-task/Singularity_Ubuntu-16-04_OpenFOAM-7"
branch: "master"
tag: "def"
commit: "a57b4aa88287651e15e9ae100f1bce8de4a5a13e"
version: "60948d9cda324ebf08ee02d1b2ca2fa91865348cac449eb560b301a249f05e44"
build_date: "2019-10-30T07:58:07.147Z"
size_mb: 925.3984375
size: 970350592
sif: "https://datasets.datalad.org/shub/psumionka-task/Singularity_Ubuntu-16-04_OpenFOAM-7/def/2019-10-30-a57b4aa8-60948d9c/60948d9cda324ebf08ee02d1b2ca2fa91865348cac449eb560b301a249f05e44.sif"
url: https://datasets.datalad.org/shub/psumionka-task/Singularity_Ubuntu-16-04_OpenFOAM-7/def/2019-10-30-a57b4aa8-60948d9c/
recipe: https://datasets.datalad.org/shub/psumionka-task/Singularity_Ubuntu-16-04_OpenFOAM-7/def/2019-10-30-a57b4aa8-60948d9c/Singularity
collection: psumionka-task/Singularity_Ubuntu-16-04_OpenFOAM-7
---

# psumionka-task/Singularity_Ubuntu-16-04_OpenFOAM-7:def

```bash
$ singularity pull shub://psumionka-task/Singularity_Ubuntu-16-04_OpenFOAM-7:def
```

## Singularity Recipe

```singularity
BootStrap: library
From: psumionka-task/default/ubuntu-16.04_core:default

%labels
    
    Author Piotr Sumionka : Politechnika Gdańska, CI TASK - dział KDM [kdm.task.gda.pl]

%help
    
    Aby uruchomić oprogramowanie OpenFOAM,
    należy do skryptu dodać:
    ". /opt/openfoam7/etc/bashrc"
    ...przed wykonaniem zadania, np.:

    # Uruchomienie zadania w kontenerze
    . /opt/openfoam7/etc/bashrc
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
    apt-get -y clean all
    #
    apt-get -y update
    apt-get -y install gdm3

    # Instalacja OpenFOAM 7
    apt-get -y update
    apt-get -y install gnome-panel gnome-flashback gnome-session-flashback indicator-applet-appmenu
    #
    sh -c "wget -O - http://dl.openfoam.org/gpg.key | apt-key add -"
    add-apt-repository http://dl.openfoam.org/ubuntu
    apt-get -y clean all
    apt-get -y update
    apt-get -y install openfoam7
    #apt-get -y update && DEBIAN_FRONTEND=noninteractive apt-get -y install openfoam7
    # sed -ie '$ a \. /opt/openfoam7/etc/bashrc' /root/.bashrc

    #echo '. /opt/openfoam7/etc/bashrc' >> $SINGULARITY_ENVIRONMENT

%environment
    # X11
    TERM=xterm

%runscript
    echo "Uruchamianie zadania wewnatrz srodowiska..."
    foamInfo simpleFoam
```

## Collection

 - Name: [psumionka-task/Singularity_Ubuntu-16-04_OpenFOAM-7](https://github.com/psumionka-task/Singularity_Ubuntu-16-04_OpenFOAM-7)
 - License: None

