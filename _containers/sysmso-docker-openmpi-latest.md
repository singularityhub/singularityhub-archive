---
id: 1581
name: "sysmso/docker-openmpi"
branch: "master"
tag: "latest"
commit: "23a458433f1f5e3f9d16c3b8ab0da9a02be14c1a"
version: "4f421b3bb71e76112a44e8b1d3da125c"
build_date: "2019-12-29T15:53:53.250Z"
size_mb: 545
size: 207675423
sif: "https://datasets.datalad.org/shub/sysmso/docker-openmpi/latest/2019-12-29-23a45843-4f421b3b/4f421b3bb71e76112a44e8b1d3da125c.simg"
url: https://datasets.datalad.org/shub/sysmso/docker-openmpi/latest/2019-12-29-23a45843-4f421b3b/
recipe: https://datasets.datalad.org/shub/sysmso/docker-openmpi/latest/2019-12-29-23a45843-4f421b3b/Singularity
collection: sysmso/docker-openmpi
---

# sysmso/docker-openmpi:latest

```bash
$ singularity pull shub://sysmso/docker-openmpi:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%files
mpi-ping.c /mpi-ping.c

%labels
AUTHOR souchal@apc.in2p3.fr
version 1.0

%environment
LD_LIBRARY_PATH=/usr/local/lib/
export LD_LIBRARY_PATH

%post

apt-get update && apt-get -y install software-properties-common wget build-essential sgml-base rsync xml-core openssh-client
add-apt-repository universe
apt-get update && apt-get -y install cmake git gfortran openmpi-common openmpi-bin libopenmpi-dev
apt-get clean

%runscript
mpicc /mpi-ping.c
```

## Collection

 - Name: [sysmso/docker-openmpi](https://github.com/sysmso/docker-openmpi)
 - License: None

