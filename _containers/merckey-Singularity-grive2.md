---
id: 8033
name: "merckey/Singularity"
branch: "master"
tag: "grive2"
commit: "64a00ab9de19c775056b755d01c4c6fad6fb9419"
version: "f34086ae7cbba81e201f7f720894cfc6"
build_date: "2019-03-30T02:29:56.248Z"
size_mb: 785
size: 255975455
sif: "https://datasets.datalad.org/shub/merckey/Singularity/grive2/2019-03-30-64a00ab9-f34086ae/f34086ae7cbba81e201f7f720894cfc6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/merckey/Singularity/grive2/2019-03-30-64a00ab9-f34086ae/
recipe: https://datasets.datalad.org/shub/merckey/Singularity/grive2/2019-03-30-64a00ab9-f34086ae/Singularity
collection: merckey/Singularity
---

# merckey/Singularity:grive2

```bash
$ singularity pull shub://merckey/Singularity:grive2
```

## Singularity Recipe

```singularity
# Google Drive client
#

  Bootstrap: docker
  From: ubuntu:16.04

%post
# Set up the basics
  apt-get -y update
  apt-get install -y build-essential
  apt-get install -y git cmake build-essential libgcrypt11-dev libyajl-dev \
  libcurl4-openssl-dev libexpat1-dev binutils-dev
  apt-get -y update
  apt-get install -y zlib1g-dev libncurses5-dev libssl-dev pkg-config \
  libboost-all-dev libcppunit-dev
# Install grive 

  cd / && git clone https://github.com/vitalif/grive2 && \
  cd /grive2 && \
  mkdir build && \
  cd build && \
  cmake .. && \
  make -j4 && \
  mv /grive2/build/grive/grive /usr/local/bin/grive && \
  rm -rf /grive2


%runscript 
  grive "$@"
```

## Collection

 - Name: [merckey/Singularity](https://github.com/merckey/Singularity)
 - License: None

