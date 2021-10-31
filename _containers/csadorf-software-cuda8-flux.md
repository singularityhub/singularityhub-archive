---
id: 2831
name: "csadorf/software"
branch: "master"
tag: "cuda8-flux"
commit: "3d509362e83831a02bf49a65666d2013eaf4bb7d"
version: "ab5bc39a3be1a3df0e9854e8e035d5b9"
build_date: "2019-01-08T21:45:14.350Z"
size_mb: 4371
size: 2012160031
sif: "https://datasets.datalad.org/shub/csadorf/software/cuda8-flux/2019-01-08-3d509362-ab5bc39a/ab5bc39a3be1a3df0e9854e8e035d5b9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/csadorf/software/cuda8-flux/2019-01-08-3d509362-ab5bc39a/
recipe: https://datasets.datalad.org/shub/csadorf/software/cuda8-flux/2019-01-08-3d509362-ab5bc39a/Singularity
collection: csadorf/software
---

# csadorf/software:cuda8-flux

```bash
$ singularity pull shub://csadorf/software:cuda8-flux
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: glotzerlab/software:cuda8-flux

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
	python3 -m pip install tensorflow-gpu
	python3 -m pip install keras
	python3 -m pip install Pillow scikit-learn pandas

%environment
	export LC_ALL=C
```

## Collection

 - Name: [csadorf/software](https://github.com/csadorf/software)
 - License: [MIT License](https://api.github.com/licenses/mit)

