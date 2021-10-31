---
id: 7633
name: "aminnayebi/ContainerMOE"
branch: "master"
tag: "ubuntumoe"
commit: "dc9f0be840b4264d7c184e514d6f1e3af1b5c982"
version: "21ad4337f51e305d41f8b6a853509cbd"
build_date: "2019-03-07T01:18:17.701Z"
size_mb: 315
size: 124039199
sif: "https://datasets.datalad.org/shub/aminnayebi/ContainerMOE/ubuntumoe/2019-03-07-dc9f0be8-21ad4337/21ad4337f51e305d41f8b6a853509cbd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/aminnayebi/ContainerMOE/ubuntumoe/2019-03-07-dc9f0be8-21ad4337/
recipe: https://datasets.datalad.org/shub/aminnayebi/ContainerMOE/ubuntumoe/2019-03-07-dc9f0be8-21ad4337/Singularity
collection: aminnayebi/ContainerMOE
---

# aminnayebi/ContainerMOE:ubuntumoe

```bash
$ singularity pull shub://aminnayebi/ContainerMOE:ubuntumoe
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

