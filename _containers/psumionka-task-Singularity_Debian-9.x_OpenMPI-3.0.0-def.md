---
id: 11437
name: "psumionka-task/Singularity_Debian-9.x_OpenMPI-3.0.0"
branch: "master"
tag: "def"
commit: "2cde261cd2a310006bce0210d1287e3f9b561cce"
version: "c35f9bb1d198159fc6235d3f9f90e58b3a11bf1782e4c1d56253dbfcdb76c8b0"
build_date: "2019-10-30T10:01:06.021Z"
size_mb: 714.54296875
size: 749252608
sif: "https://datasets.datalad.org/shub/psumionka-task/Singularity_Debian-9.x_OpenMPI-3.0.0/def/2019-10-30-2cde261c-c35f9bb1/c35f9bb1d198159fc6235d3f9f90e58b3a11bf1782e4c1d56253dbfcdb76c8b0.sif"
url: https://datasets.datalad.org/shub/psumionka-task/Singularity_Debian-9.x_OpenMPI-3.0.0/def/2019-10-30-2cde261c-c35f9bb1/
recipe: https://datasets.datalad.org/shub/psumionka-task/Singularity_Debian-9.x_OpenMPI-3.0.0/def/2019-10-30-2cde261c-c35f9bb1/Singularity
collection: psumionka-task/Singularity_Debian-9.x_OpenMPI-3.0.0
---

# psumionka-task/Singularity_Debian-9.x_OpenMPI-3.0.0:def

```bash
$ singularity pull shub://psumionka-task/Singularity_Debian-9.x_OpenMPI-3.0.0:def
```

## Singularity Recipe

```singularity
BootStrap: library
From: psumionka-task/default/debian-9.x_core:default

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
    apt-get -y clean all
    #
    apt-get -y update
    apt-get -y install gdm3

    # Install OpenMPI 3.0.0-gcc
    apt-get -y install make automake autoconf python perl gfortran
    cd /tmp
    wget https://www.open-mpi.org/software/ompi/v3.0/downloads/openmpi-3.0.0.tar.gz
    tar xvf openmpi-3.0.0.tar.gz
    cd openmpi-3.0.0
    ./configure --prefix /opt/openmpi3/3.0.0-gcc
    make
    make install
    apt-get -y --force-yes autoremove

%environment
    # openMPI 3.0
    export OMP_NUM_THREADS=1
    export OPENMPI_DIR=/opt/openmpi3/3.0.0-gcc
    export LD_LIBRARY_PATH=$OPENMPI_DIR/lib
    export MANPATH=$OPENMPI_DIR/share/man

    export PATH=$PATH:$OPENMPI_DIR/bin:$LD_LIBRARY_PATH:$MANPATH

%runscript
    echo "Uruchamianie zadania wewnatrz srodowiska..."
```

## Collection

 - Name: [psumionka-task/Singularity_Debian-9.x_OpenMPI-3.0.0](https://github.com/psumionka-task/Singularity_Debian-9.x_OpenMPI-3.0.0)
 - License: None

