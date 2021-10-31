---
id: 3652
name: "cshelton/devcontainer"
branch: "master"
tag: "latest"
commit: "27a8766062975f9e23bb36292db5bc18ac9a0440"
version: "4aed9d5516482d1604c8aa62f504709e"
build_date: "2018-07-24T21:22:23.445Z"
size_mb: 1024
size: 394694687
sif: "https://datasets.datalad.org/shub/cshelton/devcontainer/latest/2018-07-24-27a87660-4aed9d55/4aed9d5516482d1604c8aa62f504709e.simg"
url: https://datasets.datalad.org/shub/cshelton/devcontainer/latest/2018-07-24-27a87660-4aed9d55/
recipe: https://datasets.datalad.org/shub/cshelton/devcontainer/latest/2018-07-24-27a87660-4aed9d55/Singularity
collection: cshelton/devcontainer
---

# cshelton/devcontainer:latest

```bash
$ singularity pull shub://cshelton/devcontainer:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: fedora:28

%post
	dnf -y update
	dnf -y install gcc gdb make gcc-c++ cgdb
	dnf -y install vim git patch diffstat
	dnf -y install boost-devel
	dnf -y install valgrind
	dnf -y install man-pages
```

## Collection

 - Name: [cshelton/devcontainer](https://github.com/cshelton/devcontainer)
 - License: None

