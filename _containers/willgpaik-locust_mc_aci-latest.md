---
id: 6696
name: "willgpaik/locust_mc_aci"
branch: "master"
tag: "latest"
commit: "b1cfe614d1c481f27480276731881cd2f5e2ff14"
version: "8a52c93607e9823609cd8f3165c1319a"
build_date: "2019-07-19T16:27:28.898Z"
size_mb: 5653.0
size: 1633484831
sif: "https://datasets.datalad.org/shub/willgpaik/locust_mc_aci/latest/2019-07-19-b1cfe614-8a52c936/8a52c93607e9823609cd8f3165c1319a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/locust_mc_aci/latest/2019-07-19-b1cfe614-8a52c936/
recipe: https://datasets.datalad.org/shub/willgpaik/locust_mc_aci/latest/2019-07-19-b1cfe614-8a52c936/Singularity
collection: willgpaik/locust_mc_aci
---

# willgpaik/locust_mc_aci:latest

```bash
$ singularity pull shub://willgpaik/locust_mc_aci:latest
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
    mkdir -p /var/spool/torque

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
```

## Collection

 - Name: [willgpaik/locust_mc_aci](https://github.com/willgpaik/locust_mc_aci)
 - License: None

