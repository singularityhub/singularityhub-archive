---
id: 1026
name: "gipert/baseos-containers"
branch: "master"
tag: "g4.9.6"
commit: "987e20f27f9a49e287f9c576356939b3fd54cf5a"
version: "5ab906e68a4d11977ae58e39a0ab9e15"
build_date: "2017-12-04T14:10:46.878Z"
size_mb: 2777
size: 775348255
sif: "https://datasets.datalad.org/shub/gipert/baseos-containers/g4.9.6/2017-12-04-987e20f2-5ab906e6/5ab906e68a4d11977ae58e39a0ab9e15.simg"
url: https://datasets.datalad.org/shub/gipert/baseos-containers/g4.9.6/2017-12-04-987e20f2-5ab906e6/
recipe: https://datasets.datalad.org/shub/gipert/baseos-containers/g4.9.6/2017-12-04-987e20f2-5ab906e6/Singularity
collection: gipert/baseos-containers
---

# gipert/baseos-containers:g4.9.6

```bash
$ singularity pull shub://gipert/baseos-containers:g4.9.6
```

## Singularity Recipe

```singularity
# Singularityfile for containers with the gerda software
#
# Author: luigi.pertoldi@pd.infn.it
# Created: 4 Nov 2017
#
# NOTES: Please build the container from within the folder of this file

BootStrap: docker
From: centos:7

# ==> Global

%labels
    MANTAINER luigi.pertoldi@pd.infn.it
    SOURCE_REPO https://github.com/gipert/baseos-containers

%post
    yum update -q -y
    yum groupinstall -q -y "Development Tools"
    yum install -q -y htop zsh vim wget cmake \
        expat-devel xerces-c-devel fftw-devel \
        libXmu-devel libXi-devel libX11-devel libXext-devel libXft-devel libXpm-devel \
        libzip-devel mesa-libGLU-devel \
        libjpeg-devel libpng-devel \
        motif-devel qt-devel mesa-dri-drivers \
        ImageMagick xorg-x11-fonts-Type1
    yum -q clean all

%runscript
    if [ $# -eq 0 ]; then
        echo -e "\nThe following software is installed in this image:\n"
        ls /scif/apps | sort -u --ignore-case
        echo -e "\nExample usage:\n\n    $ singularity run --app <app-name> <image>\n"
        echo -e "Run 'singularity help' for other singularity commands.\n"
    else
        exec "$@"
    fi

%help
>
> This container includes a basic installation of the GERDA software, run
>
>     $ singularity apps <container>
>
> to see what's included! For specific help use the --app flag.
>

#############
# ROOT CERN #
#############

%apphelp root
    >
    > ROOT - Data Analysis Framework (https://root.cern.ch)
    >
    > Precompiled version for CentOS Cern 7 gcc4.8
    > release web page: https://root.cern.ch/content/release-60608
    >
    > To launch a ROOT session:
    > $ singularity --app root <image>
    >

%appenv root
    export ROOTSYS="/scif/apps/root"
    export MANPATH="$ROOTSYS/man:$MANPATH"
    export PYTHONPATH="$ROOTSYS/lib:$PYTHONPATH"

%apprun root
    root -l $@

%appinstall root
    wget -q -O- https://root.cern.ch/download/root_v6.06.08.Linux-centos7-x86_64-gcc4.8.tar.gz | tar --strip-components 1 -xz -C $SINGULARITY_APPROOT

%applabels root
    root-version 6.06.08

#########
# CLHEP #
#########

%appenv clhep
    export CLHEP_BASE_DIR="/scif/apps/clhep"
    export CLHEP_INCLUDE_DIR="/scif/apps/clhep/include"
    export CLHEP_LIB_DIR="/scif/apps/clhep/lib"

%appinstall clhep
     mkdir -p /scif/src/clhep-src
     wget -q -O- http://proj-clhep.web.cern.ch/proj-clhep/DISTRIBUTION/tarFiles/clhep-2.1.3.1.tgz | tar --strip-components 2 -xz -C /scif/src/clhep-src
     mkdir -p /scif/src/clhep-build && cd /scif/src/clhep-build
     cmake -DCMAKE_INSTALL_PREFIX="$SINGULARITY_APPROOT" \
         -DCMAKE_CXX_FLAGS=-std=c++11 \
         /scif/src/clhep-src > /dev/null
     cmake --build . -- -j"$(nproc)" && make install > /dev/null
     cd .. && rm -rf /scif/src/clhep-src /scif/src/clhep-build

%applabels clhep
    clhep-version 2.1.3.1

##########
# GEANT4 #
##########

%appenv geant4
    export LD_LIBRARY_PATH="/scif/apps/geant4/lib64:/scif/apps/clhep/lib:$LD_LIBRARY_PATH"
    export G4LEDATA="/scif/apps/geant4/share/Geant4-9.6.4/data/G4EMLOW6.32"
    export G4LEVELGAMMADATA="/scif/apps/geant4/share/Geant4-9.6.4/data/PhotonEvaporation2.3"
    export G4NEUTRONHPDATA="/scif/apps/geant4/share/Geant4-9.6.4/data/G4NDL4.2"
    export G4NEUTRONXSDATA="/scif/apps/geant4/share/Geant4-9.6.4/data/G4NEUTRONXS1.2"
    export G4PIIDATA="/scif/apps/geant4/share/Geant4-9.6.4/data/G4PII1.3"
    export G4RADIOACTIVEDATA="/scif/apps/geant4/share/Geant4-9.6.4/data/RadioactiveDecay3.6"
    export G4REALSURFACEDATA="/scif/apps/geant4/share/Geant4-9.6.4/data/RealSurface1.0"
    export G4SAIDXSDATA="/scif/apps/geant4/share/Geant4-9.6.4/data/G4SAIDDATA1.1"

%appinstall geant4
    mkdir -p /scif/src/geant4-src
    wget -q -O- https://geant4.web.cern.ch/geant4/support/source/geant4.9.6.p04.tar.gz | tar --strip-components 1 -xz -C /scif/src/geant4-src
    mkdir -p /scif/src/geant4-build && cd /scif/src/geant4-build
    cmake -DCMAKE_INSTALL_PREFIX="$SINGULARITY_APPROOT" \
        -DGEANT4_BUILD_CXXSTD=c++11 \
        -DGEANT4_USE_SYSTEM_CLHEP=ON \
        -DCLHEP_ROOT_DIR="/scif/apps/clhep" \
        -DGEANT4_USE_GDML=ON \
        -DGEANT4_USE_OPENGL_X11=ON \
        -DGEANT4_USE_RAYTRACER_X11=ON \
        -DGEANT4_INSTALL_DATA=ON \
        -DGEANT4_USE_XM=ON \
        -DGEANT4_USE_QT=ON \
        --fail-on-missing \
        /scif/src/geant4-src > /dev/null
    cmake --build . -- -j"$(nproc)" && make install > /dev/null
    cd .. && rm -rf /scif/src/geant4-src /scif/src/geant4-build

%applabels geant4
    geant4-version 9.6.p04
```

## Collection

 - Name: [gipert/baseos-containers](https://github.com/gipert/baseos-containers)
 - License: None

