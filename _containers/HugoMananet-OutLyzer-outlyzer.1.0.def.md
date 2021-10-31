---
id: 5747
name: "HugoMananet/OutLyzer"
branch: "master"
tag: "outlyzer.1.0.def"
commit: "f01fe8ddf868ab7205e4e30bbf2cc6d1c7c306ce"
version: "2f4d7341b222b38a704fe765e0df8b4c"
build_date: "2018-12-03T17:26:31.908Z"
size_mb: 653
size: 257019935
sif: "https://datasets.datalad.org/shub/HugoMananet/OutLyzer/outlyzer.1.0.def/2018-12-03-f01fe8dd-2f4d7341/2f4d7341b222b38a704fe765e0df8b4c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/HugoMananet/OutLyzer/outlyzer.1.0.def/2018-12-03-f01fe8dd-2f4d7341/
recipe: https://datasets.datalad.org/shub/HugoMananet/OutLyzer/outlyzer.1.0.def/2018-12-03-f01fe8dd-2f4d7341/Singularity
collection: HugoMananet/OutLyzer
---

# HugoMananet/OutLyzer:outlyzer.1.0.def

```bash
$ singularity pull shub://HugoMananet/OutLyzer:outlyzer.1.0.def
```

## Singularity Recipe

```singularity
#!/bin/bash

Bootstrap: docker
From: phusion/baseimage:0.10.2


%label

	MAINTAINER Hugo Mananet
	VERSION 1.0
	

%files

	outLyzer.py /opt/outLyzer.py
	
%post

	mkdir /soft
	mkdir /work
	mkdir /user1
	mkdir /user2
	mkdir /tmp3
	
	apt-get -y update
	apt-get -y install build-essential \
	wget \
	make \
	gcc \
	autoconf \
	perl \
	ca-certificates \
	curl \
	libbz2-dev \
	liblzma-dev \
	libncurses5-dev \
	libncursesw5-dev \
	zlib1g-dev \
	python2.7 \
	python-setuptools \
	python-dev \
	python-pip \
	python-wheel \
	python-subprocess32 \
	python-numpy \
	python-scipy \
	libpython2.7-stdlib 
	
	pip install --upgrade pip
	python2.7 -m pip install multiprocessing
	
	mkdir -p /opt/
	wget https://github.com/samtools/samtools/releases/download/1.3/samtools-1.3.tar.bz2 && mv samtools-1.3.tar.bz2 /opt/
	cd /opt/ && tar xjvf samtools-1.3.tar.bz2

	cd /opt/samtools-1.3/ && ./configure && make
	cd /opt/ && rm samtools-1.3.tar.bz2

	ln -s /opt/samtools-1.3/samtools /bin
	ln -s /opt/samtools-1.3/misc/* /bin
	
	
	chmod 755 /opt/outLyzer.py
	ln -s /opt/outLyzer.py /usr/local/bin/outlyzer.py
	
	
%environment

	# export samtools=/path/to/samtools
	
%runscript

	exec outlyzer.py "$@"
```

## Collection

 - Name: [HugoMananet/OutLyzer](https://github.com/HugoMananet/OutLyzer)
 - License: None

