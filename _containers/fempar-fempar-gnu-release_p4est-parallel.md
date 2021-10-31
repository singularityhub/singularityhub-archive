---
id: 8399
name: "fempar/fempar"
branch: "experimental"
tag: "gnu-release_p4est-parallel"
commit: "01cfd159285417f479def70e94efb646403a00c6"
version: "cef98a04279b9e904dd8304d10a1f8d7"
build_date: "2019-05-24T15:49:13.410Z"
size_mb: 4020
size: 1353936927
sif: "https://datasets.datalad.org/shub/fempar/fempar/gnu-release_p4est-parallel/2019-05-24-01cfd159-cef98a04/cef98a04279b9e904dd8304d10a1f8d7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/fempar/fempar/gnu-release_p4est-parallel/2019-05-24-01cfd159-cef98a04/
recipe: https://datasets.datalad.org/shub/fempar/fempar/gnu-release_p4est-parallel/2019-05-24-01cfd159-cef98a04/Singularity
collection: fempar/fempar
---

# fempar/fempar:gnu-release_p4est-parallel

```bash
$ singularity pull shub://fempar/fempar:gnu-release_p4est-parallel
```

## Singularity Recipe

```singularity
BootStrap: docker
From: fempar/fempar-env:gnu-release_p4est-parallel

%setup


%post

    #------------------
    # REQUERIMENTS
    #------------------

    mkdir -p /mnt /scratch /opt/fempar

    #------------------
    # USER INSTALL
    #------------------

    # ... Install here your software

    #------------------
    # CLEAN APT files
    #------------------
    apt-get clean
    rm -rf /var/lib/apt/lists/*
    rm -rf /var/tmp/*

%runscript

    echo "Arguments received: $*"
    exec "$@"

%test

    cd /opt/fempar
    ctest -j8 -V -E par_test 

%help

    echo "------------------------------------------------"
    echo "| Finite Element Multiphysics PARallel solvers |"
    echo "|             http://fempar.org/               |"
    echo "------------------------------------------------"

%appinstall fempar

    . /opt/intel/mkl/bin/mklvars.sh intel64 
    PACKAGE=fempar 
    VERSION=experimental 
    URL="https://gitlab.com/$PACKAGE/$PACKAGE.git" 
    ROOT_DIR=$(mktemp -p /tmp -d) 
    INSTALL_ROOT=/opt 
    SOURCES_DIR=$ROOT_DIR/$PACKAGE-$VERSION 
    BUILD_DIR=$INSTALL_ROOT/$PACKAGE 
    THIRDPARTY_BUILD_DIR=$INSTALL_ROOT/$PACKAGE-thirdparty 
    FORTRAN_EXTRA_FLAGS="-DFORTRAN_EXTRA_FLAGS=-fimplicit-none" 
    git clone --single-branch --branch $VERSION --recursive $URL $SOURCES_DIR 
    mkdir -p $BUILD_DIR $THIRDPARTY_BUILD_DIR 
    ################################################ 
    # Build fempar thirdparty libraries 
    ################################################ 
    cd $THIRDPARTY_BUILD_DIR 
    cmake -DCMAKE_BUILD_TYPE=RELEASE $FORTRAN_EXTRA_FLAGS $SOURCES_DIR/ThirdParty 
    cmake --build . 
    ################################################ 
    # Build fempar library 
    ################################################ 
    cd $BUILD_DIR 
    cmake -DCMAKE_BUILD_TYPE=RELEASE -DFEMPAR_ENABLE_TESTS=ON -DFEMPAR_THIRDPARTY_DIR=$THIRDPARTY_BUILD_DIR -DMPIEXEC_PREFLAGS="--allow-run-as-root -oversubscribe" $SOURCES_DIR 
    cmake --build . 
    ################################################ 
    # Clean sources 
    ################################################ 
    rm -rf $SOURCES_DIR 

%appenv fempar

    FEMPAR_DIR=/opt/fempar
    export FEMPAR_DIR

%apphelp fempar

    echo "------------------------------------------------"
    echo "| Finite Element Multiphysics PARallel solvers |"
    echo "|             http://fempar.org/               |"
    echo "|          ------------------------            |"
    echo "| FEMPAR_DIR   = /opt/fempar                   |"
    echo "| ENABLED_LIBS = MKL, BLAS, LAPACK, QHULL,     |"
    echo "|                HDF5, P4EST (parallel)        |"
    echo "------------------------------------------------"
```

## Collection

 - Name: [fempar/fempar](https://github.com/fempar/fempar)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

