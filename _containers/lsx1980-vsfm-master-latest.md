---
id: 6028
name: "lsx1980/vsfm-master"
branch: "master"
tag: "latest"
commit: "7ef5803cf863638ee953b901072358f863c76634"
version: "9e141f3f68609aaceb63c8481a758aa0"
build_date: "2020-11-30T18:53:24.478Z"
size_mb: 1622
size: 622522399
sif: "https://datasets.datalad.org/shub/lsx1980/vsfm-master/latest/2020-11-30-7ef5803c-9e141f3f/9e141f3f68609aaceb63c8481a758aa0.simg"
url: https://datasets.datalad.org/shub/lsx1980/vsfm-master/latest/2020-11-30-7ef5803c-9e141f3f/
recipe: https://datasets.datalad.org/shub/lsx1980/vsfm-master/latest/2020-11-30-7ef5803c-9e141f3f/Singularity
collection: lsx1980/vsfm-master
---

# lsx1980/vsfm-master:latest

```bash
$ singularity pull shub://lsx1980/vsfm-master:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%help
  Help will go here

  Special thanks goes to https://gist.github.com/lvisintini/e07abae48f099b913f9cf1c1f0fe43ba

%labels
  Maintainer: Chris Cotter
  Version v0.01

%setup
  mkdir ${SINGULARITY_ROOTFS}/opt/code/

%files
  ./* /opt/code

%post
  #######################################################################################
  # Install dependencies
  apt update
  apt install -y \
      wget \
      build-essential \
      python3 \
      unzip \
      glew-utils \
      imagemagick \
      libgtk2.0-dev \
      libglew-dev \
      libdevil-dev \
      libboost-all-dev \
      libatlas-cpp-0.6-dev \
      libatlas-dev \
      libatlas-base-dev \
      liblapack3 \
      libblas3 \
      libblas-dev \
      libcminpack-dev \
      libgfortran3 \
      libmetis-edf-dev \
      libparmetis-dev \
      libjpeg-turbo8 \
      libgsl-dev \
      freeglut3-dev

  cd /opt/code
  make clean
  make all
  
  mkdir /lscratch /db /work /scratch
  
  chmod -R a+rwx /opt/code

%environment
  PATH=$PATH:/opt/code/vsfm/bin/
  export PATH
  LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/code/vsfm/bin/
  export LD_LIBRARY_PATH

%runscript
  /opt/code/vsfm/bin/VisualSFM "$@"
```

## Collection

 - Name: [lsx1980/vsfm-master](https://github.com/lsx1980/vsfm-master)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

