---
id: 5814
name: "bmichanderson/singularity-containers"
branch: "master"
tag: "quast"
commit: "5f21120a98d535c84876c1b4eaca8179ccb03136"
version: "fde3a958d2207658cb680e0d8a9733e3"
build_date: "2018-12-06T22:06:25.264Z"
size_mb: 624
size: 197165087
sif: "https://datasets.datalad.org/shub/bmichanderson/singularity-containers/quast/2018-12-06-5f21120a-fde3a958/fde3a958d2207658cb680e0d8a9733e3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bmichanderson/singularity-containers/quast/2018-12-06-5f21120a-fde3a958/
recipe: https://datasets.datalad.org/shub/bmichanderson/singularity-containers/quast/2018-12-06-5f21120a-fde3a958/Singularity
collection: bmichanderson/singularity-containers
---

# bmichanderson/singularity-containers:quast

```bash
$ singularity pull shub://bmichanderson/singularity-containers:quast
```

## Singularity Recipe

```singularity
# Author: B. Anderson
# Singularity recipe for creating a container for using the program QUAST

Bootstrap: docker
From: ubuntu:18.04

%labels
	MAINTAINER bmichanderson

%post
	# install essentials for obtaining and building software, and dependencies
	apt update
	apt upgrade -y
	export DEBIAN_FRONTEND=noninteractive
	apt install -y build-essential libfreetype6-dev libpng-dev locales make pkg-config python-matplotlib python-setuptools wget zlib1g-dev

	# set locale 
	# from https://github.com/ablab/quast/issues/70
	# and https://serverfault.com/questions/362903/how-do-you-set-a-locale-non-interactively-on-debian-ubuntu
	locale-gen en_US.UTF-8
	dpkg-reconfigure tzdata -f noninteractive
	dpkg-reconfigure locales -f noninteractive
	update-locale en_US.UTF-8

	# download and extract QUAST
	VERSION=5.0.2
	URL=https://downloads.sourceforge.net/project/quast/quast-"$VERSION".tar.gz
	wget "$URL"
	tar -xzf quast-"$VERSION".tar.gz
	rm quast*.tar.gz

	# install
	cd quast-"$VERSION"
	python setup.py install

	# remove quast download and folder
	cd ..
	rm -r quast-"$VERSION"/

	# test that the program works
	quast.py --version

%help
	******************************************************************************
	This message is displayed when called as  >singularity run-help quast.img
	This container is meant to be used for running QUAST
	Execute it as >singularity exec quast.img quast.py [args]
	Check contents by entering it as >singularity shell quast.img
	******************************************************************************
```

## Collection

 - Name: [bmichanderson/singularity-containers](https://github.com/bmichanderson/singularity-containers)
 - License: None

