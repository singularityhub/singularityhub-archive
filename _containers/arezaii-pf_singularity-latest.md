---
id: 10788
name: "arezaii/pf_singularity"
branch: "master"
tag: "latest"
commit: "e81200ffad3c87d20ef39815b829165e996e9ced"
version: "5009c95774f45f48018d389247f5857a"
build_date: "2020-01-23T05:07:43.288Z"
size_mb: 957.0
size: 230445087
sif: "https://datasets.datalad.org/shub/arezaii/pf_singularity/latest/2020-01-23-e81200ff-5009c957/5009c95774f45f48018d389247f5857a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/arezaii/pf_singularity/latest/2020-01-23-e81200ff-5009c957/
recipe: https://datasets.datalad.org/shub/arezaii/pf_singularity/latest/2020-01-23-e81200ff-5009c957/Singularity
collection: arezaii/pf_singularity
---

# arezaii/pf_singularity:latest

```bash
$ singularity pull shub://arezaii/pf_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7.4.1708
%labels
    # Modified from Dockerfile written and maintained by Steven Smith <smith84@llnl.gov>
%post    

    #-----------------------------------------------------------------------------
    #  Package dependencies
    #-----------------------------------------------------------------------------
    yum -y  install  epel-release
    yum  install -y  \
    autoconf \
    automake \
    binutils \
    cmake3 \
    file \
    gcc  \
    gcc-c++  \
    gcc-gfortran \
    git \
    libtool \
    lsof \
    make \
    tcl-devel \
    tcsh \
    time \
    tk-devel \
    wget \
    which \
    zlib \
    zlib-devel && mkdir -p /home/parflow
    
    #-----------------------------------------------------------------------------
    # Set environment vars
    #-----------------------------------------------------------------------------
    export PARFLOW_DIR=/usr/local
    PATH=$PATH:/usr/lib64/openmpi/bin:$PARFLOW_DIR/bin
    LD_LIBRARY_PATH=/usr/lib64/openmpi/lib:$LD_LIBRARY_PATH
    OMPI_DIR=/opt/ompi
    #SINGULARITY_OMPI_DIR=$OMPI_DIR
    #SINGULARITYENV_APPEND_PATH=$OMPI_DIR/bin
    #SINGULAIRTYENV_APPEND_LD_LIBRARY_PATH=$OMPI_DIR/lib



    #-----------------------------------------------------------------------------
    # Build libraries
    #-----------------------------------------------------------------------------
    
    #
    # OMPI
    # 
    echo "Installing Open MPI"
    export OMPI_DIR=/opt/ompi
    export OMPI_VERSION=4.0.1
    export OMPI_URL="https://download.open-mpi.org/release/open-mpi/v4.0/openmpi-$OMPI_VERSION.tar.gz"
    mkdir -p /tmp/ompi
    mkdir -p /opt
    # Download
    cd /tmp/ompi && wget -O openmpi-$OMPI_VERSION.tar.gz $OMPI_URL && tar -xf openmpi-$OMPI_VERSION.tar.gz
    # Compile and install
    cd /tmp/ompi/openmpi-$OMPI_VERSION && ./configure --prefix=$OMPI_DIR && make install -j2
    # Set env variables so we can
    # compile our application
    export PATH=$OMPI_DIR/bin:$PATH
    export LD_LIBRARY_PATH=$OMPI_DIR/lib:$LD_LIBRARY_PATH
    export MANPATH=$OMPI_DIR/share/man:$MANPATH

    #
    # HDF5
    #
    echo "Installing HDF5"
    mkdir -p /tmp/hdf5
    cd /tmp/hdf5

    wget -q https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.10/hdf5-1.10.5/src/hdf5-1.10.5.tar.gz && \
    tar -xf hdf5-1.10.5.tar.gz && \
    cd hdf5-1.10.5 && \
    CC=mpicc ./configure \
      --prefix=$PARFLOW_DIR \
      --enable-parallel && \
    make && make install && \
    cd .. && \
    rm -fr hdf5-1.10.5 hdf5-1.10.5.tar.gz


    #
    # NetCDF
    #
    echo "Installing NetCDF"
    mkdir -p /tmp/netcdf
    cd /tmp/netcdf

    wget -q https://github.com/Unidata/netcdf-c/archive/v4.7.3.tar.gz && \
    tar -xf v4.7.3.tar.gz && \
    cd netcdf-c-4.7.3 && \
    CC=mpicc CPPFLAGS=-I${PARFLOW_DIR}/include LDFLAGS=-L${PARFLOW_DIR}/lib \
    ./configure --disable-shared --disable-dap --prefix=${PARFLOW_DIR} && \
    make && \
    make install && \
    cd .. && \
    rm -fr netcdf-c-4.7.3 v4.7.3.tar.gz


    #
    # SILO 
    #
    curl "https://wci.llnl.gov/content/assets/docs/simulation/computer-codes/silo/silo-4.10.2/silo-4.10.2.tar.gz" -o "silo-4.10.2.tar.gz" && \
    tar -xf silo-4.10.2.tar.gz && \
    cd silo-4.10.2 && \
    ./configure  --prefix=$PARFLOW_DIR --disable-silex --disable-hzip --disable-fpzip FC=/usr/bin/gfortran F77=/usr/bin/gfortran && \
    make install -j2 && \
    cd .. && \
    rm -fr silo-4.10.2 silo-4.10.2.tar.gz
    
    #
    # Hypre
    #
    cd /home/parflow
    git clone -b master --single-branch https://github.com/LLNL/hypre.git hypre && \
    cd hypre/src && \
    ./configure --prefix=$PARFLOW_DIR && \
    make install -j2 && \
    cd ../.. && \
    rm -fr hypre
    
    #-----------------------------------------------------------------------------
    # Parflow configure and build
    #-----------------------------------------------------------------------------
    
    PARFLOW_MPIEXEC_EXTRA_FLAGS="--mca mpi_yield_when_idle 1 --oversubscribe --allow-run-as-root"
    
    cd /home/parflow
    
    git clone -b pf_omp --single-branch https://github.com/hydroframe/Parflow_perfteam.git parflow && \
    mkdir -p build && \
    cd build && \
    cmake3 ../parflow \
    -DPARFLOW_AMPS_LAYER=mpi1 \
    -DPARFLOW_AMPS_SEQUENTIAL_IO=FALSE \
    -DHYPRE_ROOT=$PARFLOW_DIR \
    -DSILO_ROOT=$PARFLOW_DIR \
    -DPARFLOW_ENABLE_HDF5=TRUE \
    -DPARFLOW_ENABLE_TIMING=TRUE \
    -DPARFLOW_HAVE_CLM=ON \
    -DPARFLOW_ENABLE_NETCDF=TRUE \
    -DNETCDF_INCLUDE_DIR=${PARFLOW_DIR}/include \
    -DNETCDF_LIBRARY=${PARFLOW_DIR}/lib/libnetcdf.a \
    -DPARFLOW_ENABLE_OMP=true \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=$PARFLOW_DIR && \
    make install -j2 && \
    cd .. && \
    rm -fr parflow build

%environment
    export PARFLOW_DIR=/usr/local
    export PATH=$PATH:/usr/lib64/openmpi/bin:$PARFLOW_DIR/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib64/openmpi/lib
    export PARFLOW_MPIEXEC_EXTRA_FLAGS="--mca mpi_yield_when_idle 1 --oversubscribe --allow-run-as-root"
    export OMPI_DIR=/opt/ompi
    export SINGULARITY_OMPI_DIR=$OMPI_DIR
    export SINGULARITYENV_APPEND_PATH=$OMPI_DIR/bin
    export SINGULAIRTYENV_APPEND_LD_LIBRARY_PATH=$OMPI_DIR/lib

%runscript
    exec tclsh "$@"

%startscript
    exec tclsh "$@"
```

## Collection

 - Name: [arezaii/pf_singularity](https://github.com/arezaii/pf_singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

