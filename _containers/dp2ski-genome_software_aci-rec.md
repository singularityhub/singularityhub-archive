---
id: 6435
name: "dp2ski/genome_software_aci"
branch: "master"
tag: "rec"
commit: "a2acb6adaa565d93ba109cb20d1cb8c875e24b4a"
version: "0458787dead64b2a2e1cc36a9aebd0f5"
build_date: "2019-02-05T16:48:48.026Z"
size_mb: 2349
size: 1072955423
sif: "https://datasets.datalad.org/shub/dp2ski/genome_software_aci/rec/2019-02-05-a2acb6ad-0458787d/0458787dead64b2a2e1cc36a9aebd0f5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dp2ski/genome_software_aci/rec/2019-02-05-a2acb6ad-0458787d/
recipe: https://datasets.datalad.org/shub/dp2ski/genome_software_aci/rec/2019-02-05-a2acb6ad-0458787d/Singularity
collection: dp2ski/genome_software_aci
---

# dp2ski/genome_software_aci:rec

```bash
$ singularity pull shub://dp2ski/genome_software_aci:rec
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:centos7

%runscript

%environment
    export PATH=$PATH:/PBSuite_15.8.24/
    export PYTHONPATH=$PYTHONPATH:/PBSuite_15.8.24/

%apprun fastQValidator
exec /fastQValidator/bin/fastQValidator "$@"

%apprun NxTrim
exec /NxTrim/nxtrim "$@"

%apprun RecoverY
exec python /RecoverY/recoverY.py "$@"

%apprun Trimmomatic
exec java -jar /Trimmomatic-0.38/trimmomatic-0.38.jar "$@"

%apprun PBJelly
exec /PBSuite_15.8.24/bin/Jelly.py "$@"

%post
    # commands to be executed inside container during bootstrap
    # add python and install some packages
    # taken from one of will's singularity recipies
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
    yum -y install python-pip
    pip install numpy
    pip install biopython
    pip install matplotlib
    pip install seaborn

    #ACI mappings
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/group
    mkdir -p /gpfs/scratch
    mkdir -p /var/spool/torque

    git clone https://github.com/statgen/libStatGen
    cd libStatGen
    make all
    cd ..

    git clone https://github.com/statgen/fastQValidator
    cd fastQValidator
    make all
    cd ..

    git clone https://github.com/sequencing/NxTrim.git
    cd NxTrim
    make
    cd ..

    #this one is just a bunch of python scripts
    git clone https://github.com/makovalab-psu/RecoverY

    wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.38.zip
    unzip Trimmomatic-0.38.zip
    yum -y install java-1.8.0-openjdk     

    wget https://sourceforge.net/projects/pb-jelly/files/latest/download/PBSuite_15.8.24.tgz
    tar -xzf PBSuite_15.8.24.tgz

    pip install networkx==1.1
    cd /PBSuite_15.8.24
    sed -i 's\/stornext/snfs5/next-gen/scratch/english/Jelly/DevJelly/trunk\/PBSuite_15.8.24\g' setup.sh
    source setup.sh
```

## Collection

 - Name: [dp2ski/genome_software_aci](https://github.com/dp2ski/genome_software_aci)
 - License: None

