---
id: 5969
name: "cottersci/vsfm-master"
branch: "master"
tag: "latest"
commit: "53303e3b8e186fb7be36214e8f5a6bcce042cb45"
version: "8e505c9af9607e5fd6f9cd5f12082ad2"
build_date: "2018-12-21T17:01:16.685Z"
size_mb: 1563
size: 606392351
sif: "https://datasets.datalad.org/shub/cottersci/vsfm-master/latest/2018-12-21-53303e3b-8e505c9a/8e505c9af9607e5fd6f9cd5f12082ad2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cottersci/vsfm-master/latest/2018-12-21-53303e3b-8e505c9a/
recipe: https://datasets.datalad.org/shub/cottersci/vsfm-master/latest/2018-12-21-53303e3b-8e505c9a/Singularity
collection: cottersci/vsfm-master
---

# cottersci/vsfm-master:latest

```bash
$ singularity pull shub://cottersci/vsfm-master:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%help
  Help will go here

  Special thanks goes to https://gist.github.com/lvisintini/e07abae48f099b913f9cf1c1f0fe43ba

%labels
  Maintainer Chris Cotter
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
      unzip \
      libgtk2.0-dev \
      libglew-dev \
      libdevil-dev \
      libboost-all-dev \
      libatlas-cpp-0.6-dev \
      libatlas-dev \
      imagemagick \
      libatlas3-base \
      libcminpack-dev \
      libgfortran3 \
      libmetis-edf-dev \
      libparmetis-dev \
      freeglut3-dev \
      libgsl-dev \
      glew-utils \
      libblas-dev \
      liblapack-dev

  cd /opt/code
  make clean
  make all

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

 - Name: [cottersci/vsfm-master](https://github.com/cottersci/vsfm-master)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

