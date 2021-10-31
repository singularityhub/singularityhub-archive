---
id: 10503
name: "jrswartley/np-mc"
branch: "new_swap"
tag: "latest"
commit: "03f852dccf6ffb95d667a18c0bb374cce5e4b499"
version: "5bc17ee5e53ad0534a9019daaa74f21d"
build_date: "2019-09-24T18:35:55.669Z"
size_mb: 1755.0
size: 907448351
sif: "https://datasets.datalad.org/shub/jrswartley/np-mc/latest/2019-09-24-03f852dc-5bc17ee5/5bc17ee5e53ad0534a9019daaa74f21d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/jrswartley/np-mc/latest/2019-09-24-03f852dc-5bc17ee5/
recipe: https://datasets.datalad.org/shub/jrswartley/np-mc/latest/2019-09-24-03f852dc-5bc17ee5/Singularity
collection: jrswartley/np-mc
---

# jrswartley/np-mc:latest

```bash
$ singularity pull shub://jrswartley/np-mc:latest
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
	git clone -b new_swap https://github.com/jrswartley/np-mc.git
	cd lammps
	mkdir build
	cd build
	cmake -D PKG_PYTHON=on -D PKG_MC=on -D PKG_MOLECULE=on -D PKG_RIGID=on  -D BUILD_LIB=on -D BUILD_SHARED_LIBS=on -D CMAKE_INSTALL_PREFIX=/usr/local ../cmake
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

 - Name: [jrswartley/np-mc](https://github.com/jrswartley/np-mc)
 - License: None

