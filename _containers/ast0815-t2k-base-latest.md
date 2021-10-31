---
id: 15286
name: "ast0815/t2k-base"
branch: "master"
tag: "latest"
commit: "bab8f4c069beb7d1b75b06a263b9c88364adc9ed"
version: "561a17d981f8f16b70904242e25bdeaa"
build_date: "2021-02-12T19:09:17.468Z"
size_mb: 1006.0
size: 317804575
sif: "https://datasets.datalad.org/shub/ast0815/t2k-base/latest/2021-02-12-bab8f4c0-561a17d9/561a17d981f8f16b70904242e25bdeaa.sif"
url: https://datasets.datalad.org/shub/ast0815/t2k-base/latest/2021-02-12-bab8f4c0-561a17d9/
recipe: https://datasets.datalad.org/shub/ast0815/t2k-base/latest/2021-02-12-bab8f4c0-561a17d9/Singularity
collection: ast0815/t2k-base
---

# ast0815/t2k-base:latest

```bash
$ singularity pull shub://ast0815/t2k-base:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
#### Download base image from cern repo on docker hub
From: cern/cc7-base:latest

%post
  #yum update -y
  yum group install -y "Development Tools"

  # Taken from nd280 base Dockerfile
  # TODO:  Clean undeeded packages
  yum install -y wget cmake3 python-devel ncurses-devel libX11-devel libxml2-devel libXpm-devel libXft-devel libXext-devel libcurl-devel mesa-dri-drivers ed imake krb5-devel openssl-devel tcsh krb5-devel openssl-devel graphviz-devel libXt-devel motif-devel freetype-devel gmp-devel gsl-devel glut-devel which man-db \
  gcc-gfortran openssl-devel pcre-devel \
  mesa-libGL-devel mesa-libGLU-devel glew-devel ftgl-devel mysql-devel \
  fftw-devel cfitsio-devel graphviz-devel \
  avahi-compat-libdns_sd-devel libldap-dev python-devel \
  libxml2-devel gsl-static gsl-devel \
  gcc-c++ gcc binutils \
  libX11-devel libXpm-devel libXft-devel libXext-devel lz4-devel davix-devel gl2ps-devel &&\
  yum install -y libzstd libzstd-devel xxhash xxhash-devel lz4-devel libAfterImage-devel glew-devel cfitsio-devel ftgl-devel davix davix-devel gl2ps-devel &&\
  yum clean all
```

## Collection

 - Name: [ast0815/t2k-base](https://github.com/ast0815/t2k-base)
 - License: None

