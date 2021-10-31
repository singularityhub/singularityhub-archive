---
id: 10522
name: "serheang/sc_fenicsproject"
branch: "master"
tag: "latest"
commit: "b3f4ec5f45a3887dfe7ee628837ee9d3ede22c58"
version: "d73b1ce014b338a9a9886a10dc53fcb2"
build_date: "2020-10-04T13:08:08.571Z"
size_mb: 1924.0
size: 646963231
sif: "https://datasets.datalad.org/shub/serheang/sc_fenicsproject/latest/2020-10-04-b3f4ec5f-d73b1ce0/d73b1ce014b338a9a9886a10dc53fcb2.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/serheang/sc_fenicsproject/latest/2020-10-04-b3f4ec5f-d73b1ce0/
recipe: https://datasets.datalad.org/shub/serheang/sc_fenicsproject/latest/2020-10-04-b3f4ec5f-d73b1ce0/Singularity
collection: serheang/sc_fenicsproject
---

# serheang/sc_fenicsproject:latest

```bash
$ singularity pull shub://serheang/sc_fenicsproject:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%post
export DEBIAN_FRONTEND=noninteractive
apt-get -y update
apt-get -y install software-properties-common ffmpeg curl build-essential python3 python3-pip python3-tk
add-apt-repository universe
add-apt-repository ppa:ngsolve/ngsolve
add-apt-repository ppa:fenics-packages/fenics
apt-get -y update
apt-get -y install ngsolve
apt-get -y install --no-install-recommends fenics
pip3 install numpy scipy matplotlib pandas ffmpeg-python
ldconfig

%runscript
    exec /bin/bash -i
```

## Collection

 - Name: [serheang/sc_fenicsproject](https://github.com/serheang/sc_fenicsproject)
 - License: None

