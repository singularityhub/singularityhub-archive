---
id: 3123
name: "akashsingularityucr/caffe-cpu"
branch: "master"
tag: "latest"
commit: "3c2683ab9709c64926471071905b03c8b7886187"
version: "962537cfc4ce7848e8d9b00b249c13a5"
build_date: "2018-06-09T14:17:50.105Z"
size_mb: 1653
size: 606519327
sif: "https://datasets.datalad.org/shub/akashsingularityucr/caffe-cpu/latest/2018-06-09-3c2683ab-962537cf/962537cfc4ce7848e8d9b00b249c13a5.simg"
url: https://datasets.datalad.org/shub/akashsingularityucr/caffe-cpu/latest/2018-06-09-3c2683ab-962537cf/
recipe: https://datasets.datalad.org/shub/akashsingularityucr/caffe-cpu/latest/2018-06-09-3c2683ab-962537cf/Singularity
collection: akashsingularityucr/caffe-cpu
---

# akashsingularityucr/caffe-cpu:latest

```bash
$ singularity pull shub://akashsingularityucr/caffe-cpu:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bvlc/caffe:cpu

%environment

	#Environment variables

	#Use bash as default shell
	SHELL=/bin/bash


	#Add CUDA paths
	CPATH="/usr/local/cuda/include:$CPATH"
	PATH="/usr/local/cuda/bin:$PATH"
	LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"
	CUDA_HOME="/usr/local/cuda"

	#Add Caffe paths
	CAFFE_ROOT="/opt/caffe"
	PYCAFFE_ROOT="$CAFFE_ROOT/python"
	PYTHONPATH="$PYCAFFE_ROOT:$PYTHONPATH"
	PATH="$CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH"

	export PATH LD_LIBRARY_PATH CPATH CUDA_HOME CAFFE_ROOT PYCAFFE_ROOT PYTHONPATH

%setup
	#Runs on host
	#The path to the image is $SINGULARITY_ROOTFS


%post
	#Post setup script

	#Load environment variables
	. /environment

	#Default mount paths
	mkdir /scratch /data /shared /fastdata



%runscript
	#Executes with the singularity run command
	#delete this section to use existing docker ENTRYPOINT command





%test
	#Test that script is a success
```

## Collection

 - Name: [akashsingularityucr/caffe-cpu](https://github.com/akashsingularityucr/caffe-cpu)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

