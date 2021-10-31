---
id: 546
name: "CrazyAlan99/tensorflow-gpu"
branch: "master"
tag: "latest"
commit: "437f3d0dec4044b4887cba7e6da1b6b4e898e2ba"
version: "2bbe40397bbe3dc7bc3fe04b6edfe87c"
build_date: "2021-04-16T07:33:13.318Z"
size_mb: 5031
size: 2516373535
sif: "https://datasets.datalad.org/shub/CrazyAlan99/tensorflow-gpu/latest/2021-04-16-437f3d0d-2bbe4039/2bbe40397bbe3dc7bc3fe04b6edfe87c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CrazyAlan99/tensorflow-gpu/latest/2021-04-16-437f3d0d-2bbe4039/
recipe: https://datasets.datalad.org/shub/CrazyAlan99/tensorflow-gpu/latest/2021-04-16-437f3d0d-2bbe4039/Singularity
collection: CrazyAlan99/tensorflow-gpu
---

# CrazyAlan99/tensorflow-gpu:latest

```bash
$ singularity pull shub://CrazyAlan99/tensorflow-gpu:latest
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

 - Name: [CrazyAlan99/tensorflow-gpu](https://github.com/CrazyAlan99/tensorflow-gpu)
 - License: None

