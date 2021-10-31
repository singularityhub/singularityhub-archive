---
id: 2712
name: "thakurshalabh08/Singularity"
branch: "master"
tag: "latest"
commit: "c0e068cc49545ac8a6b62c066394067431da2773"
version: "699b7cc0d05b706d5caf2b0a21db9e3d"
build_date: "2019-09-16T14:05:12.176Z"
size_mb: 273
size: 120258591
sif: "https://datasets.datalad.org/shub/thakurshalabh08/Singularity/latest/2019-09-16-c0e068cc-699b7cc0/699b7cc0d05b706d5caf2b0a21db9e3d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/thakurshalabh08/Singularity/latest/2019-09-16-c0e068cc-699b7cc0/
recipe: https://datasets.datalad.org/shub/thakurshalabh08/Singularity/latest/2019-09-16-c0e068cc-699b7cc0/Singularity
collection: thakurshalabh08/Singularity
---

# thakurshalabh08/Singularity:latest

```bash
$ singularity pull shub://thakurshalabh08/Singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%help
	This is a test container.

%post
	apt-get update
	apt -y install gcc
	apt -y install g++
	apt -y install make
```

## Collection

 - Name: [thakurshalabh08/Singularity](https://github.com/thakurshalabh08/Singularity)
 - License: None

