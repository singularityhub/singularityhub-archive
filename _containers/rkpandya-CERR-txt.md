---
id: 9057
name: "rkpandya/CERR"
branch: "master"
tag: "txt"
commit: "4533b4c9d429b752338a29bbc4ee5253272aa8ad"
version: "dd47fe128f7e0818d43ca0a50a74020d"
build_date: "2020-11-20T09:39:22.220Z"
size_mb: 5274
size: 2894127135
sif: "https://datasets.datalad.org/shub/rkpandya/CERR/txt/2020-11-20-4533b4c9-dd47fe12/dd47fe128f7e0818d43ca0a50a74020d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rkpandya/CERR/txt/2020-11-20-4533b4c9-dd47fe12/
recipe: https://datasets.datalad.org/shub/rkpandya/CERR/txt/2020-11-20-4533b4c9-dd47fe12/Singularity
collection: rkpandya/CERR
---

# rkpandya/CERR:txt

```bash
$ singularity pull shub://rkpandya/CERR:txt
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

  	#Update and get required packages
  	apt-get update
 	apt-get install -y python3
  	apt-get install -y wget git vim

	#install python3 in python virtualenv
  	apt update
  	apt install -y virtualenv
  	virtualenv -p python3 env
  	ls env/lib
  	ls -l `which sh`
  	. env/bin/activate

  	apt install -y python3-pip
  	python --version
  	pip3 --version
  
	pip3 install Pillow 

  	#Install Tensorflow  	
  	pip3 install --no-cache-dir tensorflow-gpu==1.12.0

  	# Upgrade all packages to their latest versions
  	apt-get -y update && apt-get -y upgrade

  	# Install expect to automate responses for interactive build questions
  	apt-get -y install expect
  	 
  	apt update
  	apt-get clean

	apt update && apt install -y libsm6 libxext6
  	apt-get install -y libxrender-dev
  	
  	pip3 install numpy
  	pip3 install scikit-image
  	pip3 install opencv-python
  	pip3 install protobuf
  	
	apt-get update 
	apt-get install -y libgtk2.0-dev

	pip install --upgrade pip
  		
	apt-get install -y python-imaging

  	apt update
  	
  	mkdir /software
  	cd /software
  	git clone https://github.com/cerr/CERR.git
  	wget https://github.com/cerr/aimodels/raw/master/PROSTATE_DEEPLABV3_1.0.pb
  


%runscript
	#Executes with the singularity run command	
	
	. /env/bin/activate	
	
	python /software/CERR/CERR_core/Contouring/models/mr_prostate_DeepLab/run_inference_clinical_3D.py arg1=$1 arg2=$2
	pkill -f /software/CERR/CERR_core/Contouring/models/mr_prostate_DeepLab/run_inference_clinical_3D.py	

%test
	#Test that script is a success

	#Load environment variables
	#. /environment

	#Test tensorflow install
	#python -c "import tensorflow"
```

## Collection

 - Name: [rkpandya/CERR](https://github.com/rkpandya/CERR)
 - License: [GNU Lesser General Public License v2.1](https://api.github.com/licenses/lgpl-2.1)

