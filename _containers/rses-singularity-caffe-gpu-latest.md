---
id: 1687
name: "rses-singularity/caffe-gpu"
branch: "master"
tag: "latest"
commit: "80194c4f6b024fb55a00956a088a00e9b5005679"
version: "216b26df4b421d259975f6d1e7fac399"
build_date: "2019-08-10T23:25:10.616Z"
size_mb: 3364
size: 1691676703
sif: "https://datasets.datalad.org/shub/rses-singularity/caffe-gpu/latest/2019-08-10-80194c4f-216b26df/216b26df4b421d259975f6d1e7fac399.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rses-singularity/caffe-gpu/latest/2019-08-10-80194c4f-216b26df/
recipe: https://datasets.datalad.org/shub/rses-singularity/caffe-gpu/latest/2019-08-10-80194c4f-216b26df/Singularity
collection: rses-singularity/caffe-gpu
---

# rses-singularity/caffe-gpu:latest

```bash
$ singularity pull shub://rses-singularity/caffe-gpu:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bvlc/caffe:gpu

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

 - Name: [rses-singularity/caffe-gpu](https://github.com/rses-singularity/caffe-gpu)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

