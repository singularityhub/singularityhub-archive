---
id: 5206
name: "HugoMananet/Samtools"
branch: "master"
tag: "0.1.18"
commit: "8b245a1a57e77bd89d13044e17aefd905e7db0da"
version: "c0bc86a9062a3f17ebd69633d4bb8546"
build_date: "2018-10-12T03:09:53.179Z"
size_mb: 439
size: 161325087
sif: "https://datasets.datalad.org/shub/HugoMananet/Samtools/0.1.18/2018-10-12-8b245a1a-c0bc86a9/c0bc86a9062a3f17ebd69633d4bb8546.simg"
url: https://datasets.datalad.org/shub/HugoMananet/Samtools/0.1.18/2018-10-12-8b245a1a-c0bc86a9/
recipe: https://datasets.datalad.org/shub/HugoMananet/Samtools/0.1.18/2018-10-12-8b245a1a-c0bc86a9/Singularity
collection: HugoMananet/Samtools
---

# HugoMananet/Samtools:0.1.18

```bash
$ singularity pull shub://HugoMananet/Samtools:0.1.18
```

## Singularity Recipe

```singularity
#!/bin/bash
#

Bootstrap: docker
From: phusion/baseimage:0.11

%label
	MAINTAINER Hugo Mananet
	VERSION 2.3.6


%post
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
	wget https://sourceforge.net/projects/samtools/files/samtools/0.1.18/samtools-0.1.18.tar.bz2 && mv samtools-0.1.18.tar.bz2 /opt/

	cd /opt/ && tar xjvf samtools-0.1.18.tar.bz2
	cd /opt/samtools-0.1.18/ && make
	cd /opt/ && rm samtools-0.1.18.tar.bz2
	cp /opt/samtools-0.1.18/samtools /opt/samtools-0.1.18/misc/
	cp /opt/samtools-0.1.18/bcftools/bcftools /opt/samtools-0.1.18/misc/
	cp /opt/samtools-0.1.18/bcftools/vcfutils.pl /opt/samtools-0.1.18/misc/
	ln -s /opt/samtools-0.1.18/misc/samtools /bin
	ln -s /opt/samtools-0.1.18/misc/bcftools /bin
	ln -s /opt/samtools-0.1.18/misc/wgsim /bin
	ln -s /opt/samtools-0.1.18/misc/seqtk /bin
	ln -s /opt/samtools-0.1.18/misc/maq2sam-long /bin
	ln -s /opt/samtools-0.1.18/misc/maq2sam-short /bin
	ln -s /opt/samtools-0.1.18/misc/*.pl /bin
	ln -s /opt/samtools-0.1.18/misc/*.py /bin
```

## Collection

 - Name: [HugoMananet/Samtools](https://github.com/HugoMananet/Samtools)
 - License: [Other](None)

