---
id: 3086
name: "houzhengyang/gears-singularity"
branch: "master"
tag: "gears-tls"
commit: "a84414894462666917a65bf4951627696e3f8213"
version: "9481774be322c6370d1d0705670022e2"
build_date: "2018-06-08T05:56:44.714Z"
size_mb: 2739
size: 1106047007
sif: "https://datasets.datalad.org/shub/houzhengyang/gears-singularity/gears-tls/2018-06-08-a8441489-9481774b/9481774be322c6370d1d0705670022e2.simg"
url: https://datasets.datalad.org/shub/houzhengyang/gears-singularity/gears-tls/2018-06-08-a8441489-9481774b/
recipe: https://datasets.datalad.org/shub/houzhengyang/gears-singularity/gears-tls/2018-06-08-a8441489-9481774b/Singularity
collection: houzhengyang/gears-singularity
---

# houzhengyang/gears-singularity:gears-tls

```bash
$ singularity pull shub://houzhengyang/gears-singularity:gears-tls
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: bash

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
	git clone -b ubuntu-singularity https://github.com/gearslaboratory/las2pcd.git
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
```

## Collection

 - Name: [houzhengyang/gears-singularity](https://github.com/houzhengyang/gears-singularity)
 - License: None

