---
id: 13335
name: "jacobsanz97/ga82img"
branch: "master"
tag: "latest"
commit: "ea621512db0dd1fa6976f5d44e57a40f86893e42"
version: "bf2e06126876a74d7e016a937a1efb97"
build_date: "2020-06-19T18:59:49.685Z"
size_mb: 402.0
size: 145346591
sif: "https://datasets.datalad.org/shub/jacobsanz97/ga82img/latest/2020-06-19-ea621512-bf2e0612/bf2e06126876a74d7e016a937a1efb97.sif"
url: https://datasets.datalad.org/shub/jacobsanz97/ga82img/latest/2020-06-19-ea621512-bf2e0612/
recipe: https://datasets.datalad.org/shub/jacobsanz97/ga82img/latest/2020-06-19-ea621512-bf2e0612/Singularity
collection: jacobsanz97/ga82img
---

# jacobsanz97/ga82img:latest

```bash
$ singularity pull shub://jacobsanz97/ga82img:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:sid

%post
 
	echo "Here we are installing software and other dependencies for the container"
	apt-get update
	apt-get install -y gnupg
	#wget -O- http://neuro.debian.net/lists/sid.us-ca.full | tee /etc/apt/sources.list.d/neurodebian.sources.list
	#apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9
	apt-get update
	apt-get install -y git-annex
	apt-get clean
	

#%environments
#    unset PYTHONPATH

%runscript

    git-annex "$@"
```

## Collection

 - Name: [jacobsanz97/ga82img](https://github.com/jacobsanz97/ga82img)
 - License: None

