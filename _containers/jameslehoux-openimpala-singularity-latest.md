---
id: 12299
name: "jameslehoux/openimpala-singularity"
branch: "master"
tag: "latest"
commit: "4fbd4c5735b5645c5fe54224e5b28fcae1bb0450"
version: "e74f7b939b8aad299f40e9ffbdfd1292"
build_date: "2021-04-19T12:18:23.517Z"
size_mb: 3475.0
size: 849747999
sif: "https://datasets.datalad.org/shub/jameslehoux/openimpala-singularity/latest/2021-04-19-4fbd4c57-e74f7b93/e74f7b939b8aad299f40e9ffbdfd1292.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/jameslehoux/openimpala-singularity/latest/2021-04-19-4fbd4c57-e74f7b93/
recipe: https://datasets.datalad.org/shub/jameslehoux/openimpala-singularity/latest/2021-04-19-4fbd4c57-e74f7b93/Singularity
collection: jameslehoux/openimpala-singularity
---

# jameslehoux/openimpala-singularity:latest

```bash
$ singularity pull shub://jameslehoux/openimpala-singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:7


%help  
    Container that contains all libraries needed to run OpenImpala
      * Singularity integration with and use of MPI
      * the steps necessary to enable MPI messaging over IB
      * Build of AMReX libraries
      * Build of Hypre solver
      * HDF5 1.12.0
      * HDF5 C++ API
      * CMake
      
    Note: the original recipe for enabling MPI messaging over IB is
      * https://community.mellanox.com/docs/DOC-2431
      * This recipe is adapted from M. Dutas hpc-mpi-benchmarks.sif

    Usage: functions are installed as Singularity apps.  A few useful commands
      * singularity apps container.simg
      * singularity help --app diffusion container.simg
      * singularity run --app diffusion container.simg


%labels
    maintainer James Le Houx
    version 1.5



%post
  #
  # --- install compilers
  yum install -y centos-release-scl-rh
  yum install -y devtoolset-9

  source /opt/rh/devtoolset-9/enable

  #
  # --- install verbs
  yum groupinstall -y "Infiniband"
  yum install	   -y libibverbs-devel
  
  yum install -y gcc-gfortran wget git rh-python36 hostname
  yum --enablerepo=extras install -y epel-release
  scl enable rh-python36 bash
  yum install -y libtiff libtiff-devel python-pip boost169-devel.x86_64
  python -m pip --version
  python -m pip install --upgrade pip


    #
    # --- install OpenMPI
    OPENMPI_VERSION=3.1.4
    wget https://download.open-mpi.org/release/open-mpi/v${OPENMPI_VERSION%??}/openmpi-${OPENMPI_VERSION}.tar.gz --no-check-certificate
    tar -xf openmpi-${OPENMPI_VERSION}.tar.gz
    cd openmpi-${OPENMPI_VERSION}/
    ./configure \
       --prefix=/usr/local \
       --enable-orterun-prefix-by-default \
       --enable-mpirun-prefix-by-default \
       --with-verbs

    # Note: "--with-verbs" is not essential, as ibverbs support is picked up automatically

    make
    make install
    cd ../
    rm -fr openmpi-${OPENMPI_VERSION}*

    #
    # --- make OpenMPI libraries /usr/local/lib available
    ldconfig
    ldconfig /usr/local/lib
    
    #
    # --- install cmake
    wget https://cmake.org/files/v3.12/cmake-3.12.3.tar.gz --no-check-certificate
    tar zxvf cmake-3.* && \
    cd cmake-3.* && \
    ./bootstrap --prefix=/usr/local && \
    make -j$(nproc) && \
    make install
    cd ../

    mkdir -p /src

    #
    # --- install HDF5
    cd /src
    HDF5_VERSION=1.12.0
    wget https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.12/hdf5-${HDF5_VERSION}/src/hdf5-${HDF5_VERSION}.tar.gz --no-check-certificate
    tar -xf hdf5-${HDF5_VERSION}.tar.gz && cd hdf5-${HDF5_VERSION}
    CFLAGS="-O3 -mavx2" CXXFLAGS=${CFLAGS} FCFLAGS=${CFLAGS} \
    CC=`type -p mpicc` FC=`type -p mpif90` \
        ./configure \
        --prefix=/opt/hdf5-parallel/${HDF5_VERSION} \
        --enable-fortran \
        --enable-fortran2003 \
        --enable-parallel \
        --disable-tests && \
    make && make install

    rm -fr hdf5-${HDF5_VERSION}/ hdf5-${HDF5_VERSION}.tar.gz

    ROOT_HDF5=/opt/hdf5-parallel/1.12.0

    #
    # --- install HDF5 C++ api
    cd /src
    export CC=/opt/rh/devtoolset-9/root/usr/bin/gcc
    export CPP=/opt/rh/devtoolset-9/root/usr/bin/cpp
    export CXX=/opt/rh/devtoolset-9/root/usr/bin/c++
    python -m pip install conan
    conan remote add ess-dmsc https://api.bintray.com/conan/ess-dmsc/conan
    conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan
    git clone https://github.com/ess-dmsc/h5cpp.git && \
    cd h5cpp && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make
    make install

    #
    # --- install amrex
    cd /src
    git clone -b 21.02 --single-branch https://github.com/AMReX-Codes/amrex.git && \
    cd /src/amrex && \
    ./configure --with-mpi yes --with-omp yes --enable-eb yes && \
    make && \
    make install

    #
    # --- install hypre
    cd /src
    git clone https://github.com/hypre-space/hypre.git && \
    cd hypre/src && \
    ./configure && \
    make && \
    make install

    cd /
    cp -r /src/amrex/tmp_install_dir/include /usr/include/amrex
    cp -r /src/amrex/tmp_install_dir/lib/* /usr/lib/
    cp -r /src/hypre/src/hypre/include /usr/include/hypre
    cp -r /src/hypre/src/hypre/lib/* /usr/lib
    cp -r /src/h5cpp/build/lib/* /usr/lib
    cp -r /src/hdf5-1.12.0/src/ /usr/include/hdf5
    cp -r /src/hdf5-1.12.0/hl/src/* /usr/include/hdf5

    rm -rf /src
    
    #
    # --- install OpenImpala
    cd /
    git clone https://github.com/kramergroup/openImpala.git && \
    cd openImpala && \
    make

#============================================================#
# environment: PATH, LD_LIBRARY_PATH, etc.
#============================================================#

%environment

    export OPENMPI_VERSION=3.1.4
    export OPENIMPALA_VERSION=1.0.0
    export PATH=/opt/openmpi/${OPENMPI_VERSION}/bin:$PATH


  export PATH=/opt/rh/devtoolset-9/root/usr/bin:${PATH}}
  export LD_LIBRARY_PATH=/opt/rh/devtoolset-9/root/usr/lib64:/opt/rh/devtoolset-9/root/usr/lib:${LD_LIBRARY_PATH}
  export LD_LIBRARY_PATH=/opt/rh/devtoolset-9/root/usr/lib64/dyninst:/opt/rh/devtoolset-9/root/usr/lib/dyninst:${LD_LIBRARY_PATH}
  export LD_LIBRARY_PATH=/usr/local/lib64:/usr/lib:${LD_LIBRARY_PATH}
  
  export LC_ALL=C


#============================================================#
# script to run with command "singularity run"
#============================================================#

%runscript


#============================================================#
# script to run with command "singularity test"
#    if tests need a different environment than that
#    during the building phase (e.g. tests need the
#    environment defined in "%environment"), the image
#    can be built by omitting the test
#       sudo singularity build --notest mpirun.simg Singularity
#============================================================#

#%test
#    mpicc --version
```

## Collection

 - Name: [jameslehoux/openimpala-singularity](https://github.com/jameslehoux/openimpala-singularity)
 - License: None

