---
id: 6216
name: "aminnayebi/Py2.7Torch-Container"
branch: "master"
tag: "py2-7v1"
commit: "d2079ecc52793cce7668ac76d626a20470325892"
version: "7cad790287bcf55e10487a4ebfc70e68"
build_date: "2019-01-14T04:37:51.989Z"
size_mb: 5720
size: 2855960607
sif: "https://datasets.datalad.org/shub/aminnayebi/Py2.7Torch-Container/py2-7v1/2019-01-14-d2079ecc-7cad7902/7cad790287bcf55e10487a4ebfc70e68.simg"
url: https://datasets.datalad.org/shub/aminnayebi/Py2.7Torch-Container/py2-7v1/2019-01-14-d2079ecc-7cad7902/
recipe: https://datasets.datalad.org/shub/aminnayebi/Py2.7Torch-Container/py2-7v1/2019-01-14-d2079ecc-7cad7902/Singularity
collection: aminnayebi/Py2.7Torch-Container
---

# aminnayebi/Py2.7Torch-Container:py2-7v1

```bash
$ singularity pull shub://aminnayebi/Py2.7Torch-Container:py2-7v1
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
	chmod -R 777 /opt/conda
```

## Collection

 - Name: [aminnayebi/Py2.7Torch-Container](https://github.com/aminnayebi/Py2.7Torch-Container)
 - License: None

