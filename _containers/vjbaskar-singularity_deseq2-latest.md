---
id: 12424
name: "vjbaskar/singularity_deseq2"
branch: "master"
tag: "latest"
commit: "e98584a14086db494c9918878869866082bc8b1d"
version: "33106ba6b94b71491f9548ec1fb8e611"
build_date: "2020-03-03T16:34:28.776Z"
size_mb: 1986.0
size: 619221023
sif: "https://datasets.datalad.org/shub/vjbaskar/singularity_deseq2/latest/2020-03-03-e98584a1-33106ba6/33106ba6b94b71491f9548ec1fb8e611.sif"
url: https://datasets.datalad.org/shub/vjbaskar/singularity_deseq2/latest/2020-03-03-e98584a1-33106ba6/
recipe: https://datasets.datalad.org/shub/vjbaskar/singularity_deseq2/latest/2020-03-03-e98584a1-33106ba6/Singularity
collection: vjbaskar/singularity_deseq2
---

# vjbaskar/singularity_deseq2:latest

```bash
$ singularity pull shub://vjbaskar/singularity_deseq2:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04


%files
	install_packages.R /tmp
	R-3.5.0.tar.gz /tmp
	deseq2.R 
	basic_functions.R
%post
	apt-get update
	apt-get install -y wget vim
	apt-get update --fix-missing
	apt-get -y install apt-utils
	apt-get -y install make zlib1g-dev build-essential ncurses-dev libbz2-dev liblzma-dev
	apt-get -y install gfortran libreadline-dev libx11-dev
	apt-get -y install evince
	apt-get -y install texlive-base  libpcre3-dev libcurl4-openssl-dev
	apt-get -y install default-jre openjdk-11-jre-headless
	apt-get -y install libxml2-dev
	apt-get -y install libssl-dev 
	cd /tmp/
	tar -zxvf R-3.5.0.tar.gz
	cd R-3.5.0
	./configure --with-x=no
	make -j 8
	make install
	Rscript /tmp/install_packages.R
	cd /
	mkdir -p hello
%runscript
	Rscript deseq2.R

%labels
	Author Vijay
	Email vjbaskar@gmail.com
```

## Collection

 - Name: [vjbaskar/singularity_deseq2](https://github.com/vjbaskar/singularity_deseq2)
 - License: None

