---
id: 2942
name: "ManojGopale/Ubuntu_Anaconda_Tensorflow"
branch: "master"
tag: "modified_env"
commit: "24cf55315e43b593a0741ef45bf259382f3722d2"
version: "e1f890c06c184343dabb7e6a7477137d"
build_date: "2018-05-27T16:15:48.108Z"
size_mb: 4158
size: 2139287583
sif: "https://datasets.datalad.org/shub/ManojGopale/Ubuntu_Anaconda_Tensorflow/modified_env/2018-05-27-24cf5531-e1f890c0/e1f890c06c184343dabb7e6a7477137d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ManojGopale/Ubuntu_Anaconda_Tensorflow/modified_env/2018-05-27-24cf5531-e1f890c0/
recipe: https://datasets.datalad.org/shub/ManojGopale/Ubuntu_Anaconda_Tensorflow/modified_env/2018-05-27-24cf5531-e1f890c0/Singularity
collection: ManojGopale/Ubuntu_Anaconda_Tensorflow
---

# ManojGopale/Ubuntu_Anaconda_Tensorflow:modified_env

```bash
$ singularity pull shub://ManojGopale/Ubuntu_Anaconda_Tensorflow:modified_env
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
	echo "export PATH="$HOME/anaconda/bin:$PATH"" >> $SINGULARITY_ENVIRONMENT
	export PATH="$HOME/anaconda/bin:$PATH"

	conda update -y conda
	pip install --upgrade tensorflow
	pip install keras
	conda update -y conda
```

## Collection

 - Name: [ManojGopale/Ubuntu_Anaconda_Tensorflow](https://github.com/ManojGopale/Ubuntu_Anaconda_Tensorflow)
 - License: None

