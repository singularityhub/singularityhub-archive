---
id: 7705
name: "aminnayebi/ContainerMOE"
branch: "master"
tag: "ubuntumoe-xenial"
commit: "48dff621082253c2dd6d230d3a8759372c1f44d4"
version: "3850929b4ba6435dd62519400acea875"
build_date: "2019-03-12T08:04:35.663Z"
size_mb: 315
size: 124039199
sif: "https://datasets.datalad.org/shub/aminnayebi/ContainerMOE/ubuntumoe-xenial/2019-03-12-48dff621-3850929b/3850929b4ba6435dd62519400acea875.simg"
url: https://datasets.datalad.org/shub/aminnayebi/ContainerMOE/ubuntumoe-xenial/2019-03-12-48dff621-3850929b/
recipe: https://datasets.datalad.org/shub/aminnayebi/ContainerMOE/ubuntumoe-xenial/2019-03-12-48dff621-3850929b/Singularity
collection: aminnayebi/ContainerMOE
---

# aminnayebi/ContainerMOE:ubuntumoe-xenial

```bash
$ singularity pull shub://aminnayebi/ContainerMOE:ubuntumoe-xenial
```

## Singularity Recipe

```singularity
Bootstrap: docker
	From: ubuntu:xenial

%labels
	MAINTAINER aminnayebi

%post
	echo "It starts updating apt-get and installing essentials"
	apt-get update && apt-get -y install wget build-essential

%runscript
	echo "This is running!"
```

## Collection

 - Name: [aminnayebi/ContainerMOE](https://github.com/aminnayebi/ContainerMOE)
 - License: None

