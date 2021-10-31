---
id: 5096
name: "keceli/container_nwchem"
branch: "master"
tag: "mpich"
commit: "48bb3daf97693115b06509635ba94ee874293120"
version: "df5c12c1ac425da477071c06657f1478"
build_date: "2018-10-03T03:26:38.352Z"
size_mb: 798
size: 224067615
sif: "https://datasets.datalad.org/shub/keceli/container_nwchem/mpich/2018-10-03-48bb3daf-df5c12c1/df5c12c1ac425da477071c06657f1478.simg"
url: https://datasets.datalad.org/shub/keceli/container_nwchem/mpich/2018-10-03-48bb3daf-df5c12c1/
recipe: https://datasets.datalad.org/shub/keceli/container_nwchem/mpich/2018-10-03-48bb3daf-df5c12c1/Singularity
collection: keceli/container_nwchem
---

# keceli/container_nwchem:mpich

```bash
$ singularity pull shub://keceli/container_nwchem:mpich
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%setup
   echo ${SINGULARITY_ROOTFS}
   mkdir ${SINGULARITY_ROOTFS}/container
  
%post
   yum update -y
   yum groupinstall -y "Development Tools"
   yum install -y gcc
   yum install -y gcc-c++
   yum install -y wget
   yum install -y git
   yum install -y ca-certificates
   wget http://www.mpich.org/static/downloads/3.2.1/mpich-3.2.1.tar.gz
   tar xf mpich-3.2.1.tar.gz
   rm -f mpich-3.2.1.tar.gz
   cd mpich-3.2.1
   ./configure --prefix=$PWD/install --disable-wrapper-rpath
   make -j 4 install
   export PATH=$PATH:$PWD/install/bin
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PWD/install/lib
   cd /container
   git clone https://github.com/LLNL/mpiBench
   cd mpiBench
   mpicc -o mpibench -fPIC mpiBench.c
   
%runscript
   /container/mpiBench/mpibench
```

## Collection

 - Name: [keceli/container_nwchem](https://github.com/keceli/container_nwchem)
 - License: None

