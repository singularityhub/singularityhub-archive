---
id: 13037
name: "tin6150/pyvim"
branch: "master"
tag: "latest"
commit: "773bb2dffd97254d0097eb67d905223559aa2349"
version: "779c5aeb9300a88ce4dc9391a9ee9fb0786eb723fbedec37f450bde8e330576f"
build_date: "2021-01-07T18:10:36.286Z"
size_mb: 109.4453125
size: 114761728
sif: "https://datasets.datalad.org/shub/tin6150/pyvim/latest/2021-01-07-773bb2df-779c5aeb/779c5aeb9300a88ce4dc9391a9ee9fb0786eb723fbedec37f450bde8e330576f.sif"
url: https://datasets.datalad.org/shub/tin6150/pyvim/latest/2021-01-07-773bb2df-779c5aeb/
recipe: https://datasets.datalad.org/shub/tin6150/pyvim/latest/2021-01-07-773bb2df-779c5aeb/Singularity
collection: tin6150/pyvim
---

# tin6150/pyvim:latest

```bash
$ singularity pull shub://tin6150/pyvim:latest
```

## Singularity Recipe

```singularity
# Singularity container definition for 
# pyvim -- vim with python
# stock centos  8 vim really
# https://github.com/tin6150/vim
# https://singularity-hub.org/collections/


BootStrap: docker
#From: centos:7.6.1810
#From: centos:7
From: centos:8

%help
	This container is a CentOS  with a fuller version of vim that supports python
  Pull and run via singularity hub:
	singularity pull --name pyvim shub://tin6150/pyvim
  ./pyvim

%runscript
	#echo "vim from inside the container..."
	/usr/bin/vim "$@"


%post
	#echo "Hello from inside the container"
	touch /THIS_IS_INSIDE_SINGULARITY
	#yum -ty update 
	#yum -ty install vim python2 zsh environment-modules
	dnf --assumeyes --quiet install vim python2 zsh environment-modules

	echo "end"                  >> /THIS_IS_INSIDE_SINGULARITY
	date                        >> /THIS_IS_INSIDE_SINGULARITY

%labels
MAINTAINER  Tin Ho tin'at'lbl.gov
```

## Collection

 - Name: [tin6150/pyvim](https://github.com/tin6150/pyvim)
 - License: None

