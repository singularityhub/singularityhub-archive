---
id: 9924
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "molden"
commit: "6612464ea3924586762b2c53577a404c9f98776a"
version: "3f1e81e29a3e4550854922020b0e6918"
build_date: "2019-06-21T11:07:46.685Z"
size_mb: 1252
size: 445980703
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/molden/2019-06-21-6612464e-3f1e81e2/3f1e81e29a3e4550854922020b0e6918.simg"
url: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/molden/2019-06-21-6612464e-3f1e81e2/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/molden/2019-06-21-6612464e-3f1e81e2/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:molden

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:molden
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:centos:centos7.4.1708

%labels
MAINTAINER Thomas Green

%environment

%runscript
exec /bin/bash /bin/echo "Not supported"

%post  
yum -y install yum-utils
yum -y install epel-release
yum -y groupinstall "Base"
yum -y groupinstall "Development Tools"

#Install dependency
yum -y install libX11
yum -y install mesa-libGL
yum -y install mesa-libGLU
yum -y install mesa-libGLU-devel
yum -y install libXmu
yum -y install libXmu-devel
yum -y install imake


#Install software
cd /tmp
wget ftp://ftp.cmbi.umcn.nl/pub/molgraph/molden/molden5.9.tar.gz
tar zxvf molden5.9.tar.gz
cd molden5.9
# Remove use of sudo from makefile.
sed -i 's/sudo //g' makefile

make
make install
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

