---
id: 6199
name: "bmichanderson/singularity-containers"
branch: "master"
tag: "gapfiller"
commit: "be8c5472a894bc077d53174d06cae0931e7d62bd"
version: "9f2687e46f04ecf264f99ce6bafe1501"
build_date: "2019-01-11T19:36:04.242Z"
size_mb: 580
size: 177541151
sif: "https://datasets.datalad.org/shub/bmichanderson/singularity-containers/gapfiller/2019-01-11-be8c5472-9f2687e4/9f2687e46f04ecf264f99ce6bafe1501.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bmichanderson/singularity-containers/gapfiller/2019-01-11-be8c5472-9f2687e4/
recipe: https://datasets.datalad.org/shub/bmichanderson/singularity-containers/gapfiller/2019-01-11-be8c5472-9f2687e4/Singularity
collection: bmichanderson/singularity-containers
---

# bmichanderson/singularity-containers:gapfiller

```bash
$ singularity pull shub://bmichanderson/singularity-containers:gapfiller
```

## Singularity Recipe

```singularity
# Author: B. Anderson
# Singularity recipe for creating a container for using the program GapFiller

Bootstrap: docker
From: debian:7

%labels
	MAINTAINER bmichanderson
	PROGRAM GapFiller
	VERSION 2.1.1

%post
	# install dependencies
	apt-get update
	apt-get upgrade -y
	export DEBIAN_FRONTEND=noninteractive
	apt-get install -y build-essential gzip make libboost-all-dev tar wget zlib1g zlib1g-dev

	# download GapFiller and compile and make
	URL=https://sourceforge.net/projects/gapfiller/files/latest/download
	wget --no-check-certificate "$URL"
	tar -xzf download
	rm download
	cd gapfiller-2.1.1
	./configure; make; make install
	cd ..
	rm -r gapfiller-2.1.1
	#echo "export PATH=$PATH:/gapfiller-2.1.1/src" >> $SINGULARITY_ENVIRONMENT

%help
	******************************************************************************
	This message is displayed when called as  >singularity run-help gapfiller.img
	This container is meant to be used for running GapFiller
	Execute it as >singularity exec gapfiller.img GapFiller
	Check contents by entering it as >singularity shell gapfiller.img
	******************************************************************************
```

## Collection

 - Name: [bmichanderson/singularity-containers](https://github.com/bmichanderson/singularity-containers)
 - License: None

