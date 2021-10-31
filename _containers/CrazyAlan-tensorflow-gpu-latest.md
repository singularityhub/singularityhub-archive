---
id: 547
name: "CrazyAlan/tensorflow-gpu"
branch: "master"
tag: "latest"
commit: "437f3d0dec4044b4887cba7e6da1b6b4e898e2ba"
version: "66b0d129437f8a8ddf65451a40a3004e"
build_date: "2019-10-12T15:21:26.058Z"
size_mb: 5030
size: 2516373535
sif: "https://datasets.datalad.org/shub/CrazyAlan/tensorflow-gpu/latest/2019-10-12-437f3d0d-66b0d129/66b0d129437f8a8ddf65451a40a3004e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CrazyAlan/tensorflow-gpu/latest/2019-10-12-437f3d0d-66b0d129/
recipe: https://datasets.datalad.org/shub/CrazyAlan/tensorflow-gpu/latest/2019-10-12-437f3d0d-66b0d129/Singularity
collection: CrazyAlan/tensorflow-gpu
---

# CrazyAlan/tensorflow-gpu:latest

```bash
$ singularity pull shub://CrazyAlan/tensorflow-gpu:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04

%environment

	#Environment variables

	#Use bash as default shell
	SHELL=/bin/bash

	#Add nvidia driver paths
	PATH="/nvbin:$PATH"
	LD_LIBRARY_PATH="/nvlib;$LD_LIBRARY_PATH"

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

	#Nvidia Library mount paths
	mkdir /nvlib /nvbin

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


  #Install Tensorflow
  TF_PYTHON_URL="https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.3.0-cp35-cp35m-linux_x86_64.whl"
  pip install --ignore-installed --upgrade $TF_PYTHON_URL

	#Install Keras
	pip install keras

%runscript
	#Executes with the singularity run command
	#delete this section to use existing docker ENTRYPOINT command


%test
	#Test that script is a success
```

## Collection

 - Name: [CrazyAlan/tensorflow-gpu](https://github.com/CrazyAlan/tensorflow-gpu)
 - License: None

