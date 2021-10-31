---
id: 1668
name: "rses-singularity/tensorflow-gpu"
branch: "master"
tag: "latest"
commit: "cdaba37f6bcf1faac840ab0f267c6ec4536e6ae1"
version: "a1bcef5d31802d85f46112abee41b09d"
build_date: "2021-04-08T13:58:19.791Z"
size_mb: 6095
size: 3052335135
sif: "https://datasets.datalad.org/shub/rses-singularity/tensorflow-gpu/latest/2021-04-08-cdaba37f-a1bcef5d/a1bcef5d31802d85f46112abee41b09d.simg"
url: https://datasets.datalad.org/shub/rses-singularity/tensorflow-gpu/latest/2021-04-08-cdaba37f-a1bcef5d/
recipe: https://datasets.datalad.org/shub/rses-singularity/tensorflow-gpu/latest/2021-04-08-cdaba37f-a1bcef5d/Singularity
collection: rses-singularity/tensorflow-gpu
---

# rses-singularity/tensorflow-gpu:latest

```bash
$ singularity pull shub://rses-singularity/tensorflow-gpu:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

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

	pip install -U pip

  #Install Tensorflow
  TF_PYTHON_URL="https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.9.0-cp35-cp35m-linux_x86_64.whl"
  pip install --ignore-installed --upgrade $TF_PYTHON_URL

	#Install Keras
	pip install keras

%runscript
	#Executes with the singularity run command
	#delete this section to use existing docker ENTRYPOINT command


%test
	#Test that script is a success

	#Load environment variables
	#. /environment

	#Test tensorflow install
	#python -c "import tensorflow"
```

## Collection

 - Name: [rses-singularity/tensorflow-gpu](https://github.com/rses-singularity/tensorflow-gpu)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

