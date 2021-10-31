---
id: 8635
name: "raorr/amuse-11.2-singularity"
branch: "master"
tag: "latest"
commit: "c26d536087770165289e9d1f8b311b975bc112ea"
version: "b9cc7022b883da56af57c02b62feae30"
build_date: "2019-04-24T22:19:52.095Z"
size_mb: 7649
size: 3934949407
sif: "https://datasets.datalad.org/shub/raorr/amuse-11.2-singularity/latest/2019-04-24-c26d5360-b9cc7022/b9cc7022b883da56af57c02b62feae30.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/raorr/amuse-11.2-singularity/latest/2019-04-24-c26d5360-b9cc7022/
recipe: https://datasets.datalad.org/shub/raorr/amuse-11.2-singularity/latest/2019-04-24-c26d5360-b9cc7022/Singularity
collection: raorr/amuse-11.2-singularity
---

# raorr/amuse-11.2-singularity:latest

```bash
$ singularity pull shub://raorr/amuse-11.2-singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:10.0-devel-ubuntu16.04

%environment
	FC=gfortran
	F77=gfortran

%post
	apt-get update && apt-get install -y git wget
	apt-get install -y build-essential curl g++ gfortran gettext zlib1g-dev

	wget https://github.com/amusecode/amuse/archive/release-11.2.tar.gz
	tar -xf release-11.2.tar.gz
	mv amuse-release-11.2/ /amuse/

	apt-get install -y build-essential gfortran python-dev \
	  openmpi-bin libopenmpi-dev \
	  libgsl0-dev cmake libfftw3-3 libfftw3-dev \
	  libgmp3-dev libmpfr-dev \
	  libhdf5-serial-dev hdf5-tools \
	  python-nose python-numpy python-setuptools python-docutils \
	  python-h5py python-setuptools git openjdk-8-jdk python-pip

	pip install cython scipy mpi4py
	
	echo "export PATH=/amuse/:${PATH}" >> /etc/profile

	cd /amuse/ && ./configure --enable-cuda --with-cuda-libdir=/usr/local/cuda/lib64
	cd /amuse/ && make DOWNLOAD_CODES=1

	chmod 755 /amuse/amuse.sh
	# make the home and data folders from ACCRE available for this image
	mkdir /scratch /data /gpfs22 /gpfs23
```

## Collection

 - Name: [raorr/amuse-11.2-singularity](https://github.com/raorr/amuse-11.2-singularity)
 - License: None

