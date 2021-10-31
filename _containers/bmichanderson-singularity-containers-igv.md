---
id: 5819
name: "bmichanderson/singularity-containers"
branch: "master"
tag: "igv"
commit: "5de5d238ee3408730dc5302df3b4e0c109a824cc"
version: "e2749464efee81fdb6398e1f1299ec0c"
build_date: "2018-12-07T19:40:53.960Z"
size_mb: 514
size: 219459615
sif: "https://datasets.datalad.org/shub/bmichanderson/singularity-containers/igv/2018-12-07-5de5d238-e2749464/e2749464efee81fdb6398e1f1299ec0c.simg"
url: https://datasets.datalad.org/shub/bmichanderson/singularity-containers/igv/2018-12-07-5de5d238-e2749464/
recipe: https://datasets.datalad.org/shub/bmichanderson/singularity-containers/igv/2018-12-07-5de5d238-e2749464/Singularity
collection: bmichanderson/singularity-containers
---

# bmichanderson/singularity-containers:igv

```bash
$ singularity pull shub://bmichanderson/singularity-containers:igv
```

## Singularity Recipe

```singularity
# Author: B. Anderson
# Singularity recipe for creating a container for using the program IGV

Bootstrap: docker
From: ubuntu:18.04

%labels
	MAINTAINER bmichanderson
	PROGRAM IGV
	VERSION 2.4.16

%post
	# install java and needed packages
	apt update
	apt upgrade -y
	export DEBIAN_FRONTEND=noninteractive
	apt install -y glib-networking-common libcanberra-gtk-module locales openjdk-8-jre unzip wget

	# set locale
	locale-gen en_US.UTF-8
	dpkg-reconfigure locales -f noninteractive
	update-locale en_US.UTF-8

	# download IGV
	VERSION=2.4.16
	URL=http://data.broadinstitute.org/igv/projects/downloads/2.4/IGV_"$VERSION".zip
	wget "$URL"
	unzip IGV_"$VERSION".zip
	echo "export PATH=$PATH:/IGV_$VERSION" >> $SINGULARITY_ENVIRONMENT

%environment
	# set locale
	export LC_ALL=en_US.UTF-8

%help
	******************************************************************************
	This message is displayed when called as  >singularity run-help igv.img
	This container is meant to be used for running IGV
	Execute it as >singularity exec igv.img igv.sh
	Check contents by entering it as >singularity shell igv.img
	******************************************************************************
```

## Collection

 - Name: [bmichanderson/singularity-containers](https://github.com/bmichanderson/singularity-containers)
 - License: None

