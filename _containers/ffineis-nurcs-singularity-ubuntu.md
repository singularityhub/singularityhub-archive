---
id: 3621
name: "ffineis/nurcs-singularity"
branch: "master"
tag: "ubuntu"
commit: "0d69068d97f8154011feee238084bfa915665bb6"
version: "4a2f0f3af3ae76f3b0ad26c38c31f5a3"
build_date: "2020-03-02T18:13:40.013Z"
size_mb: 717
size: 307204127
sif: "https://datasets.datalad.org/shub/ffineis/nurcs-singularity/ubuntu/2020-03-02-0d69068d-4a2f0f3a/4a2f0f3af3ae76f3b0ad26c38c31f5a3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ffineis/nurcs-singularity/ubuntu/2020-03-02-0d69068d-4a2f0f3a/
recipe: https://datasets.datalad.org/shub/ffineis/nurcs-singularity/ubuntu/2020-03-02-0d69068d-4a2f0f3a/Singularity
collection: ffineis/nurcs-singularity
---

# ffineis/nurcs-singularity:ubuntu

```bash
$ singularity pull shub://ffineis/nurcs-singularity:ubuntu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment

    # Set system locale
    export LC_ALL=C

%post

    # ------------------------------------------------ #
    #                   Kernel overhead                #
    # ------------------------------------------------ #

    apt-get -y update && apt-get -y upgrade
    apt-get -y --allow-unauthenticated install \
    apt-utils \
	autoconf \
	automake \
	build-essential \
	cmake \
	curl \
	git \
	gfortran \
	libtool \
	libssl-dev \
	libffi-dev \
	libxslt1-dev \
	libxml2-dev \
	pkg-config \
	python-dev \
	python-pip \
	python-tk \
	python-wheel \
	python3-dev \
	python3-pip \
	python3-wheel \
	unzip \
	wget \
	zip \
	zlib1g-dev


    # ------------------------------------------------ #
    #                   Mount bind points              #
    # note: not necessary if `enable overlay = yes`,   #
    # appears to be the case on Quest				   #
    # ------------------------------------------------ #

    mkdir /software

%test

	cat /usr/lib/os-release

%files

    singularity_logo.txt /opt

%runscript

    cat /opt/singularity_logo.txt

%environment
```

## Collection

 - Name: [ffineis/nurcs-singularity](https://github.com/ffineis/nurcs-singularity)
 - License: None

