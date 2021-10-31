---
id: 10263
name: "willgpaik/dssp_aci"
branch: "master"
tag: "latest"
commit: "aa834e67097ec97f0504cc5d4c6b4413a2254983"
version: "6ad3f315f43c4209265206aef284147c"
build_date: "2020-05-19T15:39:54.731Z"
size_mb: 2463.0
size: 847425567
sif: "https://datasets.datalad.org/shub/willgpaik/dssp_aci/latest/2020-05-19-aa834e67-6ad3f315/6ad3f315f43c4209265206aef284147c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/dssp_aci/latest/2020-05-19-aa834e67-6ad3f315/
recipe: https://datasets.datalad.org/shub/willgpaik/dssp_aci/latest/2020-05-19-aa834e67-6ad3f315/Singularity
collection: willgpaik/dssp_aci
---

# willgpaik/dssp_aci:latest

```bash
$ singularity pull shub://willgpaik/dssp_aci:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: willgpaik/centos7_aci

%setup

%files

%environment 
    export PATH=$PATH:/opt/sw/dssp/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
    export DSSP=/opt/sw/dssp/bin
    source /usr/local/gromacs/bin/GMXRC

%runscript

%post
    yum -y update
    
    source /opt/rh/devtoolset-8/enable
    
    export BOOST_ROOT=/usr/local
    
    mkdir -p /opt/sw/dssp
    cd /opt/sw
    git clone https://github.com/mhekkel/libzeep.git
    cd libzeep
    
    sed -i -e '23s/-g/-g $(BOOST_LIB_DIR:%=-L%)/g' makefile
    sed -i -e 's|# BUILD_SHARED_LIB = $(BUILD_SHARED_LIB)|BUILD_SHARED_LIB = 1|g' makefile
    sed -i -e 's|# BOOST = $(HOME)/my-boost|BOOST = $(BOOST_ROOT)|g' makefile
    sed -i -e 's|BOOST_LIB_DIR       = $(BOOST:%=%/lib)|BOOST_LIB_DIR       = $(BOOST_ROOT)/lib|g' makefile
    sed -i -e 's|BOOST_INC_DIR       = $(BOOST:%=%/include)|BOOST_INC_DIR       = $(BOOST_ROOT)/include|g' makefile
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$BOOST_ROOT/lib:/opt/sw/libzeep/lib:/lib:/lib64
    export CPATH=$CPATH:$BOOST_ROOT/include:/opt/sw/libzeep/include/zeep
    
    make lib -j 2
    
    cd /opt/sw
    
    # Install dssp
    git clone https://github.com/cmbi/xssp.git
    cd xssp
    ./autogen.sh
    ./configure --prefix=/opt/sw/dssp/ --with-boost=$BOOST_ROOT/ --with-boost-libdir=$BOOST_ROOT/lib \
        CPPFLAGS="-I${BOOST_ROOT}/include -I${BUILD_DIR}/include -I/opt/sw/libzeep/include/zeep" \
        LDFLAGS="-L${BOOST_ROOT}/lib -L${BUILD_DIR}/lib -L/opt/sw/libzeep/lib" \
        CFLAGS=-lrt CXXFLAGS=-lrt
    make -j $NP && make install
    
    # Install GROMACS
    cd /opt/sw
    wget http://ftp.gromacs.org/pub/gromacs/gromacs-2019.3.tar.gz
    tar xfz gromacs-2019.3.tar.gz
    cd gromacs-2019.3
    mkdir build
    cd build
    cmake3 .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON
    make
    make check
    make install
    source /usr/local/gromacs/bin/GMXRC
    
    cd /opt/sw
    rm -rf xssp
    rm -rf gromacs-2019.3*
```

## Collection

 - Name: [willgpaik/dssp_aci](https://github.com/willgpaik/dssp_aci)
 - License: None

