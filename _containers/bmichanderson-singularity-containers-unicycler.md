---
id: 5742
name: "bmichanderson/singularity-containers"
branch: "master"
tag: "unicycler"
commit: "1e140b633ee1c9db83765b86d47d0bb20338a05a"
version: "1639700170405445749e904ff044d95a"
build_date: "2021-03-24T21:42:20.929Z"
size_mb: 1095
size: 406212639
sif: "https://datasets.datalad.org/shub/bmichanderson/singularity-containers/unicycler/2021-03-24-1e140b63-16397001/1639700170405445749e904ff044d95a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bmichanderson/singularity-containers/unicycler/2021-03-24-1e140b63-16397001/
recipe: https://datasets.datalad.org/shub/bmichanderson/singularity-containers/unicycler/2021-03-24-1e140b63-16397001/Singularity
collection: bmichanderson/singularity-containers
---

# bmichanderson/singularity-containers:unicycler

```bash
$ singularity pull shub://bmichanderson/singularity-containers:unicycler
```

## Singularity Recipe

```singularity
# Author: B. Anderson
# Singularity recipe for creating a container for using the program Unicycler

Bootstrap: docker
From: ubuntu:18.04

%labels
	MAINTAINER bmichanderson
	PROGRAM Unicycler
	VERSION latest

%post
	# install essentials for obtaining and building software
	apt update
	apt upgrade -y
	apt install -y autoconf automake build-essential cmake git libtool libpthread-stubs0-dev \
			make python3-dev python3-setuptools wget zlib1g zlib1g-dev
	# install additional dependencies
	apt install -y bowtie2 ncbi-blast+ openjdk-11-jre samtools
	# SPAdes
	VERSION=3.13.0
	URL=https://github.com/ablab/spades/releases/download/v"$VERSION"/SPAdes-"$VERSION"-Linux.tar.gz
	wget "$URL"
	tar -xzf SPAdes-"$VERSION"-Linux.tar.gz
	rm SPAdes-"$VERSION"-Linux.tar.gz
	echo "export PATH=$PATH:/SPAdes-$VERSION-Linux/bin" >> $SINGULARITY_ENVIRONMENT
	# Pilon
	VERSION=1.23
	URL=https://github.com/broadinstitute/pilon/releases/download/v"$VERSION"/pilon-"$VERSION".jar
	wget "$URL"
	mv pilon-"$VERSION".jar /usr/local/bin/
	# Racon
	git clone --recursive https://github.com/isovic/racon.git racon
	cd racon
	mkdir build
	cd build
	cmake -DCMAKE_BUILD_TYPE=Release ..
	make
	make install
	cd ../..
	rm -r racon/
	# Unicycler
	git clone https://github.com/rrwick/Unicycler.git
	cd Unicycler
	./setup.py install
	cd ../
	rm -r Unicycler/
	# test that the program works
	unicycler --version

%help
	******************************************************************************
	This message is displayed when called as  >singularity run-help unicycler.img
	This container is meant to be used for running Unicycler
	Execute it as >singularity exec unicycler.img unicycler [args]
	Check contents by entering it as >singularity shell unicycler.img
	******************************************************************************
```

## Collection

 - Name: [bmichanderson/singularity-containers](https://github.com/bmichanderson/singularity-containers)
 - License: None

