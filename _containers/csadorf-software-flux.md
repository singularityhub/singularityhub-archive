---
id: 3209
name: "csadorf/software"
branch: "master"
tag: "flux"
commit: "3d509362e83831a02bf49a65666d2013eaf4bb7d"
version: "896eeff75bad293972a829540ecedc73"
build_date: "2019-01-08T21:45:14.375Z"
size_mb: 3841
size: 1738072095
sif: "https://datasets.datalad.org/shub/csadorf/software/flux/2019-01-08-3d509362-896eeff7/896eeff75bad293972a829540ecedc73.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/csadorf/software/flux/2019-01-08-3d509362-896eeff7/
recipe: https://datasets.datalad.org/shub/csadorf/software/flux/2019-01-08-3d509362-896eeff7/Singularity
collection: csadorf/software
---

# csadorf/software:flux

```bash
$ singularity pull shub://csadorf/software:flux
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: glotzerlab/software:flux

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
	python3 -m pip install Pillow
	python3 -m pip install scikit-learn
	python3 -m pip install pandas

%environment
	export LC_ALL=C
```

## Collection

 - Name: [csadorf/software](https://github.com/csadorf/software)
 - License: [MIT License](https://api.github.com/licenses/mit)

