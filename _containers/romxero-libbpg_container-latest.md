---
id: 15011
name: "romxero/libbpg_container"
branch: "main"
tag: "latest"
commit: "98b273d318bc38cec8a7d1e65d7fd14aabeddd12"
version: "a7c8eeae4cc790ee22538b3578374319"
build_date: "2020-12-01T06:23:04.733Z"
size_mb: 1240.0
size: 405413919
sif: "https://datasets.datalad.org/shub/romxero/libbpg_container/latest/2020-12-01-98b273d3-a7c8eeae/a7c8eeae4cc790ee22538b3578374319.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/romxero/libbpg_container/latest/2020-12-01-98b273d3-a7c8eeae/
recipe: https://datasets.datalad.org/shub/romxero/libbpg_container/latest/2020-12-01-98b273d3-a7c8eeae/Singularity
collection: romxero/libbpg_container
---

# romxero/libbpg_container:latest

```bash
$ singularity pull shub://romxero/libbpg_container:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
Author "Randall Cab White - rcwhite@stanford.edu"

###########
#%setup
###########
###########

#Downlaod packages
%post
  apt-get -ym update
  apt-get -ym install libsdl2-image-2.0-0 libsdl2-image-dev gcc yasm \
wget curl gnupg2 jq sed gawk util-linux libsdl-dev \
git cmake build-essential parallel libjpeg-dev libsdl-image* \
rsync perl ssh openssl coreutils emscripten libpng-dev

#grabbing building libbpg
mkdir /bpgbuild
cd /bpgbuild
git clone https://github.com/mirrorer/libbpg

####
cd libbpg
make
make install
make clean

%environment
  export IMAGE_NAME="libbpg_container"
%runscript
#
```

## Collection

 - Name: [romxero/libbpg_container](https://github.com/romxero/libbpg_container)
 - License: None

