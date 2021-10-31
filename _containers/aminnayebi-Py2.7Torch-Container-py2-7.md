---
id: 6064
name: "aminnayebi/Py2.7Torch-Container"
branch: "master"
tag: "py2-7"
commit: "11c2eb4f9ce7695699fbec79582d6e39a08a5db1"
version: "cd1e2a6d1a897c665acd5ef3db19f9d1"
build_date: "2019-01-14T04:37:51.995Z"
size_mb: 5720
size: 2855960607
sif: "https://datasets.datalad.org/shub/aminnayebi/Py2.7Torch-Container/py2-7/2019-01-14-11c2eb4f-cd1e2a6d/cd1e2a6d1a897c665acd5ef3db19f9d1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/aminnayebi/Py2.7Torch-Container/py2-7/2019-01-14-11c2eb4f-cd1e2a6d/
recipe: https://datasets.datalad.org/shub/aminnayebi/Py2.7Torch-Container/py2-7/2019-01-14-11c2eb4f-cd1e2a6d/Singularity
collection: aminnayebi/Py2.7Torch-Container
---

# aminnayebi/Py2.7Torch-Container:py2-7

```bash
$ singularity pull shub://aminnayebi/Py2.7Torch-Container:py2-7
```

## Singularity Recipe

```singularity
Bootstrap: docker
	From: vanessa/pytorch-dev:py2.7

%labels
	MAINTAINER aminnayebi


%runscript
	echo "This is running!"

%post
	chmod 777 /opt/conda
```

## Collection

 - Name: [aminnayebi/Py2.7Torch-Container](https://github.com/aminnayebi/Py2.7Torch-Container)
 - License: None

