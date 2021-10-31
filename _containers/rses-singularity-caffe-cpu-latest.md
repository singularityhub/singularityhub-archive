---
id: 1686
name: "rses-singularity/caffe-cpu"
branch: "master"
tag: "latest"
commit: "3c2683ab9709c64926471071905b03c8b7886187"
version: "c74103aef8ab673215b42ae7776143b2"
build_date: "2018-02-09T16:52:41.763Z"
size_mb: 1697
size: 621101087
sif: "https://datasets.datalad.org/shub/rses-singularity/caffe-cpu/latest/2018-02-09-3c2683ab-c74103ae/c74103aef8ab673215b42ae7776143b2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rses-singularity/caffe-cpu/latest/2018-02-09-3c2683ab-c74103ae/
recipe: https://datasets.datalad.org/shub/rses-singularity/caffe-cpu/latest/2018-02-09-3c2683ab-c74103ae/Singularity
collection: rses-singularity/caffe-cpu
---

# rses-singularity/caffe-cpu:latest

```bash
$ singularity pull shub://rses-singularity/caffe-cpu:latest
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

 - Name: [rses-singularity/caffe-cpu](https://github.com/rses-singularity/caffe-cpu)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

