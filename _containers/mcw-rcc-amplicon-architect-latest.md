---
id: 4691
name: "mcw-rcc/amplicon-architect"
branch: "master"
tag: "latest"
commit: "a4df5f78b3cc65f6705a21463d4318e96db05eb0"
version: "61b1b0db4b1cc6d57cd6c8516b184156"
build_date: "2018-09-07T02:36:52.701Z"
size_mb: 756
size: 340357151
sif: "https://datasets.datalad.org/shub/mcw-rcc/amplicon-architect/latest/2018-09-07-a4df5f78-61b1b0db/61b1b0db4b1cc6d57cd6c8516b184156.simg"
url: https://datasets.datalad.org/shub/mcw-rcc/amplicon-architect/latest/2018-09-07-a4df5f78-61b1b0db/
recipe: https://datasets.datalad.org/shub/mcw-rcc/amplicon-architect/latest/2018-09-07-a4df5f78-61b1b0db/Singularity
collection: mcw-rcc/amplicon-architect
---

# mcw-rcc/amplicon-architect:latest

```bash
$ singularity pull shub://mcw-rcc/amplicon-architect:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Maintainer Matthew Flister
Version 09.06.18

%help
This container runs AmpliconArchitect.

%environment
    SHELL=/bin/bash
    PATH=/opt/programs/mosek/8/tools/platform/linux64x86/bin:$PATH
    LD_LIBRARY_PATH=/opt/programs/mosek/8/tools/platform/linux64x86/bin:$LD_LIBRARY_PATH
    MOSEKLM_LICENSE_FILE=/home/$USER/.mosek/8/licenses
    AA_DATA_REPO=/rcc/stor1/refdata/ampliconarchitect/data_repo
    AA_SRC=/opt/programs/AmpliconArchitect-master/src
    export SHELL PATH LD_LIBRARY_PATH  MOSEKLM_LICENSE_FILE AA_DATA_REPO AA_SRC

%post
    # default mount points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts

    # install packages
    apt-get update && apt-get install -y --no-install-recommends \
	build-essential \
	python-dev \
	gfortran \
	python-numpy \
	python-scipy \
	python-matplotlib \
	python-pip \
	python-setuptools \
	zlib1g-dev \
	samtools \
	wget \
	unzip
    apt-get clean


    # python packages
    pip install pysam Flask

    # install mosek
    mkdir -p /opt/programs
    mkdir -p /opt/output
    mkdir -p /opt/input
    cd /opt/programs && wget http://download.mosek.com/stable/8.0.0.60/mosektoolslinux64x86.tar.bz2
    cd /opt/programs && tar xf mosektoolslinux64x86.tar.bz2
    cd /opt/programs/mosek/8/tools/platform/linux64x86/python/2/ && python setup.py install

    # install ampliconarchitect
    cd /opt/programs && wget https://github.com/virajbdeshpande/AmpliconArchitect/archive/master.zip
    cd /opt/programs && unzip master.zip
```

## Collection

 - Name: [mcw-rcc/amplicon-architect](https://github.com/mcw-rcc/amplicon-architect)
 - License: [MIT License](https://api.github.com/licenses/mit)

