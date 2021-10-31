---
id: 4014
name: "ffineis/nurcs-singularity"
branch: "master"
tag: "tensorflow_gpu"
commit: "edc49cef182f835f16bf6ad5a3af389cea88248c"
version: "6ed46c199466729639ef9699e05e9efe"
build_date: "2018-08-16T07:54:17.355Z"
size_mb: 3447
size: 1625993247
sif: "https://datasets.datalad.org/shub/ffineis/nurcs-singularity/tensorflow_gpu/2018-08-16-edc49cef-6ed46c19/6ed46c199466729639ef9699e05e9efe.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ffineis/nurcs-singularity/tensorflow_gpu/2018-08-16-edc49cef-6ed46c19/
recipe: https://datasets.datalad.org/shub/ffineis/nurcs-singularity/tensorflow_gpu/2018-08-16-edc49cef-6ed46c19/Singularity
collection: ffineis/nurcs-singularity
---

# ffineis/nurcs-singularity:tensorflow_gpu

```bash
$ singularity pull shub://ffineis/nurcs-singularity:tensorflow_gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:7.5-cudnn5-devel


%post

	# install CUDA samples for testing, other CLI goodies.
	apt-get -y update && apt-get -y upgrade
	apt-get -y --allow-unauthenticated install \
		apt-utils \
		build-essential \
		cmake \
		git \
		gcc \
		locales \
		gfortran \
		libopenblas-dev \
		liblapack-dev \
		libfreetype6-dev \
		libtool \
		libssl-dev \
		libffi-dev \
		wget \
		vim \
		pkg-config \
		python-dev \
		python-pip \
		zlib1g-dev

	apt-get -y --allow-unauthenticated install python-software-properties \
		python-setuptools \
		python-numpy \
		python-scipy \
		python-sympy \
		python-nose \
		python-pandas \

	locale-gen "en_US.UTF-8"
	dpkg-reconfigure locales
	export LANGUAGE="en_US.UTF-8"
	echo 'LANGUAGE="en_US.UTF-8"' >> /etc/default/locale
	echo 'LC_ALL="en_US.UTF-8"' >> /etc/default/locale

	# default mount paths.
	mkdir /software
  
	# Nvidia Library mount paths.
	mkdir /nvlib /nvbin

	# python2 TF/data science package dependencies
	pip install --upgrade --ignore-installed pip numpy six==1.11.0 tornado==4.1
	pip install --ignore-installed cython
	pip install --upgrade --ignore-installed scipy==0.14
	pip install statsmodels
    pip install mock \
		matplotlib \
		sklearn \
		ipython==5.1 \
		mlpy \
		nltk \
		biopython

	# open cv for python2
	sudo apt-get -y install python-opencv
	# install TF v.0.8.0, compatible with CUDA 7.5
	export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.8.0rc0-cp27-none-linux_x86_64.whl
	sudo pip install --upgrade $TF_BINARY_URL


%environment

	#Use bash as default shell
	SHELL=/bin/bash
	
	#Add nvidia driver paths
	PATH="/nvbin:$PATH"
	LD_LIBRARY_PATH="/nvlib:$LD_LIBRARY_PATH"
	
	#Add CUDA paths
	CPATH="/usr/local/cuda/include:$CPATH"
	PATH="/usr/local/cuda/bin:$PATH"
	LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"
	CUDA_HOME="/usr/local/cuda"
	
	export PATH LD_LIBRARY_PATH CPATH CUDA_HOME


%files

	gpu_matmul.py /opt


%test

	python -c 'import tensorflow'

	# ON GPU-ENABLED MACHINE...
	# python -c 'from tensorflow.python.client import device_lib; print(device_lib.list_local_devices())'
	# python /opt/gpu_matmul.py
```

## Collection

 - Name: [ffineis/nurcs-singularity](https://github.com/ffineis/nurcs-singularity)
 - License: None

