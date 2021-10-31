---
id: 4204
name: "willianmh/singularity"
branch: "master"
tag: "bak"
commit: "2b1942b828449ad52a0d30f501e91a50e9da59af"
version: "6c9b22ff125dea9616ed0439956dd9ee"
build_date: "2018-08-28T03:21:34.752Z"
size_mb: 9523
size: 4831424543
sif: "https://datasets.datalad.org/shub/willianmh/singularity/bak/2018-08-28-2b1942b8-6c9b22ff/6c9b22ff125dea9616ed0439956dd9ee.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/willianmh/singularity/bak/2018-08-28-2b1942b8-6c9b22ff/
recipe: https://datasets.datalad.org/shub/willianmh/singularity/bak/2018-08-28-2b1942b8-6c9b22ff/Singularity
collection: willianmh/singularity
---

# willianmh/singularity:bak

```bash
$ singularity pull shub://willianmh/singularity:bak
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.2-cudnn7-devel-ubuntu16.04

%environment

	#Environment variables

	#Use bash as default shell
	SHELL=/bin/bash

	#Add CUDA paths
	CPATH="/usr/local/cuda/include:$CPATH"
	PATH="/usr/local/cuda/bin:$PATH"
	LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"
	CUDA_HOME="/usr/local/cuda"

	#Add Anaconda path
	PATH="/usr/local/anaconda3-4.2.0/bin:$PATH"

	export PATH LD_LIBRARY_PATH CPATH CUDA_HOME

%setup
	#Runs on host
	#The path to the image is $SINGULARITY_ROOTFS



%post
	#Post setup script

	#Load environment variables
	. /environment

	#Default mount paths
	mkdir /scratch /data /shared /fastdata


  #Updating and getting required packages
  apt-get update
  apt-get install -y wget git vim tmux tree htop
	apt-get install -y libtool m4 automake
	apt-get install -y unrar unzip


	# Utility and support packages
  apt-get install -y aptitude build-essential cmake gcc g++ gfortran git \
      pkg-config python-pip python-dev software-properties-common


	# More utilities
  apt-get install -y graphviz libatlas-dev libfreetype6 libfreetype6-dev \
      libgraphviz-dev liblapack-dev swig libxft-dev libxml2-dev \
      libxslt-dev zlib1g-dev

  # Python modules from system package manager
  apt-get install -y python-numpy python-scipy python-nose python-h5py \
      python-skimage python-matplotlib python-pandas python-sklearn \
      python-sympy python-virtualenv

  #Creates a build directory
  mkdir build
  cd build

  #Download and install Anaconda
  CONDA_INSTALL_PATH="/usr/local/anaconda3-4.2.0"
  wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
  chmod +x Anaconda3-4.2.0-Linux-x86_64.sh
  ./Anaconda3-4.2.0-Linux-x86_64.sh -b -p $CONDA_INSTALL_PATH


  #Install Tensorflow
  pip install tensorflow-gpu

	#Install Keras
	pip install keras


	# wget "http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/12998/parallel_studio_xe_2018_update3_cluster_edition.tgz"
	#
	# mkdir /tmp/psxe_staging_area
	# tar -xvzf parallel_studio_xe_2018_update3_cluster_edition.tgz -C /tmp/psxe_staging_area
	#
	# cd /tmp/psxe_staging_area/parallel_studio_xe_2018_update3_cluster_edition
	#
	# sed -i 's/decline/accept' silent.cfg
	#
	# ./install.sh --silent=silent.cfg

%runscript
	#Executes with the singularity run command
	#delete this section to use existing docker ENTRYPOINT command


%test
	#Test that script is a success
```

## Collection

 - Name: [willianmh/singularity](https://github.com/willianmh/singularity)
 - License: None

