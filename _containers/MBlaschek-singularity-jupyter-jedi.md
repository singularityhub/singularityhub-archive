---
id: 11754
name: "MBlaschek/singularity-jupyter"
branch: "master"
tag: "jedi"
commit: "ac28c00030727fcdbc7abe0cbcb64dd19f826fd5"
version: "a3be88fc429f7895b41a86f239602d26c1acc266a29817b53d07ec51caf24d70"
build_date: "2019-12-06T10:37:55.528Z"
size_mb: 962.73046875
size: 1009496064
sif: "https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/jedi/2019-12-06-ac28c000-a3be88fc/a3be88fc429f7895b41a86f239602d26c1acc266a29817b53d07ec51caf24d70.sif"
url: https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/jedi/2019-12-06-ac28c000-a3be88fc/
recipe: https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/jedi/2019-12-06-ac28c000-a3be88fc/Singularity
collection: MBlaschek/singularity-jupyter
---

# MBlaschek/singularity-jupyter:jedi

```bash
$ singularity pull shub://MBlaschek/singularity-jupyter:jedi
```

## Singularity Recipe

```singularity
BootStrap: docker
From: jcsda/docker_base-gnu-openmpi-dev:latest

%labels
MAINTAINER Mark Miesch
SPECIES JEDI

%runscript
    echo "Welcome, this is Singularity container for JEDI with GNU 7"

%environment
    export DISPLAY=:0.0
    export TERM=xterm
    export FC=mpifort
    export CXX=mpicxx
    export CC=mpicc
    export GIT_MERGE_AUTOEDIT=no
    export NETCDF=/usr/local
    export PNETCDF=/usr/local
    export HDF5_ROOT=/usr/local
    export PIO=/usr/local
    export BOOST_ROOT=/usr/local
    export EIGEN3_INCLUDE_DIR=/usr/local
    export LAPACK_PATH=/usr/local
    export LAPACK_DIR=$LAPACK_PATH
    export LAPACK_LIBRARIES="$LAPACK_PATH/lib/liblapack.a;$LAPACK_PATH/lib/libblas.a"
    export SERIAL_CC=gcc
    export SERIAL_CXX=g++
    export SERIAL_FC=gfortran
    export MPI_CC=mpicc
    export MPI_CXX=mpicxx
    export MPI_FC=mpifort
%post
    # build jedi stack
    cd /root \
      && git clone https://github.com/jcsda/jedi-stack.git \
      && cd jedi-stack/buildscripts \
      && git checkout develop
    #
    # Modify config
    #
    cat config/config_container-gnu-openmpi-dev.sh | sed 's/export        STACK_BUILD_JASPER=N/export        STACK_BUILD_JASPER=Y/g' > config/config_container-gnu-openmpi-dev2.sh
    #
    # Build
    #
    ./build_stack.sh "container-gnu-openmpi-dev2" \
        && mv ../jedi-stack-contents.log /etc \
        && chmod a+r /etc/jedi-stack-contents.log \
        && rm -rf /root/jedi-stack \
        && rm -rf /var/lib/apt/lists/* \
        && mkdir /worktmp
    # add user
    useradd -U -k /etc/skel -s /bin/bash -d /home/jedi -m jedi
    echo "[credential]\n    helper = cache --timeout=7200" >> ~jedi/.gitconfig && \
      mkdir ~jedi/.openmpi && \
      echo "rmaps_base_oversubscribe = 1" >> ~jedi/.openmpi/mca-params.conf && \
      chown -R jedi:jedi ~jedi/.gitconfig ~jedi/.openmpi
    # Travis CI
    cd /usr/local/src \
      && curl -L -O http://downloads.sourceforge.net/ltp/lcov-1.14.tar.gz \
      && tar -xvf lcov-1.14.tar.gz \
      && cd lcov-1.14 \
      && make install \
      && rm -rf /usr/local/src/*
```

## Collection

 - Name: [MBlaschek/singularity-jupyter](https://github.com/MBlaschek/singularity-jupyter)
 - License: None

