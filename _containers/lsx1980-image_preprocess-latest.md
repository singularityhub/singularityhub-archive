---
id: 9958
name: "lsx1980/image_preprocess"
branch: "master"
tag: "latest"
commit: "b087318ec061ccc5bca6c8ad60125c98e3f6b5f2"
version: "4096ee9d8c76b7b142c59cd273e046c2"
build_date: "2019-06-25T18:43:29.798Z"
size_mb: 619
size: 229343263
sif: "https://datasets.datalad.org/shub/lsx1980/image_preprocess/latest/2019-06-25-b087318e-4096ee9d/4096ee9d8c76b7b142c59cd273e046c2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/lsx1980/image_preprocess/latest/2019-06-25-b087318e-4096ee9d/
recipe: https://datasets.datalad.org/shub/lsx1980/image_preprocess/latest/2019-06-25-b087318e-4096ee9d/Singularity
collection: lsx1980/image_preprocess
---

# lsx1980/image_preprocess:latest

```bash
$ singularity pull shub://lsx1980/image_preprocess:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels
  Maintainer: Suxing Liu
  Version v1.01

%setup
  #----------------------------------------------------------------------
  # commands to be executed on host outside container during bootstrap
  #----------------------------------------------------------------------
  mkdir ${SINGULARITY_ROOTFS}/opt/code/

%files
  ./* /opt/code/

%post
  #----------------------------------------------------------
  # Install common dependencies and create default entrypoint,
  # commands to be executed inside container during bootstrap
  #----------------------------------------------------------
  # Install dependencies
  apt update
  apt install -y \
    build-essential \
    python3 \
    python-setuptools \
    python-numpy \
    python-opencv 


  mkdir /lscratch /db /work /scratch
  
  chmod -R a+rwx /opt/code/
  
%environment
  #----------------------------------------------------------
  # Setup environment variables
  #----------------------------------------------------------
  PYTHONPATH=$PYTHONPATH:/opt/code/
  export PATH
  LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/code/
  export LD_LIBRARY_PATH

%runscript
  #----------------------------------------------------------
  # Run scripts inside container
  #----------------------------------------------------------
   # commands to be executed when the container runs
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

 - Name: [lsx1980/image_preprocess](https://github.com/lsx1980/image_preprocess)
 - License: None

