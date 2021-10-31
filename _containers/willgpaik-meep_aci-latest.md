---
id: 10637
name: "willgpaik/meep_aci"
branch: "master"
tag: "latest"
commit: "34415e9a8214295fdf3a430fc674329fba718ec3"
version: "a4cb70a7e073f96f835dd7df6bb1bc15"
build_date: "2020-07-28T20:52:16.712Z"
size_mb: 3135.0
size: 1028423711
sif: "https://datasets.datalad.org/shub/willgpaik/meep_aci/latest/2020-07-28-34415e9a-a4cb70a7/a4cb70a7e073f96f835dd7df6bb1bc15.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/meep_aci/latest/2020-07-28-34415e9a-a4cb70a7/
recipe: https://datasets.datalad.org/shub/willgpaik/meep_aci/latest/2020-07-28-34415e9a-a4cb70a7/Singularity
collection: willgpaik/meep_aci
---

# willgpaik/meep_aci:latest

```bash
$ singularity pull shub://willgpaik/meep_aci:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: willgpaik/centos7_aci:latest

%setup

%files

%environment
  export PATH=$PATH:/opt/sw/MEEP_build/bin
  export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/sw/MEEP_build/lib:/opt/sw/MEEP_build/lib64
  export CPATH=$CPATH:/opt/sw/MEEP_build/include
  #export PYTHONPATH=$PYTHONPATH:/opt/sw/MEEP_build/lib/python3.6/site-packages
  export PYTHONPATH=/opt/sw/MEEP_build/lib64/python3.6/site-packages/
  
  source /opt/rh/python27/enable
  PATH="$PATH:/usr/lib64/openmpi/bin/"
  LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib64/openmpi/lib/"
  MPI_ROOT=/usr/lib64/openmpi/
  export PATH
  export LD_LIBRARY_PATH
  export MPI_ROOT

%runscript

%post
  yum -y install atlas-devel \
    blas-devel \
    lapack-devel \
    libtool-ltdl-devel \
    guile-devel \
    libunistring-devel
    
  yum -y --enablerepo=extras install epel-release
  yum -y install   \
    bison             \
    byacc             \
    cscope            \
    ctags             \
    cvs               \
    diffstat          \
    oxygen            \
    flex              \
    gcc               \
    gcc-c++           \
    gcc-gfortran      \
    gettext           \
    git               \
    indent            \
    intltool          \
    libtool           \
    patch             \
    patchutils        \
    rcs               \
    redhat-rpm-config \
    rpm-build         \
    subversion        \
    systemtap         \
    wget
  yum -y install    \
    openblas-devel     \
    fftw3-devel        \
    libpng-devel       \
    gsl-devel          \
    gmp-devel          \
    pcre-devel         \
    libtool-ltdl-devel \
    libunistring-devel \
    libffi-devel       \
    gc-devel           \
    zlib-devel         \
    openssl-devel      \
    sqlite-devel       \
    bzip2-devel        \
    ffmpeg
    
  source /opt/rh/python27/enable
  PATH="$PATH:/usr/lib64/openmpi/bin/"
  LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib64/openmpi/lib/"
  MPI_ROOT=/usr/lib64/openmpi/
  export PATH
  export LD_LIBRARY_PATH
  export MPI_ROOT

    
  # Install HDF5
  cd /tmp
  git clone https://bitbucket.hdfgroup.org/scm/hdffv/hdf5.git
  cd hdf5/
  git checkout tags/hdf5-1_10_5
  ./configure --enable-unsupported --enable-cxx --enable-parallel --enable-shared --prefix=/usr/local CC=mpicc CXX=mpic++
  make -j 2
  make install
  cd /tmp
  rm -rf hdf5
  
  # Install FFTW 3.3.8
  cd /tmp
  wget http://www.fftw.org/fftw-3.3.8.tar.gz
  tar -xf fftw-3.3.8.tar.gz
  cd fftw-3.3.8
  ./configure --prefix=/usr/local --enable-shared --enable-mpi --enable-openmp --enable-threads CC=mpicc CXX=mpic++
  make -j 2 && make install
  cd /tmp
  rm -rf fftw-3.3.8*
  
  export PATH=$PATH:/usr/local/bin
  export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
  export CPATH=$CPATH:/usr/local/include
    
  mkdir /opt/sw
  cd /opt/sw
  wget https://raw.githubusercontent.com/willgpaik/meep_aci/master/meep_install.sh
  #wget https://raw.githubusercontent.com/willgpaik/meep_aci/master/meep_update.sh
  
  chmod +x meep_install.sh
  #chmod +x meep_update.sh
  
  ./meep_install.sh
  #./meep_update.sh
  
  #rm meep_install.sh meep_update.sh
  rm meep_install.sh
```

## Collection

 - Name: [willgpaik/meep_aci](https://github.com/willgpaik/meep_aci)
 - License: None

