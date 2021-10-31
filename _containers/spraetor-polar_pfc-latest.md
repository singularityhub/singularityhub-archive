---
id: 14069
name: "spraetor/polar_pfc"
branch: "master"
tag: "latest"
commit: "fe80198eb6f425ecf36bc907b7eb204dc1ea5b4b"
version: "f80bb511cc035666a2f2c27463d8aabb"
build_date: "2020-08-30T19:19:12.196Z"
size_mb: 672.0
size: 194326559
sif: "https://datasets.datalad.org/shub/spraetor/polar_pfc/latest/2020-08-30-fe80198e-f80bb511/f80bb511cc035666a2f2c27463d8aabb.sif"
url: https://datasets.datalad.org/shub/spraetor/polar_pfc/latest/2020-08-30-fe80198e-f80bb511/
recipe: https://datasets.datalad.org/shub/spraetor/polar_pfc/latest/2020-08-30-fe80198e-f80bb511/Singularity
collection: spraetor/polar_pfc
---

# spraetor/polar_pfc:latest

```bash
$ singularity pull shub://spraetor/polar_pfc:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:buster

%labels
  Author simon.praetorius@tu-dresden.de"
  Version v0.1

%files
  code /app

%post
  apt-get update -y
  apt-get install -y --no-install-recommends \
      build-essential \
      ca-certificates \
      cmake \
      g++-8 \
      gcc-8 \
      git \
      libalglib-dev \
      libboost-dev \
      libeigen3-dev \
      libfftw3-dev \
      zlib1g-dev
  apt-get clean
  rm -rf /var/lib/apt/lists/*

%post
  mkdir -p /tmp/sources && cd /tmp/sources
  git clone https://github.com/jlblancoc/nanoflann.git --single-branch --branch master
  git clone https://bitbucket.org/nschaeff/shtns.git --single-branch --branch master

  cd /tmp/sources/shtns
  ./configure --prefix=/opt/software/shtns --enable-openmp
  make && make install

  mkdir -p /opt/software/nanoflann/include
  cp /tmp/sources/nanoflann/include/*.hpp /opt/software/nanoflann/include

  rm -rf /tmp/sources

%post
  mkdir /app/build && cd /app/build
  cmake -DCMAKE_BUILD_TYPE=Release \
        -DSHTNS_LIB:PATH=/opt/software/shtns/lib \
        -DSHTNS_INC:PATH=/opt/software/shtns/include \
        -DNANOFLANN_INC:PATH=/opt/software/nanoflann/include \
        -DALGLIB_INC:PATH=/usr/include/libalglib /app
  make

%environment
  export PATH=/app/build:$PATH

%runscript
  /app/build/polar_pfc $@
```

## Collection

 - Name: [spraetor/polar_pfc](https://github.com/spraetor/polar_pfc)
 - License: None

