---
id: 10049
name: "lsx1980/3D_model_reconstruction"
branch: "master"
tag: "latest"
commit: "03092287ff755e01f4a2f760323bd0072e2d61c4"
version: "b55a8bd96be7db1aa9d9cc950044bb7f"
build_date: "2019-06-26T22:56:27.295Z"
size_mb: 1699
size: 648982559
sif: "https://datasets.datalad.org/shub/lsx1980/3D_model_reconstruction/latest/2019-06-26-03092287-b55a8bd9/b55a8bd96be7db1aa9d9cc950044bb7f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/lsx1980/3D_model_reconstruction/latest/2019-06-26-03092287-b55a8bd9/
recipe: https://datasets.datalad.org/shub/lsx1980/3D_model_reconstruction/latest/2019-06-26-03092287-b55a8bd9/Singularity
collection: lsx1980/3D_model_reconstruction
---

# lsx1980/3D_model_reconstruction:latest

```bash
$ singularity pull shub://lsx1980/3D_model_reconstruction:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%help
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
      python-setuptools \
      python-numpy \
      python-opencv \
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
  #/opt/code/vsfm/bin/VisualSFM "$@"
  
   echo "Arguments received: $*"
   exec /usr/bin/python "$@"

%test
  #----------------------------------------------------------
  # commands to be executed within container at close of bootstrap process
  #----------------------------------------------------------
   python --version
   #python requirement.py
```

## Collection

 - Name: [lsx1980/3D_model_reconstruction](https://github.com/lsx1980/3D_model_reconstruction)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

