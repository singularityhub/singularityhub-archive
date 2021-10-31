---
id: 5735
name: "bmichanderson/singularity-containers"
branch: "master"
tag: "kat"
commit: "8640a1241da34c9608c6cb2437af7b637e3028e2"
version: "89f40eeb40d0f660e3d28cc5c338c405"
build_date: "2021-04-06T11:13:12.547Z"
size_mb: 689
size: 261898271
sif: "https://datasets.datalad.org/shub/bmichanderson/singularity-containers/kat/2021-04-06-8640a124-89f40eeb/89f40eeb40d0f660e3d28cc5c338c405.simg"
url: https://datasets.datalad.org/shub/bmichanderson/singularity-containers/kat/2021-04-06-8640a124-89f40eeb/
recipe: https://datasets.datalad.org/shub/bmichanderson/singularity-containers/kat/2021-04-06-8640a124-89f40eeb/Singularity
collection: bmichanderson/singularity-containers
---

# bmichanderson/singularity-containers:kat

```bash
$ singularity pull shub://bmichanderson/singularity-containers:kat
```

## Singularity Recipe

```singularity
# Author: B. Anderson
# Description: a Singularity definition file for creating a container for using the program KAT (Kmer Analysis Toolkit)

Bootstrap: docker
From: ubuntu:18.04

%labels
	# This section contains labels for the container
	MAINTAINER bmichanderson
	PROGRAM KAT
	VERSION latest

%post
	# This section is executed after the base OS has been installed
	# Upgrade software and install essentials for building KAT
	apt update
	apt upgrade -y
	export DEBIAN_FRONTEND=noninteractive
	apt install -y autoconf automake build-essential git libtool libpthread-stubs0-dev make \
			python3-dev python3-matplotlib python3-numpy python3-scipy python3-sphinx \
			python3-setuptools python3-tabulate wget zlib1g zlib1g-dev
	# Install KAT
	git clone https://github.com/TGAC/KAT.git
	cd KAT
	./build_boost.sh
	./autogen.sh
	./configure
	# can leverage extra cores with the -j option
	make -j6
	make install
	cd ../
	rm -r KAT/
	# test that the program works
	kat --version

%help
	******************************************************************************
	This message is displayed when called as  >singularity run-help kat.img
	This container is meant to be used for running KAT (Kmer Analysis Toolkit)
	Execute it as >singularity exec kat.img kat [args]
	Check contents by entering it as >singularity shell kat.img
	******************************************************************************
```

## Collection

 - Name: [bmichanderson/singularity-containers](https://github.com/bmichanderson/singularity-containers)
 - License: None
