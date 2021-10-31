---
id: 9928
name: "rohinijoshi06/container_recipes"
branch: "master"
tag: "latest"
commit: "7179ac26840ca5a9d31ea039b0b70fb3b1fbfcbd"
version: "9be719465752dcca9dbdb07c8eadf925"
build_date: "2019-06-21T06:30:09.391Z"
size_mb: 1922
size: 634163231
sif: "https://datasets.datalad.org/shub/rohinijoshi06/container_recipes/latest/2019-06-21-7179ac26-9be71946/9be719465752dcca9dbdb07c8eadf925.simg"
url: https://datasets.datalad.org/shub/rohinijoshi06/container_recipes/latest/2019-06-21-7179ac26-9be71946/
recipe: https://datasets.datalad.org/shub/rohinijoshi06/container_recipes/latest/2019-06-21-7179ac26-9be71946/Singularity
collection: rohinijoshi06/container_recipes
---

# rohinijoshi06/container_recipes:latest

```bash
$ singularity pull shub://rohinijoshi06/container_recipes:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%post
   # Install common dependencies
   apt-get update \
    && apt-get --yes install --no-install-recommends \
    bison \
    build-essential \
    cmake \
    flex \
    g++ \
    gcc \
    gettext-base \
    gfortran \
    git \
    libarmadillo-dev \
    libblas-dev \
    libboost-date-time-dev \
    libboost-dev \
    libboost-filesystem-dev \
    libboost-numpy-dev \
    libboost-program-options-dev \
    libboost-python-dev \
    libboost-regex-dev \
    libboost-signals-dev \
    libboost-system-dev \
    libboost-test-dev \
    libboost-thread-dev \
    libcfitsio-dev \
    libfftw3-dev \
    libgsl-dev \
    libgtkmm-3.0-dev \
    libhdf5-serial-dev \
    liblapacke-dev \
    liblog4cplus-1.1-9 \
    liblog4cplus-dev \
    libncurses5-dev \
    libpng-dev \
    libpython2.7-dev \
    libreadline-dev \
    libxml2-dev \
    openssh-server \
    python \
    python-numpy \
    python-pip \
    python-setuptools \
    python-tk \
    subversion \
    vim \
    wcslib-dev \
    wget \
    && rm -rf /var/lib/apt/lists/* \
    && pip install \
    scipy \
    aplpy \
    astropy==2.0.4 \
    matplotlib==2.2.3 \
    pyvo \
    PySocks \
    python-monetdb \
    wcsaxes \
    xmlrunner

   pip install --upgrade numpy 
   
   # Install HDF5
   #RUN wget https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.10/hdf5-1.10.5/src/hdf5-1.10.5.tar.gz \
   # && tar xvf hdf5-1.10.5.tar.gz && cd hdf5-1.10.5 \
   # && ./configure --prefix=/opt/lofarsoft/ --enable-fortran --enable-cxx --enable-threadsafe --enable-unsupported \
   # && make -j4 && make install && cd ../ && rm -rf hdf5-1.10.5 hdf5-1.10.5.tar.gz
   
   # Install casacore data
   mkdir -p /opt/lofarsoft/data \
    && cd /opt/lofarsoft/data \
    && wget ftp://anonymous@ftp.astron.nl/outgoing/Measures/WSRT_Measures.ztar \
    && tar xvf WSRT_Measures.ztar \
    && rm WSRT_Measures.ztar 
   
   # Install casacore
   wget https://github.com/casacore/casacore/archive/v2.4.1.tar.gz \
    && tar xvf v2.4.1.tar.gz && cd casacore-2.4.1 && mkdir build \
    && cd build \
    && cmake -DBUILD_PYTHON=True \
         -DDATA_DIR=/opt/lofarsoft/data \
         -DUSE_OPENMP=ON -DUSE_THREADS=OFF -DUSE_FFTW3=TRUE \
         -DUSE_HDF5=ON -DCXX11=ON -DCMAKE_BUILD_TYPE=Release \
         -DCMAKE_INSTALL_PREFIX=/opt/lofarsoft/ \
         -DCMAKE_CXX_FLAGS="-fsigned-char -O2 -DNDEBUG -march=native" ../ \
    && make -j4 && make install \
    && cd ../../ && rm -rf casacore-2.4.1 v2.4.1.tar.gz
    
    # Install casarest
   git clone https://github.com/casacore/casarest.git \
    && cd casarest \
    && git checkout 2350d906194979d70448bf869bf628c24a0e4c19 \
    && mkdir build \
    && cd build \
    && cmake -DCMAKE_INSTALL_PREFIX=/opt/lofarsoft/ \
             -DCMAKE_PREFIX_PATH=/opt/lofarsoft ../ \
    && make -j4 && make install \
    && cd ../../ && rm -rf casarest
   
   # Install python casacore
   wget https://github.com/casacore/python-casacore/archive/v3.0.0.tar.gz \
    && tar xvf v3.0.0.tar.gz && cd python-casacore-3.0.0 \
    && python setup.py build_ext -I/opt/lofarsoft/include -L/opt/lofarsoft/lib/ \
    && mkdir -p /opt/lofarsoft/lib/python2.7/site-packages/ \
    && export PYTHONPATH=/opt/lofarsoft/lib/python2.7/site-packages/ \
    && python setup.py install --prefix=/opt/lofarsoft
   
   # Install AOFlagger
   wget https://sourceforge.net/projects/aoflagger/files/latest/download \
    && mv download download.tar && tar xvf download.tar \
    && cd aoflagger-2.14.0 && mkdir build && cd build \
    && cmake ../ -DCMAKE_INSTALL_PREFIX=/opt/lofarsoft/ \
                 -DCMAKE_PREFIX_PATH=/opt/lofarsoft \
    && make -j4 && make install && cd ../../ \
    && rm -rf download.tar aoflagger-2.14.0
   
   # Install pyBDSF
   git clone https://github.com/lofar-astron/PyBDSF.git \
    && export PYTHONPATH=/opt/lofarsoft/lib/python2.7/site-packages/ \
    && cd PyBDSF && python setup.py install --prefix=/opt/lofarsoft \
    && cd ../ && rm -rf PyBDSF
    
   # Install the LOFAR beam library
   git clone https://github.com/lofar-astron/LOFARBeam.git \
    && cd LOFARBeam && mkdir build && cd build \
    && cmake -DCMAKE_INSTALL_PREFIX=/opt/lofarsoft/ \
             -DCMAKE_PREFIX_PATH=/opt/lofarsoft ../ \
    && make && make install \
    && cd ../../ && rm -rf LOFARBeam 
   
   # Install DP3
   git clone https://github.com/lofar-astron/DP3.git \
    && cd DP3 && mkdir build && cd build \
    && cmake -DCMAKE_INSTALL_PREFIX=/opt/lofarsoft/ \
             -DCMAKE_PREFIX_PATH=/opt/lofarsoft ../ \
    && make && make install \
    && ln -s /opt/lofarsoft/bin/DPPP /opt/lofarsoft/bin/NDPPP \
    && cd ../../ && rm -rf DP3
   
   # Install LOFAR 3.2.10
   svn --non-interactive -q co \
      https://svn.astron.nl/LOFAR/tags/LOFAR-Release-3_2_10/ source \
    && cd source && mkdir -p build/gnucxx11_optarch \
    && cd build/gnucxx11_optarch \
    && export PYTHONPATH=/opt/lofarsoft/lib/python2.7/site-packages/ \
    && cmake -DBUILD_PACKAGES="MS ParmDB pyparmdb Pipeline" -DBUILD_TESTING=OFF \
          -DCMAKE_INSTALL_PREFIX=/opt/lofarsoft/ \
          -DCMAKE_PREFIX_PATH=/opt/lofarsoft/ \
          -DUSE_OPENMP=True ../../ \
    && make -j4 && make install && cd ../../../ && rm -rf source
    
    # Install dysco
    wget https://github.com/aroffringa/dysco/archive/v1.2.tar.gz \
     && tar xvf v1.2.tar.gz && cd dysco-1.2 && mkdir build && cd build \
     && cmake ../ -DCMAKE_INSTALL_PREFIX=/opt/lofarsoft/ \
              -DCMAKE_PREFIX_PATH=/opt/lofarsoft/ \
     && make -j4 && make install && cd ../../ \
     && rm -rf dysco-1.2 v1.2.tar.gz
     
   # Install LSMTool
   git clone https://github.com/darafferty/LSMTool.git \
     && cd LSMTool \
     && export PYTHONPATH=/opt/lofarsoft/lib/python2.7/site-packages/ \
     && python setup.py install --prefix=/opt/lofarsoft/ \
     && cd ../ && rm -rf LSMTool 
   
   # Install RMextract
   git clone https://github.com/lofar-astron/RMextract.git \
     && cd RMextract \
     && export PYTHONPATH=/opt/lofarsoft/lib/python2.7/site-packages/ \
     && python setup.py install --prefix=/opt/lofarsoft/ --add-lofar-utils \
     && cd ../ && rm -rf RMextract
    
   # Install wsclean
   wget https://sourceforge.net/projects/wsclean/files/wsclean-2.7/wsclean-2.7.tar.bz2/download \
     && mv download download.tar && tar xvf download.tar \
     && cd wsclean-2.7 && mkdir build && cd build \
     && cmake ../ -DCMAKE_INSTALL_PREFIX=/opt/lofarsoft/ \
              -DCMAKE_PREFIX_PATH=/opt/lofarsoft/ \
     && make -j4 && make install && cd ../../ && rm -rf wsclean-2.7 download.tar

   # Install losoto
   git clone https://github.com/revoltek/losoto.git \
     && cd losoto \
     && export PYTHONPATH=/opt/lofarsoft/lib/python2.7/site-packages/ \
     && python setup.py install --prefix=/opt/lofarsoft/ \
     && cd ../ && rm -rf losoto 

%environment
   . /opt/lofarsoft/lofarinit.sh
   export HDF5_USE_FILE_LOCKING=FALSE

%help
   Singularity image containing all required software to run prefactor 3.0. This image is built on Ubuntu 18.04.
```

## Collection

 - Name: [rohinijoshi06/container_recipes](https://github.com/rohinijoshi06/container_recipes)
 - License: None

