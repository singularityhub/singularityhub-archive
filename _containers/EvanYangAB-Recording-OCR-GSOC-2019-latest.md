---
id: 9608
name: "EvanYangAB/Recording-OCR-GSOC-2019"
branch: "master"
tag: "latest"
commit: "6fc98f1970cb72e1df9958fd874852b2d7fdb47a"
version: "095cc0302de2cd9295fd30144e77cf27"
build_date: "2019-08-07T11:02:16.145Z"
size_mb: 6393
size: 3183173663
sif: "https://datasets.datalad.org/shub/EvanYangAB/Recording-OCR-GSOC-2019/latest/2019-08-07-6fc98f19-095cc030/095cc0302de2cd9295fd30144e77cf27.simg"
url: https://datasets.datalad.org/shub/EvanYangAB/Recording-OCR-GSOC-2019/latest/2019-08-07-6fc98f19-095cc030/
recipe: https://datasets.datalad.org/shub/EvanYangAB/Recording-OCR-GSOC-2019/latest/2019-08-07-6fc98f19-095cc030/Singularity
collection: EvanYangAB/Recording-OCR-GSOC-2019
---

# EvanYangAB/Recording-OCR-GSOC-2019:latest

```bash
$ singularity pull shub://EvanYangAB/Recording-OCR-GSOC-2019:latest
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
  apt-get install -y libsm6 libxext6 libxrender-dev

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
	pip install scipy
	pip install Pillow
	pip install cython
	pip install matplotlib
	pip install scikit-image
	pip install opencv-python
	pip install h5py
	pip install imgaug
	pip install IPython[all]
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

 - Name: [EvanYangAB/Recording-OCR-GSOC-2019](https://github.com/EvanYangAB/Recording-OCR-GSOC-2019)
 - License: None

