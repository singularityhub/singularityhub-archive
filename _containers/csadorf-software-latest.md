---
id: 2940
name: "csadorf/software"
branch: "master"
tag: "latest"
commit: "3d509362e83831a02bf49a65666d2013eaf4bb7d"
version: "3355a97ae955d273bce946057686dd27"
build_date: "2019-01-08T21:45:14.400Z"
size_mb: 3592
size: 1663299615
sif: "https://datasets.datalad.org/shub/csadorf/software/latest/2019-01-08-3d509362-3355a97a/3355a97ae955d273bce946057686dd27.simg"
url: https://datasets.datalad.org/shub/csadorf/software/latest/2019-01-08-3d509362-3355a97a/
recipe: https://datasets.datalad.org/shub/csadorf/software/latest/2019-01-08-3d509362-3355a97a/Singularity
collection: csadorf/software
---

# csadorf/software:latest

```bash
$ singularity pull shub://csadorf/software:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: glotzerlab/software:latest

%labels
	MAINTAINER csadorf

%post
	ln -s /usr/bin/python3 /usr/bin/python
	apt-get update && apt-get install -y --no-install-recommends \
		libhdf5-dev \
		graphviz \
		locales \
		python3-dev \
		python3-pip \
		python3-scipy \
		python3-matplotlib \
		python3-mpi4py
	python3 -m pip install --upgrade pip
	python3 -m pip install tensorflow
	python3 -m pip install keras
	python3 -m pip install Pillow scikit-learn pandas

%environment
	export LC_ALL=C
	export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-8.0/lib64
```

## Collection

 - Name: [csadorf/software](https://github.com/csadorf/software)
 - License: [MIT License](https://api.github.com/licenses/mit)

