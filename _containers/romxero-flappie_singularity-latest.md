---
id: 8459
name: "romxero/flappie_singularity"
branch: "master"
tag: "latest"
commit: "1989ba49cc7d387afce9ad85b81c78c9b5c7e528"
version: "d1d3699624b07f28c828f27293805d1a"
build_date: "2019-04-17T14:28:05.102Z"
size_mb: 1568
size: 550219807
sif: "https://datasets.datalad.org/shub/romxero/flappie_singularity/latest/2019-04-17-1989ba49-d1d36996/d1d3699624b07f28c828f27293805d1a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/romxero/flappie_singularity/latest/2019-04-17-1989ba49-d1d36996/
recipe: https://datasets.datalad.org/shub/romxero/flappie_singularity/latest/2019-04-17-1989ba49-d1d36996/Singularity
collection: romxero/flappie_singularity
---

# romxero/flappie_singularity:latest

```bash
$ singularity pull shub://romxero/flappie_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Author "Randall Cab White - rcwhite@stanford.edu"

#########
#%setup


#########
%post
	
	alias sudo='' #makes it easier to copy and paste tutorials =P
	apt-get -ym update
	apt-get -ym install git kdiff3 curl 
    apt-get -ym install cmake gcc # BUILD UTILS
    
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
    apt-get -ym install git-lfs
    
    git lfs install #redundant
    
    apt-get -ym install libcunit1 hdf5-tools libhdf5-10 libopenblas-base # Running libraries
	apt-get -ym install libcunit1-dev libhdf5-dev libopenblas-dev

	##apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
	##echo "deb http://download.mono-project.com/repo/debian wheezy main" | sudo tee /etc/apt/sources.list.d/mono-xamarin.list
	##apt-get -ym update
	##apt-get -ym install mono-complete
	
	
	git clone https://github.com/nanoporetech/flappie
	cd flappie
	make flappie
	
%environment
	export IMAGE_NAME="FLAGPIE"
	export PATH="/flappie/build:$PATH" #setting the path for flapp
```

## Collection

 - Name: [romxero/flappie_singularity](https://github.com/romxero/flappie_singularity)
 - License: None

