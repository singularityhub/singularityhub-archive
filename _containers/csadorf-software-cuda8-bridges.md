---
id: 2829
name: "csadorf/software"
branch: "master"
tag: "cuda8-bridges"
commit: "3d509362e83831a02bf49a65666d2013eaf4bb7d"
version: "1098c8eea1157e7b6a79180060a79c50"
build_date: "2019-01-08T23:44:45.545Z"
size_mb: 3960
size: 1777934367
sif: "https://datasets.datalad.org/shub/csadorf/software/cuda8-bridges/2019-01-08-3d509362-1098c8ee/1098c8eea1157e7b6a79180060a79c50.simg"
url: https://datasets.datalad.org/shub/csadorf/software/cuda8-bridges/2019-01-08-3d509362-1098c8ee/
recipe: https://datasets.datalad.org/shub/csadorf/software/cuda8-bridges/2019-01-08-3d509362-1098c8ee/Singularity
collection: csadorf/software
---

# csadorf/software:cuda8-bridges

```bash
$ singularity pull shub://csadorf/software:cuda8-bridges
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: glotzerlab/software:cuda8-bridges

%labels
	MAINTAINER csadorf

%post
	ln -s /usr/bin/python3 /usr/bin/python
	python3 -m pip install --upgrade pip
	python3 -m pip install --upgrade \
		Click==7.0 \
		Keras==2.2.4 \
		rmsd==1.3.0 \
		tensorflow==1.12.0 \
		umap-learn==0.3.6

%environment
	export LC_ALL=C
```

## Collection

 - Name: [csadorf/software](https://github.com/csadorf/software)
 - License: [MIT License](https://api.github.com/licenses/mit)

