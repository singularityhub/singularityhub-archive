---
id: 14006
name: "kiwiroy/singularity-tomahawk"
branch: "master"
tag: "0.7.1"
commit: "218a7a9e5774ec88bf1f2bf3930fece2626b68be"
version: "bea28b163de7945508c0d4bbbfe58aee5dc023ed07e3ed0ed4cfcba2ab144849"
build_date: "2020-08-20T01:12:47.930Z"
size_mb: 57.91015625
size: 60723200
sif: "https://datasets.datalad.org/shub/kiwiroy/singularity-tomahawk/0.7.1/2020-08-20-218a7a9e-bea28b16/bea28b163de7945508c0d4bbbfe58aee5dc023ed07e3ed0ed4cfcba2ab144849.sif"
url: https://datasets.datalad.org/shub/kiwiroy/singularity-tomahawk/0.7.1/2020-08-20-218a7a9e-bea28b16/
recipe: https://datasets.datalad.org/shub/kiwiroy/singularity-tomahawk/0.7.1/2020-08-20-218a7a9e-bea28b16/Singularity
collection: kiwiroy/singularity-tomahawk
---

# kiwiroy/singularity-tomahawk:0.7.1

```bash
$ singularity pull shub://kiwiroy/singularity-tomahawk:0.7.1
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:bionic

%labels
  Author kiwiroy@users-noreply.github.com
  Maintainer roy.storey@plantandfood.co.nz
  Version 0.7.1

%post
### install / update system dependencies
  apt-get -y update && apt-get -y install \
      autoconf             \
      build-essential      \
      curl                 \
      git                  \
      libbz2-dev           \
      libcurl4             \
      libcurl4-openssl-dev \
      liblz4-dev           \
      liblzma-dev          \
      libssl-dev           \
      libzstd-dev          \
      zlib1g-dev
### install htslib 1.9 due to a dependency
  git clone https://github.com/samtools/htslib.git htslib-1.9
  cd htslib-1.9
  git reset --hard 1832d3a
  autoreconf && ./configure && make -j5 && make install
  cd ..
### install zstd - commented as libzstd-dev installs enough
  # git clone https://github.com/facebook/zstd.git zstd
  # cd zstd
  # make -j5 V=1 && make install V=1
  # cd ..
### clone project
  git clone https://github.com/mklarqvist/tomahawk.git tomahawk
  cd tomahawk
  git reset --hard beta-0.7.1
  make -j5 && make install
### update ld.so.cache - avoid setting LD_LIBRARY_PATH for libhts.so
  ldconfig

### cleanup
  rm -rf /htslib-1.9 /tomahawk
  apt-get -y remove autoconf build-essential curl git libbz2-dev libcurl4-openssl-dev liblz4-dev liblzma-dev libssl-dev libzstd-dev zlib1g-dev
  apt-get -y autoremove

%runscript
  exec tomahawk "$@"
```

## Collection

 - Name: [kiwiroy/singularity-tomahawk](https://github.com/kiwiroy/singularity-tomahawk)
 - License: None

