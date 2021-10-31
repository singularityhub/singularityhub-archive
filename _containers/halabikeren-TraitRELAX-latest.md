---
id: 15149
name: "halabikeren/TraitRELAX"
branch: "master"
tag: "latest"
commit: "a5682e1ee141d94d23bde21e72487b00207a1a10"
version: "747aefa9b7c0a81ae83ef7634773cbe4"
build_date: "2020-12-20T15:56:00.953Z"
size_mb: 5655.0
size: 926400543
sif: "https://datasets.datalad.org/shub/halabikeren/TraitRELAX/latest/2020-12-20-a5682e1e-747aefa9/747aefa9b7c0a81ae83ef7634773cbe4.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/halabikeren/TraitRELAX/latest/2020-12-20-a5682e1e-747aefa9/
recipe: https://datasets.datalad.org/shub/halabikeren/TraitRELAX/latest/2020-12-20-a5682e1e-747aefa9/Singularity
collection: halabikeren/TraitRELAX
---

# halabikeren/TraitRELAX:latest

```bash
$ singularity pull shub://halabikeren/TraitRELAX:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%help
TraitRELAX pre-copiled program version ${version}

%post
	export TZ=America/Los_Angeles
	ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
	apt-get update 
	apt-get install -y build-essential
	apt-get install -y tzdata
	apt-get install -y cmake
	apt-get install -y git
	apt-get install -y wget
	apt-get install -y pkg-config
	apt-get install -y libgomp1
	mkdir -p ./traitrelax/exec/
    wget https://github.com/halabikeren/TraitRELAX/releases/download/1.0.1/traitrelax_v1.0.1.tar.gz
    tar -xf traitrelax_v1.0.1.tar.gz -C ./traitrelax/
	mkdir -p /traitrelax/bpp-core/build/
    cd /traitrelax/bpp-core/build/
    cmake -DCMAKE_INSTALL_PREFIX=/traitrelax/ -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=TRUE ..
    make
    make install
	mkdir -p /traitrelax/bpp-seq/build/
    cd /traitrelax/bpp-seq/build/
    cmake -DCMAKE_INSTALL_PREFIX=/traitrelax/ -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=TRUE ..
    make
    make install
	mkdir -p /traitrelax/bpp-phyl/build/
    cd /traitrelax/bpp-phyl/build/
    cmake -DCMAKE_INSTALL_PREFIX=/traitrelax/ -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=TRUE ..
    make
    make install
	cd /traitrelax/TraitRELAX/
    cmake -DCMAKE_INSTALL_PREFIX=/traitrelax/ -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=TRUE .
    make
    make install

%runscript
    cd /traitrelax/exec
    exec /traitrelax/TraitRELAX/TraitRELAX/TraitRELAX param=$@
```

## Collection

 - Name: [halabikeren/TraitRELAX](https://github.com/halabikeren/TraitRELAX)
 - License: [Other](None)

