---
id: 6785
name: "powerPlant/portcullis-srf"
branch: "master"
tag: "latest"
commit: "702718d1beebc165e42f5b256c7976d76de962dc"
version: "c2719658bbf639c3b596136a5c0591b0"
build_date: "2019-09-26T16:48:48.047Z"
size_mb: 669
size: 218681375
sif: "https://datasets.datalad.org/shub/powerPlant/portcullis-srf/latest/2019-09-26-702718d1-c2719658/c2719658bbf639c3b596136a5c0591b0.simg"
url: https://datasets.datalad.org/shub/powerPlant/portcullis-srf/latest/2019-09-26-702718d1-c2719658/
recipe: https://datasets.datalad.org/shub/powerPlant/portcullis-srf/latest/2019-09-26-702718d1-c2719658/Singularity
collection: powerPlant/portcullis-srf
---

# powerPlant/portcullis-srf:latest

```bash
$ singularity pull shub://powerPlant/portcullis-srf:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: fedora:27

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 1.1.2

%post
## Install required packages
dnf install -y autoconf automake bzip2 bzip2-devel gcc gcc-c++ git libgomp libtool libstdc++-static make perl python35 python3-devel wget which xz xz-devel zlib zlib-devel
 
pip3.6 install pandas
pip3.6 install sphinx

## samtools compilation
wget -q https://github.com/samtools/samtools/releases/download/1.6/samtools-1.6.tar.bz2
tar -xvf samtools-1.6.tar.bz2
cd samtools-1.6
./configure --without-curses
make -j2
make install
cd ..

## portcullis compilation
wget -q https://github.com/maplesond/portcullis/archive/Release-1.1.2.tar.gz
tar -xvf Release-1.1.2.tar.gz
cd portcullis-Release-1.1.2
./autogen.sh
./build_boost.sh
./configure
make 
make install

echo "/portcullis/deps/boost/build/lib/" > /etc/ld.so.conf.d/portcullis.conf 
ldconfig

## clean up
dnf -y remove autoconf automake bzip2-devel gcc gcc-c++ git make python3-devel wget which xz-devel zlib-devel
dnf -y clean all
rm -rf /samtools* /portcullis* /Release-*

%runscript
portcullis "$@"
```

## Collection

 - Name: [powerPlant/portcullis-srf](https://github.com/powerPlant/portcullis-srf)
 - License: None

