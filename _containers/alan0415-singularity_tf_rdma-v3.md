---
id: 8518
name: "alan0415/singularity_tf_rdma"
branch: "master"
tag: "v3"
commit: "cc9a99231ae2f91c9b73261e7688ef8d346aa6bc"
version: "f24228a72ef3b9b50c0bee5447b0e555"
build_date: "2019-04-20T16:49:54.133Z"
size_mb: 3153
size: 1870266399
sif: "https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v3/2019-04-20-cc9a9923-f24228a7/f24228a72ef3b9b50c0bee5447b0e555.simg"
url: https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v3/2019-04-20-cc9a9923-f24228a7/
recipe: https://datasets.datalad.org/shub/alan0415/singularity_tf_rdma/v3/2019-04-20-cc9a9923-f24228a7/Singularity
collection: alan0415/singularity_tf_rdma
---

# alan0415/singularity_tf_rdma:v3

```bash
$ singularity pull shub://alan0415/singularity_tf_rdma:v3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04

%environment
	SHELL=/bin/bash
	
	#Add nvidia driver paths
	PATH="/nvbin:$PATH"
	LD_LIBRARY_PATH="/nvlib;$LD_LIBRARY_PATH"

	#Add CUDA paths
	CPATH="/usr/local/cuda/include:$CPATH"
	PATH="/usr/local/cuda/bin:$PATH"
	LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"
	CUDA_HOME="/usr/local/cuda"

	#Add Bazel Path
	export PATH=/root/bazel/bin:$PATH
	

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
  apt-get install -y build-essential
  apt-get install -y python3

#Install Bazel
   cd /home
   wget https://github.com/bazelbuild/bazel/releases/download/0.24.0/bazel-0.24.0-installer-linux-x86_64.sh
#   chmod 777 bazel-0.24.0-installer-linux-x86_64.sh
#   mkdir -p /home/spark/xs/tf/bazel/bin
#   ./bazel-0.24.0-installer-linux-x86_64.sh --prefix=/home/spark/xs/tf/bazel \
#                                           --bin=/home/spark/xs/tf/bazel/bin \ 
#                                           --base=/home/spark/xs/tf/bazel/.bazel \
        
#   source /root/bazel/lib/bazel/bin/bazel-complete.bash

#Install Tensorflow

#sudo add-apt-repository ppa:deadsnakes/ppa
#sudo apt update
#sudo apt install python3.6
```

## Collection

 - Name: [alan0415/singularity_tf_rdma](https://github.com/alan0415/singularity_tf_rdma)
 - License: None

