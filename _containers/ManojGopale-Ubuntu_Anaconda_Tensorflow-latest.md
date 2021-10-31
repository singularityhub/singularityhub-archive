---
id: 2565
name: "ManojGopale/Ubuntu_Anaconda_Tensorflow"
branch: "master"
tag: "latest"
commit: "c4dae0dfd01723f47ffad119f5150e947d2708ac"
version: "a6779bee0a9966d5ed460a3e55f92f79"
build_date: "2018-04-21T17:37:03.644Z"
size_mb: 4166
size: 2145787935
sif: "https://datasets.datalad.org/shub/ManojGopale/Ubuntu_Anaconda_Tensorflow/latest/2018-04-21-c4dae0df-a6779bee/a6779bee0a9966d5ed460a3e55f92f79.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ManojGopale/Ubuntu_Anaconda_Tensorflow/latest/2018-04-21-c4dae0df-a6779bee/
recipe: https://datasets.datalad.org/shub/ManojGopale/Ubuntu_Anaconda_Tensorflow/latest/2018-04-21-c4dae0df-a6779bee/Singularity
collection: ManojGopale/Ubuntu_Anaconda_Tensorflow
---

# ManojGopale/Ubuntu_Anaconda_Tensorflow:latest

```bash
$ singularity pull shub://ManojGopale/Ubuntu_Anaconda_Tensorflow:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%post
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

