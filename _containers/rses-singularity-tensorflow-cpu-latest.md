---
id: 1667
name: "rses-singularity/tensorflow-cpu"
branch: "master"
tag: "latest"
commit: "9dc77245fae00802b185542795efa3baa41fe694"
version: "f61a6a1f36d12b6008ed59b884741d21"
build_date: "2019-08-06T20:56:41.390Z"
size_mb: 5478
size: 2659373087
sif: "https://datasets.datalad.org/shub/rses-singularity/tensorflow-cpu/latest/2019-08-06-9dc77245-f61a6a1f/f61a6a1f36d12b6008ed59b884741d21.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rses-singularity/tensorflow-cpu/latest/2019-08-06-9dc77245-f61a6a1f/
recipe: https://datasets.datalad.org/shub/rses-singularity/tensorflow-cpu/latest/2019-08-06-9dc77245-f61a6a1f/Singularity
collection: rses-singularity/tensorflow-cpu
---

# rses-singularity/tensorflow-cpu:latest

```bash
$ singularity pull shub://rses-singularity/tensorflow-cpu:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.1-cudnn7-devel-ubuntu16.04

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
  apt-get install -y wget git vim

  #Creates a build directory
  mkdir build
  cd build

  #Download and install Anaconda
  CONDA_INSTALL_PATH="/usr/local/anaconda3-4.2.0"
  wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
  chmod +x Anaconda3-4.2.0-Linux-x86_64.sh
  ./Anaconda3-4.2.0-Linux-x86_64.sh -b -p $CONDA_INSTALL_PATH


  #Install Tensorflow CPU
  pip install tensorflow

	#Install Keras
	pip install keras

%runscript
	#Executes with the singularity run command
	#delete this section to use existing docker ENTRYPOINT command


%test
	#Test that script is a success

	#Load environment variables
	. /environment

	#Test tensorflow install
	python -c "import tensorflow"
```

## Collection

 - Name: [rses-singularity/tensorflow-cpu](https://github.com/rses-singularity/tensorflow-cpu)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

