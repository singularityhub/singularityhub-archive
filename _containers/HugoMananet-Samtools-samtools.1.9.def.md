---
id: 5785
name: "HugoMananet/Samtools"
branch: "master"
tag: "samtools.1.9.def"
commit: "e30452a4092515740d2e4dd19dd1e004d3385177"
version: "f7f0a774efe9cab1c6688287f2b4b055"
build_date: "2018-12-03T17:26:31.312Z"
size_mb: 537
size: 187658271
sif: "https://datasets.datalad.org/shub/HugoMananet/Samtools/samtools.1.9.def/2018-12-03-e30452a4-f7f0a774/f7f0a774efe9cab1c6688287f2b4b055.simg"
url: https://datasets.datalad.org/shub/HugoMananet/Samtools/samtools.1.9.def/2018-12-03-e30452a4-f7f0a774/
recipe: https://datasets.datalad.org/shub/HugoMananet/Samtools/samtools.1.9.def/2018-12-03-e30452a4-f7f0a774/Singularity
collection: HugoMananet/Samtools
---

# HugoMananet/Samtools:samtools.1.9.def

```bash
$ singularity pull shub://HugoMananet/Samtools:samtools.1.9.def
```

## Singularity Recipe

```singularity
#!/bin/bash
#

Bootstrap: docker
From: phusion/baseimage:0.11

%label

	MAINTAINER Hugo Mananet


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


	mkdir -p /opt/
	wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 && mv samtools-1.9.tar.bz2 /opt/
	wget https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2 && mv bcftools-1.9.tar.bz2 /opt/
	cd /opt/ && tar xjvf samtools-1.9.tar.bz2 && tar xjvf bcftools-1.9.tar.bz2

	cd /opt/samtools-1.9/ && ./configure && make
	cd /opt/ && rm samtools-1.9.tar.bz2

	cd /opt/bcftools-1.9/ && ./configure && make
	cd /opt/ && rm bcftools-1.9.tar.bz2

	ln -s /opt/samtools-1.9/samtools /bin
	ln -s /opt/bcftools-1.9/bcftools /bin
	ln -s /opt/samtools-1.9/misc/* /bin
	ln -s /opt/bcftools-1.9/misc/* /bin
```

## Collection

 - Name: [HugoMananet/Samtools](https://github.com/HugoMananet/Samtools)
 - License: [Other](None)

