---
id: 12928
name: "thakk/TOBIAS"
branch: "master"
tag: "latest"
commit: "72620fdc2f31e1542dfbabe72d9ca9509fcc1ed2"
version: "ede4b4d7fa616796dd36d16f7a587ac9"
build_date: "2020-05-07T08:20:03.857Z"
size_mb: 2558.0
size: 1073086495
sif: "https://datasets.datalad.org/shub/thakk/TOBIAS/latest/2020-05-07-72620fdc-ede4b4d7/ede4b4d7fa616796dd36d16f7a587ac9.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/thakk/TOBIAS/latest/2020-05-07-72620fdc-ede4b4d7/
recipe: https://datasets.datalad.org/shub/thakk/TOBIAS/latest/2020-05-07-72620fdc-ede4b4d7/Singularity
collection: thakk/TOBIAS
---

# thakk/TOBIAS:latest

```bash
$ singularity pull shub://thakk/TOBIAS:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
#From: alpine:3.11.6
From: centos:8
Stage: compile

%post
	#echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
	#apk update
	#apk add bash
	#apk add git
	#apk add build-base
    #apk add zlib
    #apk add zlib-dev
    #apk add bzip2
    #apk add bzip2-dev
    #apk add xz
    #apk add xz-dev
	#apk add gcc
	#apk add gfortran
	#apk add python3
	#apk add python3-dev
	#apk add py3-scipy
	#apk add py3-matplotlib
	#apk add lapack
	#apk add lapack-dev
	#apk add freetype
	#ln -s `which python3` /bin/python
	dnf -y makecache
	dnf -y group install "Development Tools"
	dnf -y install --allowerasing hostname which dnf-utils
	dnf -y install --allowerasing python3 python3-devel
	dnf -y install --allowerasing python3-pip git zlib zlib-devel bzip2 bzip2-devel \
      xz xz-devel libcurl libcurl-devel ncurses ncurses-devel \
      unzip wget
	ln -s /usr/bin/python3 /usr/bin/python
	ln -s /usr/bin/pip3 /usr/bin/pip
	pip install Cython numpy pandas matplotlib scipy botocore
	dnf install -y epel-release
	dnf config-manager --set-enabled PowerTools
	dnf install -y ImageMagick ImageMagick-devel
	pip install wand

%apprun TOBIAS
   exec TOBIAS

%appinstall TOBIAS
	mkdir /install_src
    cd /install_src
    git clone https://github.com/arq5x/bedtools2/
    cd bedtools2
    make -j 8
    make install
	#pip3 install matplotlib
	#pip3 install Cython
	pip install gimmemotifs
	pip install tobias

%apphelp bedtools
   TOBIAS https://github.com/loosolab/TOBIAS
```

## Collection

 - Name: [thakk/TOBIAS](https://github.com/thakk/TOBIAS)
 - License: None

