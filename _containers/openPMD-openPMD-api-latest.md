---
id: 3050
name: "openPMD/openPMD-api"
branch: "dev"
tag: "latest"
commit: "529938265022027c8ea3536692c5414f19582711"
version: "6b8ebd814134aaa19aeae40378ee5c05"
build_date: "2019-10-20T19:32:24.577Z"
size_mb: 706
size: 245514271
sif: "https://datasets.datalad.org/shub/openPMD/openPMD-api/latest/2019-10-20-52993826-6b8ebd81/6b8ebd814134aaa19aeae40378ee5c05.simg"
url: https://datasets.datalad.org/shub/openPMD/openPMD-api/latest/2019-10-20-52993826-6b8ebd81/
recipe: https://datasets.datalad.org/shub/openPMD/openPMD-api/latest/2019-10-20-52993826-6b8ebd81/Singularity
collection: openPMD/openPMD-api
---

# openPMD/openPMD-api:latest

```bash
$ singularity pull shub://openPMD/openPMD-api:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:unstable
#From: debian:testing
#From: ubuntu:cosmic

%help
Welcome to the openPMD-api container.
This container contains a pre-installed openPMD-api library.
This container provides serial I/O.
Supported backends are HDF5 and ADIOS.
Supported frontends are C++11 and Python3.

%setup
    mkdir -p ${SINGULARITY_ROOTFS}/opt/openpmd-api

%files
    ./* /opt/openpmd-api

%post
    apt-get update && \
    apt-get install -y --no-install-recommends \
        cmake \
        make \
        g++ \
        ipython3 \
        python3-dev \
        pybind11-dev \
        libadios-bin libadios-dev \
        libglib2.0-dev libbz2-dev libibverbs-dev libnetcdf-dev \
        libhdf5-dev && \
    rm -rf /var/lib/apt/lists/*

    # python3-numpy

    # missing: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=900804
    # libadios-openmpi-dev
    # libopenmpi-dev libhdf5-openmpi-dev

    cd $(mktemp -d)
    cmake /opt/openpmd-api \
        -DopenPMD_USE_MPI=OFF \
        -DopenPMD_USE_HDF5=ON \
        -DopenPMD_USE_ADIOS1=ON \
        -DopenPMD_USE_ADIOS2=OFF \
        -DopenPMD_USE_PYTHON=ON \
        -DPYTHON_EXECUTABLE=$(which python3) \
        -DBUILD_TESTING=OFF \
        -DCMAKE_INSTALL_PREFIX=/usr/local \
        -DCMAKE_INSTALL_PYTHONDIR=lib/python3.6/dist-packages
    make
    # make test
    make install

#%test
#    make test

%runscript
    ipython3

%labels
    openPMD_HAVE_MPI OFF
    openPMD_HAVE_HDF5 ON
    openPMD_HAVE_ADIOS1 ON
    openPMD_HAVE_ADIOS2 OFF
    openPMD_HAVE_PYTHON ON
```

## Collection

 - Name: [openPMD/openPMD-api](https://github.com/openPMD/openPMD-api)
 - License: [GNU Lesser General Public License v3.0](https://api.github.com/licenses/lgpl-3.0)

