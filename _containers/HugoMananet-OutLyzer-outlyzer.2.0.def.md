---
id: 5748
name: "HugoMananet/OutLyzer"
branch: "master"
tag: "outlyzer.2.0.def"
commit: "bfd00035885ee17290ef57a1a9d79197a8537d7b"
version: "9aed1fe53b8bd1aecac97fd00dc5a010"
build_date: "2018-12-03T17:26:31.917Z"
size_mb: 653
size: 257019935
sif: "https://datasets.datalad.org/shub/HugoMananet/OutLyzer/outlyzer.2.0.def/2018-12-03-bfd00035-9aed1fe5/9aed1fe53b8bd1aecac97fd00dc5a010.simg"
url: https://datasets.datalad.org/shub/HugoMananet/OutLyzer/outlyzer.2.0.def/2018-12-03-bfd00035-9aed1fe5/
recipe: https://datasets.datalad.org/shub/HugoMananet/OutLyzer/outlyzer.2.0.def/2018-12-03-bfd00035-9aed1fe5/Singularity
collection: HugoMananet/OutLyzer
---

# HugoMananet/OutLyzer:outlyzer.2.0.def

```bash
$ singularity pull shub://HugoMananet/OutLyzer:outlyzer.2.0.def
```

## Singularity Recipe

```singularity
#!/bin/bash
Bootstrap: docker
From: phusion/baseimage:0.10.2


%label

	MAINTAINER Hugo Mananet
	VERSION 2.0
	
	
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
	python-wheel \
	python-subprocess32 \
	python-numpy \
	python-scipy \
	libpython2.7-stdlib \
	python-pip

	pip install --upgrade pip
	python2.7 -m pip install multiprocessing
	
	mkdir -p /opt/
	wget https://github.com/samtools/samtools/releases/download/1.3/samtools-1.3.tar.bz2 && mv samtools-1.3.tar.bz2 /opt/
	cd /opt/ && tar xjvf samtools-1.3.tar.bz2

	cd /opt/samtools-1.3/ && ./configure && make
	cd /opt/ && rm samtools-1.3.tar.bz2

	ln -s /opt/samtools-1.3/samtools /bin
	ln -s /opt/samtools-1.3/misc/* /bin
	
	wget -P /opt/ https://github.com/EtieM/outLyzer/archive/v2.tar.gz
	# mv v2.tar.gz /opt/v2.tar.gz
	cd /opt/ && tar xzvf v2.tar.gz
	rm /opt/v2.tar.gz 
	## ou "v2" uniquement (a tester)
	
	chmod 755 /opt/outLyzer-2/outLyzer.py
	ln -s /opt/outLyzer-2/outLyzer.py /usr/local/bin/outlyzer.py
	
	
%environment

	# export samtools=/path/to/samtools
	
%runscript

	exec outlyzer.py "$@"
```

## Collection

 - Name: [HugoMananet/OutLyzer](https://github.com/HugoMananet/OutLyzer)
 - License: None

