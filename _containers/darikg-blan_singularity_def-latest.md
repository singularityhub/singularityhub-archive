---
id: 12802
name: "darikg/blan_singularity_def"
branch: "master"
tag: "latest"
commit: "5ccd6573c2a5ef7da68596a0773b1d83daadd902"
version: "e47d0fc8109f1461a4122ba44b9da872"
build_date: "2020-05-11T03:04:27.207Z"
size_mb: 5630.0
size: 2316533791
sif: "https://datasets.datalad.org/shub/darikg/blan_singularity_def/latest/2020-05-11-5ccd6573-e47d0fc8/e47d0fc8109f1461a4122ba44b9da872.sif"
url: https://datasets.datalad.org/shub/darikg/blan_singularity_def/latest/2020-05-11-5ccd6573-e47d0fc8/
recipe: https://datasets.datalad.org/shub/darikg/blan_singularity_def/latest/2020-05-11-5ccd6573-e47d0fc8/Singularity
collection: darikg/blan_singularity_def
---

# darikg/blan_singularity_def:latest

```bash
$ singularity pull shub://darikg/blan_singularity_def:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:20.04

%post

	#TODO add blender to path somehow
	
    apt -y update
    apt -y install --no-install-recommends xz-utils wget git openmpi-bin mpi mpich blender

	# CONDA -------------------------
	wget -q --no-check-certificate https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
	bash Miniconda3-latest-Linux-x86_64.sh -b -p /conda
	rm Miniconda3-latest-Linux-x86_64.sh
	chmod -R 777 /conda

	# PYTHON LIBS -------------------------
	echo "Installing python libraries"
	/conda/bin/conda create -y -n blan1 python=3.7
	. /conda/etc/profile.d/conda.sh
	conda init
	conda activate blan1
	conda install -y python=3.7
	pip install --no-cache-dir tensorflow==2.2.0rc0 numpy==1.18.3 tensorflow_datasets pytest tables
	conda install -y ipython pandas toolz matplotlib imageio click pyyaml bokeh mpi4py
	
	# To checK:
	# conda install -c conda-forge jupyterlab
	# pip install htcondor
	# conda clean --all -f -y
	
	echo ". /conda/etc/profile.d/conda.sh" >> $SINGULARITY_ENVIRONMENT
	echo "conda activate blan1" >> $SINGULARITY_ENVIRONMENT

	# BLENDER -------------------------
	# Installing blender through apt above was an easy way to get all the dependencies but we want a new version of blender itself
	apt -y remove blender
	wget -q --no-check-certificate https://mirror.clarkson.edu/blender/release/Blender2.82/blender-2.82a-linux64.tar.xz
    tar -xf /blender-2.82a-linux64.tar.xz
    rm /blender-2.82a-linux64.tar.xz
	
	rm -rf /blender-2.82a-linux64/2.82/python/lib/python3.7/site-packages/numpy
	
	/blender-2.82a-linux64/2.82/python/bin/python3.7m -m ensurepip
	/blender-2.82a-linux64/2.82/python/bin/pip3 install --upgrade pip
	/blender-2.82a-linux64/2.82/python/bin/pip3 install pyyaml tblib
	apt clean
	chmod -R 777 /blender-2.82a-linux64
	echo "PATH=/blender-2.82a-linux64:\$PATH" >> $SINGULARITY_ENVIRONMENT
	
%environment
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
	
%labels
    Author DarikGamble
```

## Collection

 - Name: [darikg/blan_singularity_def](https://github.com/darikg/blan_singularity_def)
 - License: None

