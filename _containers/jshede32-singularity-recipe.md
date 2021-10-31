---
id: 8000
name: "jshede32/singularity"
branch: "master"
tag: "recipe"
commit: "28fc061804793d12f81a1e4e765f9470aae323d1"
version: "0f644c271733257647dba9f234ea44e0"
build_date: "2019-04-02T20:23:25.489Z"
size_mb: 2957
size: 1431052319
sif: "https://datasets.datalad.org/shub/jshede32/singularity/recipe/2019-04-02-28fc0618-0f644c27/0f644c271733257647dba9f234ea44e0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jshede32/singularity/recipe/2019-04-02-28fc0618-0f644c27/
recipe: https://datasets.datalad.org/shub/jshede32/singularity/recipe/2019-04-02-28fc0618-0f644c27/Singularity
collection: jshede32/singularity
---

# jshede32/singularity:recipe

```bash
$ singularity pull shub://jshede32/singularity:recipe
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: valian/docker-python-opencv-ffmpeg:cuda-py3


%post
	su
	apt-get update
	exit
	sudo apt-get install vim
	sudo apt-get install wget
	pip3 install tensorflow-gpu
	pip install tensorflow-gpu
	pip install geopy
	pip install PIL
	pip install numpy
	pip install scilearn
```

## Collection

 - Name: [jshede32/singularity](https://github.com/jshede32/singularity)
 - License: None

