---
id: 11957
name: "Computational-Plant-Science/3D_model_traits_demo"
branch: "master"
tag: "latest"
commit: "4269ec867de33c5cb6b909f7e6a0ebc40b3f25a7"
version: "1445583f61611e013530c59c1f8ccfae"
build_date: "2020-01-07T14:38:32.807Z"
size_mb: 1265.0
size: 558604319
sif: "https://datasets.datalad.org/shub/Computational-Plant-Science/3D_model_traits_demo/latest/2020-01-07-4269ec86-1445583f/1445583f61611e013530c59c1f8ccfae.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/Computational-Plant-Science/3D_model_traits_demo/latest/2020-01-07-4269ec86-1445583f/
recipe: https://datasets.datalad.org/shub/Computational-Plant-Science/3D_model_traits_demo/latest/2020-01-07-4269ec86-1445583f/Singularity
collection: Computational-Plant-Science/3D_model_traits_demo
---

# Computational-Plant-Science/3D_model_traits_demo:latest

```bash
$ singularity pull shub://Computational-Plant-Science/3D_model_traits_demo:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

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
    python3-setuptools \
    python3-pip \
    python3-tk \
    python3-numexpr \
    python3-pil.imagetk \
    libgl1-mesa-glx \
    libsm6 \
    libxext6
    
    
  pip3 install numpy \
                Pillow \
                rdp \
                scipy \
                scikit-image \
                matplotlib \
                plyfile \
                open3d \
                opencv-python \
                openpyxl

  pip3 install -U scikit-learn
  

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
   python3 --version
   #python3 requirement.py
```

## Collection

 - Name: [Computational-Plant-Science/3D_model_traits_demo](https://github.com/Computational-Plant-Science/3D_model_traits_demo)
 - License: None

