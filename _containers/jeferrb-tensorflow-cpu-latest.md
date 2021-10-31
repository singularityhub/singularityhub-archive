---
id: 2811
name: "jeferrb/tensorflow-cpu"
branch: "master"
tag: "latest"
commit: "bdeb255fe027a047f812fc6ea2a643dd600d0743"
version: "539c4b4cfaeddecd5f298b3eb84fd356"
build_date: "2018-05-18T02:49:52.939Z"
size_mb: 6370
size: 3060084767
sif: "https://datasets.datalad.org/shub/jeferrb/tensorflow-cpu/latest/2018-05-18-bdeb255f-539c4b4c/539c4b4cfaeddecd5f298b3eb84fd356.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jeferrb/tensorflow-cpu/latest/2018-05-18-bdeb255f-539c4b4c/
recipe: https://datasets.datalad.org/shub/jeferrb/tensorflow-cpu/latest/2018-05-18-bdeb255f-539c4b4c/Singularity
collection: jeferrb/tensorflow-cpu
---

# jeferrb/tensorflow-cpu:latest

```bash
$ singularity pull shub://jeferrb/tensorflow-cpu:latest
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
  apt-get install -y wget git vim python python3

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
	pip install --upgrade pip
	pip install --upgrade keras
	pip install --upgrade gensim
	pip install --upgrade dask
	pip install https://pypi.python.org/packages/source/n/nltk/nltk-3.2.1.tar.gz
	conda install nomkl numpy scipy scikit-learn numexpr matplotlib ipython jupyter pandas sympy nose
	conda remove mkl mkl-service

%runscript
	#Executes with the singularity run command
	#delete this section to use existing docker ENTRYPOINT command


%test
	#Test that script is a success

	#Load environment variables
	. /environment

	#Test tensorflow install
	python -c "import tensorflow"
	python -c "import gensim"
```

## Collection

 - Name: [jeferrb/tensorflow-cpu](https://github.com/jeferrb/tensorflow-cpu)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

