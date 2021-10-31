---
id: 4984
name: "mcw-rcc/geant4"
branch: "master"
tag: "4.10.4"
commit: "45e24494a5465ec6515b92a3116abf8ff0319dc6"
version: "a5e262ef8529f3d59e0870eaf78dfff5"
build_date: "2020-10-02T17:44:12.696Z"
size_mb: 4796
size: 1601499167
sif: "https://datasets.datalad.org/shub/mcw-rcc/geant4/4.10.4/2020-10-02-45e24494-a5e262ef/a5e262ef8529f3d59e0870eaf78dfff5.simg"
url: https://datasets.datalad.org/shub/mcw-rcc/geant4/4.10.4/2020-10-02-45e24494-a5e262ef/
recipe: https://datasets.datalad.org/shub/mcw-rcc/geant4/4.10.4/2020-10-02-45e24494-a5e262ef/Singularity
collection: mcw-rcc/geant4
---

# mcw-rcc/geant4:4.10.4

```bash
$ singularity pull shub://mcw-rcc/geant4:4.10.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer Matthew Flister
Version 4.10.4p02

%help
This container runs Geant4.

%environment
    export LD_LIBRARY_PATH="/opt/geant4/lib:$LD_LIBRARY_PATH"
    export G4LEDATA="/opt/geant4/share/Geant4-10.4.2/data/G4EMLOW7.3"
    export G4LEVELGAMMADATA="/opt/geant4/share/Geant4-10.4.2/data/PhotonEvaporation5.2"
    export G4NEUTRONHPDATA="/opt/geant4/share/Geant4-10.4.2/data/G4NDL4.5"
    export G4NEUTRONXSDATA="/opt/geant4/share/Geant4-10.4.2/data/G4NEUTRONXS1.4"
    export G4PIIDATA="/opt/geant4/share/Geant4-10.4.2/data/G4PII1.3"
    export G4RADIOACTIVEDATA="/opt/geant4/share/Geant4-10.4.2/data/RadioactiveDecay5.2"
    export G4REALSURFACEDATA="/opt/geant4/share/Geant4-10.4.2/data/RealSurface2.1.1"
    export G4SAIDXSDATA="/opt/geant4/share/Geant4-10.4.2/data/G4SAIDDATA1.1"
    export G4ENSDFSTATEDATA="/opt/geant4/share/Geant4-10.4.2/data/G4ENSDFSTATE2.2"
    export G4ABLADATA="/opt/geant4/share/Geant4-10.4.2/data/G4ABLA3.1"

%post
    # default mount points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts
    
    # Install necessary packages
    apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gcc-multilib \
        ca-certificates \
        zlib1g-dev \
        libfreetype6-dev \
        libexpat1-dev \
        cmake \
        wget \
        dcmtk
    apt-get clean

    # install geant4
    wget https://github.com/Geant4/geant4/archive/v10.4.2.tar.gz && tar xvf v10.4.2.tar.gz
    mkdir -p geant4-10.4.2/geant4-build && cd geant4-10.4.2/geant4-build
    cmake .. -DCMAKE_INSTALL_PREFIX=/opt/geant4 -DGEANT4_INSTALL_DATA=ON
    make && make install 
    cd ~/ && rm -rf geant4-10.4.2 v10.4.2.tar.gz
```

## Collection

 - Name: [mcw-rcc/geant4](https://github.com/mcw-rcc/geant4)
 - License: [MIT License](https://api.github.com/licenses/mit)

