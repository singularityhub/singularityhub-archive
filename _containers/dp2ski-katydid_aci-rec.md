---
id: 7713
name: "dp2ski/katydid_aci"
branch: "master"
tag: "rec"
commit: "28e8083362166d8de36d20fdf6197d8431da3006"
version: "d13277078c29320e6e38a8dd540e1563"
build_date: "2019-03-13T03:34:54.408Z"
size_mb: 6569
size: 1859559455
sif: "https://datasets.datalad.org/shub/dp2ski/katydid_aci/rec/2019-03-13-28e80833-d1327707/d13277078c29320e6e38a8dd540e1563.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dp2ski/katydid_aci/rec/2019-03-13-28e80833-d1327707/
recipe: https://datasets.datalad.org/shub/dp2ski/katydid_aci/rec/2019-03-13-28e80833-d1327707/Singularity
collection: dp2ski/katydid_aci
---

# dp2ski/katydid_aci:rec

```bash
$ singularity pull shub://dp2ski/katydid_aci:rec
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum
%setup

%files

%environment 


%runscript


%post
    # commands to be executed inside container during bootstrap
    # add python and install some packages
    yum install -y epel-release
    yum install -y terminator
    yum install -y centos-release-scl
    yum install -y vte-devel
    yum install -y vte291-devel
    yum install -y vte-profile
    yum install -y centos-release-scl
    yum -y install devtoolset-7
#    yum install -y devtoolset-7-gcc*
    scl enable devtoolset-7 bash
    yum -y groups install "Development Tools"
#    yum -y groups install "GNOME Desktop"
    yum -y groups install "Base"
#    yum -y groups install "X Window System" "Desktop" "Fonts"
    yum -y install git cmake gcc-c++ gcc binutils \
        libX11-devel libXpm-devel libXft-devel libXext-devel
    yum -y install gcc-gfortran openssl-devel pcre-devel \
        mesa-libGL-devel mesa-libGLU-devel glew-devel ftgl-devel mysql-devel \
        fftw-devel cfitsio-devel graphviz-devel \
        avahi-compat-libdns_sd-devel libldap-dev python-devel \
        libxml2-devel gsl-static
    yum -y install gsl-devel \
        openblas-devel \
        lapack-devel
    yum -y install openmpi-devel
    yum -y install cmake3
    yum -y install hdf5-devel
#    yum -y install boost-devel
    yum -y install patch
    yum -y install redhat-lsb-core
    yum -y update

    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/scratch
    mkdir -p /gpfs/group

#    echo "source /opt/rh/devtoolset-7/enable" >> ~/.bashrc

    mkdir -p /opt/sw/
    cd /opt/sw/
    
    source /opt/rh/devtoolset-7/enable

    # Install Boost
    cd /opt/sw/
    wget https://dl.bintray.com/boostorg/release/1.69.0/source/boost_1_69_0.tar.gz
    tar -xf boost_1_69_0.tar.gz
    cd boost_1_69_0
    ./bootstrap.sh
    ./b2 install
    
    # Install root
    cd /opt/sw/
#    wget https://root.cern.ch/download/root_v6.14.04.Linux-centos7-x86_64-gcc4.8.tar.gz
#    tar -xf root_v6.14.04.Linux-centos7-x86_64-gcc4.8.tar.gz
#    rm root_v6.14.04.Linux-centos7-x86_64-gcc4.8.tar.gz
    wget https://root.cern/download/root_v6.16.00.Linux-centos7-x86_64-gcc4.8.tar.gz
    tar -xf root_v6.16.00.Linux-centos7-x86_64-gcc4.8.tar.gz
    source root/bin/thisroot.sh
#    echo "source /opt/sw/root/bin/thisroot.sh" >> ~/.bashrc

    # Install locust_mc
    cd /opt/sw/
    git clone "https://github.com/project8/locust_mc"
    cd locust_mc
    git submodule update --init --recursive
    git clone https://github.com/project8/Kassiopeia.git
    sed -i -e 's/option( locust_mc_BUILD_WITH_KASSIOPEIA "Option to build with Kassiopeia" FALSE )/option( locust_mc_BUILD_WITH_KASSIOPEIA "Option to build with Kassiopeia" TRUE )/g' CMakeLists.txt
    mkdir build
    cd build
    cmake3 ..
    make install
    source bin/source/kasperenv.sh
#    echo "source /opt/sw/locust_mc/build/bin/kasperenv.sh" >> ~/.bashrc


    # Delete tar files
    cd /opt/sw/
    rm root_v6.16.00.Linux-centos7-x86_64-gcc4.8.tar.gz
    rm boost_1_69_0.tar.gz
    rm -rf boost_1_69_0

    #need matio for katydid
    yum install -y zlib
    #git clone https://github.com/tbeu/matio
    #cd matio/
    #git submodule update --recursive
    #./autogen.sh
    #./configure
    #make
    #make check
    #make install

    #install katydid
    cd /opt/sw/
    git clone https://github.com/project8/Katydid
    cd Katydid
    git submodule update --init --recursive
    sed -i -e 's/option (Katydid_USE_MATLAB "Flag to optionally use MatIO libraries, needed to read MAT files" ON)/option (Katydid_USE_MATLAB "Flag to optionally use MatIO libraries, needed to read MAT files" OFF)/g' CMakeLists.txt
    mkdir build && cd build
    cmake3 .. 
    make
    make install
```

## Collection

 - Name: [dp2ski/katydid_aci](https://github.com/dp2ski/katydid_aci)
 - License: None

