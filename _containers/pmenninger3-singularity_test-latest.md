---
id: 696
name: "pmenninger3/singularity_test"
branch: "master"
tag: "latest"
commit: "0e03da76ff9a714f9eabeab42ecc9a8efe78ac7a"
version: "1ceba61331a138c15082458a93d7b7cb"
build_date: "2017-11-28T19:11:34.528Z"
size_mb: 1388
size: 527417375
sif: "https://datasets.datalad.org/shub/pmenninger3/singularity_test/latest/2017-11-28-0e03da76-1ceba613/1ceba61331a138c15082458a93d7b7cb.simg"
url: https://datasets.datalad.org/shub/pmenninger3/singularity_test/latest/2017-11-28-0e03da76-1ceba613/
recipe: https://datasets.datalad.org/shub/pmenninger3/singularity_test/latest/2017-11-28-0e03da76-1ceba613/Singularity
collection: pmenninger3/singularity_test
---

# pmenninger3/singularity_test:latest

```bash
$ singularity pull shub://pmenninger3/singularity_test:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%runscript

	echo "Hopefully this works!"

%post

	echo "Installing git"
	apt-get update
	apt-get install -y git

	echo "Installing python"
	apt-get install -y software-properties-common python-software-properties
	add-apt-repository ppa:fkrull/deadsnakes
	apt-get update
	apt-get install -y python2.7

	echo "Installing pip and virtualenv"
	apt-get install -y python-pip python-dev build-essential
	pip install --upgrade pip
	pip install --upgrade virtualenv
	
	echo "Installing python-tk"
	apt-get install -y python-tk

	echo "Installing TensorFlow"
	pip install tensorflow

	echo "Installing Keras"
	pip install keras

	echo "Installing matplotlib, sklearn, h5py"
	pip install matplotlib
	pip install sklearn
	pip install h5py
```

## Collection

 - Name: [pmenninger3/singularity_test](https://github.com/pmenninger3/singularity_test)
 - License: None

