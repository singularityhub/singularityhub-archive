---
id: 6865
name: "arcsUVA/hydrator"
branch: "master"
tag: "0.0.2"
commit: "bc592a0a31e44606c1865b2fcf0e36d33af05a48"
version: "d6ce68f448b296aa010cf9aaa0877d97"
build_date: "2019-02-04T16:33:11.332Z"
size_mb: 1116
size: 415539231
sif: "https://datasets.datalad.org/shub/arcsUVA/hydrator/0.0.2/2019-02-04-bc592a0a-d6ce68f4/d6ce68f448b296aa010cf9aaa0877d97.simg"
url: https://datasets.datalad.org/shub/arcsUVA/hydrator/0.0.2/2019-02-04-bc592a0a-d6ce68f4/
recipe: https://datasets.datalad.org/shub/arcsUVA/hydrator/0.0.2/2019-02-04-bc592a0a-d6ce68f4/Singularity
collection: arcsUVA/hydrator
---

# arcsUVA/hydrator:0.0.2

```bash
$ singularity pull shub://arcsUVA/hydrator:0.0.2
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL:  http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum


%post
    yum -y install vim-minimal 
    yum -y install curl 
    yum -y install wget 
    yum -y install git 
    yum -y install gtk2
    yum -y install gtk2-devel
    yum -y install libXtst
    yum -y install libXtst-devel
    yum -y install libXScrnSaver
    yum -y install libXScrnSaver-devel
    yum -y install GConf2
    yum -y install GConf2-devel
    yum -y install alsa-lib
    yum -y install alsa-lib-devel
    yum -y install epel-release 
    curl --silent --location https://rpm.nodesource.com/setup_8.x | bash -
    yum -y install nodejs  
    yum -y install gcc-c++ make  
    yum -y install dpkg
    #yum -y install PackageKit-gtk3-module
    npm -v
    #Need to create a directory within the container
    #     to hold the application
    pwd
    mkdir /opt/hydrator
    cd /opt/hydrator
    wget https://s3.amazonaws.com/docnow-web/Hydrator_0.0.2_amd64.deb
    ar x Hydrator_0.0.2_amd64.deb
    dpkg -x Hydrator_0.0.2_amd64.deb .
    cd 

%runscript
    echo "This is a Centos container holding Hydrator"
    #hydrator
    /opt/hydrator/opt/Hydrator/hydrator

    

%files

%environment
    #export HYDRATOR_HOME=opt/Hydrator
    #export PATH="opt/Hydrator"
    #export HYDRATORPATH=${HYDRATOR_HOME}

%labels
    #AUTHOR jmh5ad@virginia.edu
```

## Collection

 - Name: [arcsUVA/hydrator](https://github.com/arcsUVA/hydrator)
 - License: None

