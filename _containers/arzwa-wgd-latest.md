---
id: 6263
name: "arzwa/wgd"
branch: "master"
tag: "latest"
commit: "6154c88c7b4cc1effe34f3a30c6bd707e0da4620"
version: "2982aea32b0cb0326563a709f2d3c94b"
build_date: "2021-04-07T13:18:11.140Z"
size_mb: 1177
size: 503529503
sif: "https://datasets.datalad.org/shub/arzwa/wgd/latest/2021-04-07-6154c88c-2982aea3/2982aea32b0cb0326563a709f2d3c94b.simg"
url: https://datasets.datalad.org/shub/arzwa/wgd/latest/2021-04-07-6154c88c-2982aea3/
recipe: https://datasets.datalad.org/shub/arzwa/wgd/latest/2021-04-07-6154c88c-2982aea3/Singularity
collection: arzwa/wgd
---

# arzwa/wgd:latest

```bash
$ singularity pull shub://arzwa/wgd:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu

%runscript
	wgd --help

%help
	wgd --help

%labels
	AUTHOR arzwa@psb.vib-ugent.be

%environment
	# click was complaining about this
	export LC_ALL=C.UTF-8
	export LANG=C.UTF-8

%post
	# install python, git, etc.
	apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -yq install python3-pip python3-tk git wget \
	    build-essential mcl ncbi-blast+ muscle mafft prank fasttree phyml paml

	# set an alias for fasttree
	ln -s /usr/bin/fasttree /usr/bin/FastTree

	# get wgd
	git clone https://github.com/arzwa/wgd.git
	cd wgd

	# install wgd
	pip3 install .
```

## Collection

 - Name: [arzwa/wgd](https://github.com/arzwa/wgd)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

