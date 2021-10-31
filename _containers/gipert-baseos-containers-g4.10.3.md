---
id: 1025
name: "gipert/baseos-containers"
branch: "master"
tag: "g4.10.3"
commit: "987e20f27f9a49e287f9c576356939b3fd54cf5a"
version: "25b810d2f040b340cdd76ab7b39020cc"
build_date: "2020-06-16T18:06:55.563Z"
size_mb: 2273
size: 943075359
sif: "https://datasets.datalad.org/shub/gipert/baseos-containers/g4.10.3/2020-06-16-987e20f2-25b810d2/25b810d2f040b340cdd76ab7b39020cc.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/gipert/baseos-containers/g4.10.3/2020-06-16-987e20f2-25b810d2/
recipe: https://datasets.datalad.org/shub/gipert/baseos-containers/g4.10.3/2020-06-16-987e20f2-25b810d2/Singularity
collection: gipert/baseos-containers
---

# gipert/baseos-containers:g4.10.3

```bash
$ singularity pull shub://gipert/baseos-containers:g4.10.3
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
    yum install -q -y epel-release deltarpm
    yum groupinstall -q -y "Development Tools"
    yum install -q -y htop zsh vim wget cmake3 \
        expat-devel xerces-c-devel fftw-devel \
        libXmu-devel libXi-devel libX11-devel libXext-devel libXft-devel libXpm-devel \
        libzip-devel mesa-libGLU-devel \
        libjpeg-devel libpng-devel \
        motif-devel qt-devel mesa-dri-drivers \
        ImageMagick xorg-x11-fonts-Type1
    yum -q clean all
    ln -s /usr/bin/cmake3 /usr/bin/cmake

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

%appinstall clhep
     mkdir -p /scif/src/clhep-src
     wget -q -O- http://proj-clhep.web.cern.ch/proj-clhep/DISTRIBUTION/tarFiles/clhep-2.3.4.4.tgz | tar --strip-components 2 -xz -C /scif/src/clhep-src
     mkdir -p /scif/src/clhep-build && cd /scif/src/clhep-build
     cmake -DCMAKE_INSTALL_PREFIX="$SINGULARITY_APPROOT" \
         -DCMAKE_CXX_FLAGS=-std=c++11 \
         /scif/src/clhep-src > /dev/null
     cmake --build . -- -j"$(nproc)" && make install > /dev/null
     cd .. && rm -rf /scif/src/clhep-src /scif/src/clhep-build

%applabels clhep
    clhep-version 2.3.4.4

##########
# GEANT4 #
##########

%appenv geant4
    export LD_LIBRARY_PATH="/scif/apps/geant4/lib64:/scif/apps/clhep/lib:$LD_LIBRARY_PATH"
    export G4LEDATA="/scif/apps/geant4/share/Geant4-10.3.3/data/G4EMLOW6.50"
    export G4LEVELGAMMADATA="/scif/apps/geant4/share/Geant4-10.3.3/data/PhotonEvaporation4.3.2"
    export G4NEUTRONHPDATA="/scif/apps/geant4/share/Geant4-10.3.3/data/G4NDL4.5"
    export G4NEUTRONXSDATA="/scif/apps/geant4/share/Geant4-10.3.3/data/G4NEUTRONXS1.4"
    export G4PIIDATA="/scif/apps/geant4/share/Geant4-10.3.3/data/G4PII1.3"
    export G4RADIOACTIVEDATA="/scif/apps/geant4/share/Geant4-10.3.3/data/RadioactiveDecay5.1.1"
    export G4REALSURFACEDATA="/scif/apps/geant4/share/Geant4-10.3.3/data/RealSurface1.0"
    export G4SAIDXSDATA="/scif/apps/geant4/share/Geant4-10.3.3/data/G4SAIDDATA1.1"
    export G4ENSDFSTATEDATA="/scif/apps/geant4/share/Geant4-10.3.3/data/G4ENSDFSTATE2.1"
    export G4ABLADATA="/scif/apps/geant4/share/Geant4-10.3.3/data/G4ABLA3.0"

%appinstall geant4
    mkdir -p /scif/src/geant4-src
    wget -q -O- http://cern.ch/geant4/support/source/geant4.10.03.p03.tar.gz | tar --strip-components 1 -xz -C /scif/src/geant4-src
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
    geant4-version 10.3.p03
```

## Collection

 - Name: [gipert/baseos-containers](https://github.com/gipert/baseos-containers)
 - License: None

