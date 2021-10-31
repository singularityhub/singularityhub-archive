---
id: 6776
name: "powerPlant/portcullis-srf"
branch: "master"
tag: "1.1.1"
commit: "6e990061f68d57fd0453b26c2295d86138dee0b4"
version: "3b4f80dcdf7d8ceb0e76c79264a4d254"
build_date: "2019-02-05T05:54:32.417Z"
size_mb: 681
size: 222298143
sif: "https://datasets.datalad.org/shub/powerPlant/portcullis-srf/1.1.1/2019-02-05-6e990061-3b4f80dc/3b4f80dcdf7d8ceb0e76c79264a4d254.simg"
url: https://datasets.datalad.org/shub/powerPlant/portcullis-srf/1.1.1/2019-02-05-6e990061-3b4f80dc/
recipe: https://datasets.datalad.org/shub/powerPlant/portcullis-srf/1.1.1/2019-02-05-6e990061-3b4f80dc/Singularity
collection: powerPlant/portcullis-srf
---

# powerPlant/portcullis-srf:1.1.1

```bash
$ singularity pull shub://powerPlant/portcullis-srf:1.1.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: fedora:27

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 1.1.1

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
wget -q https://github.com/maplesond/portcullis/archive/Release-1.1.1.tar.gz
tar -xvf Release-1.1.1.tar.gz
cd portcullis-Release-1.1.1
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
exec portcullis "$@"
```

## Collection

 - Name: [powerPlant/portcullis-srf](https://github.com/powerPlant/portcullis-srf)
 - License: None

