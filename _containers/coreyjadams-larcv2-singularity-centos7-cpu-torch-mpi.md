---
id: 5975
name: "coreyjadams/larcv2-singularity"
branch: "centos"
tag: "centos7-cpu-torch-mpi"
commit: "d21f6c1206513245c1f2314e27826bb87a94fc0c"
version: "3a0ee68e4d0e20a81aa097abad31e413"
build_date: "2019-01-08T14:49:56.486Z"
size_mb: 3170
size: 1301004319
sif: "https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cpu-torch-mpi/2019-01-08-d21f6c12-3a0ee68e/3a0ee68e4d0e20a81aa097abad31e413.simg"
url: https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cpu-torch-mpi/2019-01-08-d21f6c12-3a0ee68e/
recipe: https://datasets.datalad.org/shub/coreyjadams/larcv2-singularity/centos7-cpu-torch-mpi/2019-01-08-d21f6c12-3a0ee68e/Singularity
collection: coreyjadams/larcv2-singularity
---

# coreyjadams/larcv2-singularity:centos7-cpu-torch-mpi

```bash
$ singularity pull shub://coreyjadams/larcv2-singularity:centos7-cpu-torch-mpi
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: coreyjadams/larcv2-singularity:centos7-cpu-torch

#Bootstrap: localimage
#From: /home/cadams/DeepLearnPhysics/larcv2-singularity/centos7-cpu-torch1.0rc


%help
Centos7 with torch1.0rc, horovod, mpich, SCN
ML/DL packages  : torch sc-learn
Sci.  packages  : numpy pandas sc-image matplotlib opencv-python
Basic python    : ipython jupyter yaml pygments six zmq wheel h5py tqdm mpi4py horovod
Development kit : g++/gcc cython libqt4-dev python-dev
Utility kit     : git wget emacs vim openssh-client mpich

To start your container simply try
singularity exec THIS_CONTAINER.simg bash

%labels
Maintainer coreyjadams
Version centos7-cpu-torch1.0rc-mpich3.2.1

#------------
# Global installation
#------------
%environment
 

    # for MPICH:
    export PATH=/usr/local/mpich/install/bin/:${PATH}
    export LD_LIBRARY_PATH=/usr/local/mpich/install/lib/:${LD_LIBRARY_PATH}

%post


    # install MPICH
    wget -q http://www.mpich.org/static/downloads/3.2.1/mpich-3.2.1.tar.gz
    tar xf mpich-3.2.1.tar.gz
    rm mpich-3.2.1.tar.gz
    cd mpich-3.2.1
    # disable the addition of the RPATH to compiled executables
    # this allows us to override the MPI libraries to use those
    # found via LD_LIBRARY_PATH
    ./configure --prefix=/usr/local/mpich/install --disable-wrapper-rpath
    make -j 4 install
    # add to local environment to build pi.c
    export PATH=$PATH:/usr/local/mpich//install/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/mpich//install/lib
    env | sort
    cd ..
    rm -rf mpich-3.2.1


    # Add mpi4py and horovod:
    pip --no-cache-dir --disable-pip-version-check install mpi4py


    # install Horovod, add other HOROVOD_* environment variables as necessary
    HOROVOD_WITH_PYTORCH=1 pip install --no-cache-dir horovod
```

## Collection

 - Name: [coreyjadams/larcv2-singularity](https://github.com/coreyjadams/larcv2-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

