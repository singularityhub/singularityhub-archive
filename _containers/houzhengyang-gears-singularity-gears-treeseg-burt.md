---
id: 3084
name: "houzhengyang/gears-singularity"
branch: "master"
tag: "gears-treeseg-burt"
commit: "88ac752dbc23abd7475bf6dd5014ede15b11220e"
version: "e4e16cc9ba4bd2b19736f570fd765feb"
build_date: "2018-06-08T05:56:44.723Z"
size_mb: 2739
size: 1106026527
sif: "https://datasets.datalad.org/shub/houzhengyang/gears-singularity/gears-treeseg-burt/2018-06-08-88ac752d-e4e16cc9/e4e16cc9ba4bd2b19736f570fd765feb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/houzhengyang/gears-singularity/gears-treeseg-burt/2018-06-08-88ac752d-e4e16cc9/
recipe: https://datasets.datalad.org/shub/houzhengyang/gears-singularity/gears-treeseg-burt/2018-06-08-88ac752d-e4e16cc9/Singularity
collection: houzhengyang/gears-singularity
---

# houzhengyang/gears-singularity:gears-treeseg-burt

```bash
$ singularity pull shub://houzhengyang/gears-singularity:gears-treeseg-burt
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: bash

# TLS Apps?

%environment
	LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib:/usr/lib
	export LD_LIBRARY_PATH

%post

# Setup locale and core build dependencies::
	sed -i 's/main/main restricted universe/g' /etc/apt/sources.list
	apt-get update
	apt-get install -y locales
	locale-gen en_US.UTF-8
	apt-get install -y git cmake

### las2pcd: https://github.com/murtiad/las2pcd
	cd
	apt-get install -y libpcl-dev liblas-dev liblas-c-dev
	git clone -b treeseg_fix https://github.com/gearslaboratory/las2pcd.git
	cd las2pcd
	cmake .
	make
	mv las2pcd /usr/bin/

## treeseg: https://github.com/apburt/treeseg
	cd
	apt-get install -y libarmadillo-dev libproj-dev libpcl-dev
	git clone -b ubuntu-singularity-verbose https://github.com/gearslaboratory/treeseg.git
	cd treeseg
	mkdir build
  	cd build
  	cmake ../src
  	make
	mv libtreeseg.so /usr/local/lib
	mv libleafsep.so /usr/local/lib
  	mv * /usr/local/bin
```

## Collection

 - Name: [houzhengyang/gears-singularity](https://github.com/houzhengyang/gears-singularity)
 - License: None

