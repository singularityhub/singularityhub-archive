---
id: 2830
name: "csadorf/software"
branch: "master"
tag: "cuda8-comet"
commit: "3d509362e83831a02bf49a65666d2013eaf4bb7d"
version: "7f94264c5154b6b5476816e52b6be1c6"
build_date: "2019-01-09T08:35:39.492Z"
size_mb: 3891
size: 1759281183
sif: "https://datasets.datalad.org/shub/csadorf/software/cuda8-comet/2019-01-09-3d509362-7f94264c/7f94264c5154b6b5476816e52b6be1c6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/csadorf/software/cuda8-comet/2019-01-09-3d509362-7f94264c/
recipe: https://datasets.datalad.org/shub/csadorf/software/cuda8-comet/2019-01-09-3d509362-7f94264c/Singularity
collection: csadorf/software
---

# csadorf/software:cuda8-comet

```bash
$ singularity pull shub://csadorf/software:cuda8-comet
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: glotzerlab/software:cuda8-comet

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

