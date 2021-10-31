---
id: 7871
name: "dp2ski/guppy_aci"
branch: "master"
tag: "rec"
commit: "c724feef8eb21be433ed3cfa609170876275d9b8"
version: "dd898db23888ff2c111158f82c387ac0"
build_date: "2019-03-21T18:05:58.244Z"
size_mb: 1963
size: 751157279
sif: "https://datasets.datalad.org/shub/dp2ski/guppy_aci/rec/2019-03-21-c724feef-dd898db2/dd898db23888ff2c111158f82c387ac0.simg"
url: https://datasets.datalad.org/shub/dp2ski/guppy_aci/rec/2019-03-21-c724feef-dd898db2/
recipe: https://datasets.datalad.org/shub/dp2ski/guppy_aci/rec/2019-03-21-c724feef-dd898db2/Singularity
collection: dp2ski/guppy_aci
---

# dp2ski/guppy_aci:rec

```bash
$ singularity pull shub://dp2ski/guppy_aci:rec
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:centos7

%runscript
    exec /opt/guppy/ont-guppy-cpu/bin/guppy_basecaller "$@"

%environment
    PATH = /opt/guppy/ont-guppy-cpu/bin/:$PATH

%post
    # commands to be executed inside container during bootstrap
    yum update -y
    yum install -y epel-release
    yum install -y terminator
    yum install -y centos-release-scl
    yum install -y vte-devel
    yum install -y vte291-devel
    yum install -y vte-profile
    yum install -y devtoolset-7-gcc*
    scl enable devtoolset-7 bash
    yum -y groups install "Development Tools"
    yum -y groups install "Base"
    yum -y install git cmake gcc-c++ gcc binutils \
    libX11-devel libXpm-devel libXft-devel libXext-devel
    yum -y install gcc-gfortran openssl-devel pcre-devel \
    mesa-libGL-devel mesa-libGLU-devel glew-devel ftgl-devel mysql-devel \
    fftw-devel cfitsio-devel graphviz-devel \
    avahi-compat-libdns_sd-devel libldap-dev python-devel \
    libxml2-devel gsl-devel

    mkdir -p /opt/guppy/
    cd /opt/guppy
    wget https://mirror.oxfordnanoportal.com/software/analysis/ont-guppy-cpu_2.3.5_linux64.tar.gz
    tar -xzvf ont-guppy-cpu_2.3.5_linux64.tar.gz

    #ACI mappings
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/group
    mkdir -p /gpfs/scratch
    mkdir -p /var/spool/torque
```

## Collection

 - Name: [dp2ski/guppy_aci](https://github.com/dp2ski/guppy_aci)
 - License: None

