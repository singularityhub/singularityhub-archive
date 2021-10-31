---
id: 15575
name: "MBlaschek/singularity-jupyter"
branch: "master"
tag: "stuff"
commit: "e48f3f7a2c7ab569fa1585d5c1e9df73f4d270e1"
version: "fc20c88e3d90c8f56b9e0aba8d097182df4447ca8a9ef824cae17d6e08e1edf2"
build_date: "2021-02-22T22:47:59.146Z"
size_mb: 1039.82421875
size: 1090334720
sif: "https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/stuff/2021-02-22-e48f3f7a-fc20c88e/fc20c88e3d90c8f56b9e0aba8d097182df4447ca8a9ef824cae17d6e08e1edf2.sif"
url: https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/stuff/2021-02-22-e48f3f7a-fc20c88e/
recipe: https://datasets.datalad.org/shub/MBlaschek/singularity-jupyter/stuff/2021-02-22-e48f3f7a-fc20c88e/Singularity
collection: MBlaschek/singularity-jupyter
---

# MBlaschek/singularity-jupyter:stuff

```bash
$ singularity pull shub://MBlaschek/singularity-jupyter:stuff
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%files
	run.sh /usr/bin

%runscript
	exec /usr/bin/run.sh "$@"

%apprun meld
	meld

%post
	apt-get -y update
	DEBIAN_FRONTEND=noninteractive apt-get -y install pandoc texlive-xetex texlive-fonts-recommended texlive-generic-recommended texlive-generic-extra

	# DEBIAN_FRONTEND=noninteractive apt-get -y install git xorg meld wget nano pandoc apt-transport-https
	# download atom editor
	# wget https://github.com/atom/atom/releases/download/v1.41.0/atom-amd64.deb
	# dpkg -i --force-depends atom-amd64.deb
	# install missing dependencies
	# DEBIAN_FRONTEND=noninteractive apt-get -y -f install
	# typora
	# wget -qO - https://typora.io/linux/public-key.asc | apt-key add -
	# echo "deb https://typora.io/linux ./" > /etc/apt/sources.list.d/typora.list
	# apt-get -y update
	# DEBIAN_FRONTEND=noninteractive apt-get -y install typora
	#
	# Clean
	#
	apt-get -y autoremove
	apt-get -y clean
	apt-get -y autoclean

%environment
	XDG_RUNTIME_DIR=$PWD/.runtime/
```

## Collection

 - Name: [MBlaschek/singularity-jupyter](https://github.com/MBlaschek/singularity-jupyter)
 - License: None

