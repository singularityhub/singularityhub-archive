---
id: 12750
name: "manvari/dockerhub-d2l-cu102"
branch: "master"
tag: "latest"
commit: "8b84e1853307ffade258c226da3b9c9b31c53266"
version: "c3d7e950d81bcab0dab95918d64f9fef"
build_date: "2020-04-20T11:37:13.970Z"
size_mb: 3035.0
size: 2058342431
sif: "https://datasets.datalad.org/shub/manvari/dockerhub-d2l-cu102/latest/2020-04-20-8b84e185-c3d7e950/c3d7e950d81bcab0dab95918d64f9fef.sif"
url: https://datasets.datalad.org/shub/manvari/dockerhub-d2l-cu102/latest/2020-04-20-8b84e185-c3d7e950/
recipe: https://datasets.datalad.org/shub/manvari/dockerhub-d2l-cu102/latest/2020-04-20-8b84e185-c3d7e950/Singularity
collection: manvari/dockerhub-d2l-cu102
---

# manvari/dockerhub-d2l-cu102:latest

```bash
$ singularity pull shub://manvari/dockerhub-d2l-cu102:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian

%post

	apt-get update && apt-get install -y curl git unzip
	curl -fsSL https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh
	chmod +x /miniconda.sh
	.//miniconda.sh -b -p /miniconda
	rm /miniconda.sh

	mkdir /d2l && cd /d2l
	curl -O https://d2l.ai/d2l-en.zip
	unzip d2l-en.zip && rm d2l-en.zip

	bash -c "\
		source /miniconda/bin/activate && \
		cd /d2l && \
		conda create --name d2l -y && \
		conda activate d2l && \
		conda install python=3.7 pip -y && \
		pip install mxnet-cu102 git+https://github.com/d2l-ai/d2l-en && \
		conda deactivate \
	"
	chmod -R 777 /d2l

%runscript

	bash -c "\
		source /miniconda/bin/activate && \
		cd /d2l && \
		conda activate d2l && \
		jupyter notebook \
	"
```

## Collection

 - Name: [manvari/dockerhub-d2l-cu102](https://github.com/manvari/dockerhub-d2l-cu102)
 - License: None

