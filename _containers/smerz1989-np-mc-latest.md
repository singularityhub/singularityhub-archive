---
id: 11681
name: "smerz1989/np-mc"
branch: "update_swap"
tag: "latest"
commit: "81b5e8862f34346b240e6792a9776331ba955684"
version: "b3b37d0368c9629caee6bb5c662d71f7"
build_date: "2020-07-06T20:23:07.775Z"
size_mb: 1841.0
size: 1022963743
sif: "https://datasets.datalad.org/shub/smerz1989/np-mc/latest/2020-07-06-81b5e886-b3b37d03/b3b37d0368c9629caee6bb5c662d71f7.sif"
url: https://datasets.datalad.org/shub/smerz1989/np-mc/latest/2020-07-06-81b5e886-b3b37d03/
recipe: https://datasets.datalad.org/shub/smerz1989/np-mc/latest/2020-07-06-81b5e886-b3b37d03/Singularity
collection: smerz1989/np-mc
---

# smerz1989/np-mc:latest

```bash
$ singularity pull shub://smerz1989/np-mc:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%post
	apt-get -y update
	apt-get -y install git\
			 cmake\
			build-essential\
			python3-dev\
			libpython3-dev\
			python3\
			python3-pip
	git clone -b stable_12Dec2018 https://github.com/lammps/lammps.git
	git clone https://github.com/smerz1989/np-mc.git
	cd lammps
	mkdir build
	cd build
	cmake -D PKG_PYTHON=on -D PKG_USER-MISC=on -D PKG_MC=on -D PKG_MOLECULE=on -D PKG_RIGID=on -D BUILD_LIB=on -D BUILD_SHARED_LIBS=on -D CMAKE_INSTALL_PREFIX=/usr/local ../cmake
	make
	make install
	cd ../../np-mc/
	pip3 install .

%environment
	
	export PATH=/usr/local/bin:$PATH
	export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
	export PYTHONPATH=/usr/local/lib/python3/dist-packages/:$PYTHONPATH

%runscript

	lmp "$@"
```

## Collection

 - Name: [smerz1989/np-mc](https://github.com/smerz1989/np-mc)
 - License: None

