---
id: 5732
name: "romxero/loadcaffe_singularity"
branch: "master"
tag: "latest"
commit: "7f832fe3c13a63af790387bef3004d09f93fdfb8"
version: "5e35b7c193070eb74f7d3eaf5a3db8e9"
build_date: "2018-11-30T00:08:57.268Z"
size_mb: 581
size: 215670815
sif: "https://datasets.datalad.org/shub/romxero/loadcaffe_singularity/latest/2018-11-30-7f832fe3-5e35b7c1/5e35b7c193070eb74f7d3eaf5a3db8e9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/romxero/loadcaffe_singularity/latest/2018-11-30-7f832fe3-5e35b7c1/
recipe: https://datasets.datalad.org/shub/romxero/loadcaffe_singularity/latest/2018-11-30-7f832fe3-5e35b7c1/Singularity
collection: romxero/loadcaffe_singularity
---

# romxero/loadcaffe_singularity:latest

```bash
$ singularity pull shub://romxero/loadcaffe_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
Author "Randall Cab White - rcwhite@stanford.edu"

#########
#%setup
#########

##Just grabbing default packages from ubuntu repository
%post
	apt-get -ym update
    apt-get -ym install git bison cmake flex gcc g++ tcl-tclreadline # GNU toolchain
    apt-get -ym install libprotobuf-dev protobuf-compiler # GSL
    apt-get -ym install readline-common libreadline-dev #readline
    apt-get -ym install openssl libssl-dev
    apt-get -ym install wget curl zip #grabbing utilities
	export PREFIX=/usr/local
	mkdir -p /home
	cd /home
	git clone https://github.com/torch/distro.git ~/torch --recursive
	cd ~/torch
	./clean.sh
	./install.sh
	ls -lrths 
	
	luarocks install image
	luarocks install torch
	luarocks install nn
	luarocks install graph
	luarocks install torchnet
	luarocks install optnet
	luarocks install optim
	luarocks install iterm
	luarocks list
	
	
	luarocks install luasocket	
	luarocks install loadcaffe
	

%environment
	export IMAGE_NAME="LOAD_CAFFE"
```

## Collection

 - Name: [romxero/loadcaffe_singularity](https://github.com/romxero/loadcaffe_singularity)
 - License: None

