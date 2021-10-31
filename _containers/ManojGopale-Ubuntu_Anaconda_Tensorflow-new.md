---
id: 2610
name: "ManojGopale/Ubuntu_Anaconda_Tensorflow"
branch: "master"
tag: "new"
commit: "10248533793d5018f659cf617012cb86f917498f"
version: "2ba76f143d84e5b34728fb5b381e559d"
build_date: "2020-12-14T15:44:16.173Z"
size_mb: 4166
size: 2145787935
sif: "https://datasets.datalad.org/shub/ManojGopale/Ubuntu_Anaconda_Tensorflow/new/2020-12-14-10248533-2ba76f14/2ba76f143d84e5b34728fb5b381e559d.simg"
url: https://datasets.datalad.org/shub/ManojGopale/Ubuntu_Anaconda_Tensorflow/new/2020-12-14-10248533-2ba76f14/
recipe: https://datasets.datalad.org/shub/ManojGopale/Ubuntu_Anaconda_Tensorflow/new/2020-12-14-10248533-2ba76f14/Singularity
collection: ManojGopale/Ubuntu_Anaconda_Tensorflow
---

# ManojGopale/Ubuntu_Anaconda_Tensorflow:new

```bash
$ singularity pull shub://ManojGopale/Ubuntu_Anaconda_Tensorflow:new
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%post
	mkdir /extra
	mkdir /xdisk
	mkdir /rsgrps

	apt-get update
	apt-get install -y wget
	apt-get install -y bzip2
	apt-get install -y vim

	wget https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
	bash Anaconda3-5.1.0-Linux-x86_64.sh -f -b -p $HOME/anaconda
	export PATH="$HOME/anaconda/bin:$PATH"

	conda update -y conda
	pip install --upgrade tensorflow
	pip install keras
	conda update -y conda
```

## Collection

 - Name: [ManojGopale/Ubuntu_Anaconda_Tensorflow](https://github.com/ManojGopale/Ubuntu_Anaconda_Tensorflow)
 - License: None

