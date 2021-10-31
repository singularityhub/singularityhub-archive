---
id: 11555
name: "lsx1980/3D_model_traits_measurement"
branch: "master"
tag: "latest"
commit: "e19d5465880fab2b557727b3a4b984ff86f63cbe"
version: "80a490e6d1a1549a1d75a722489531f0"
build_date: "2021-01-11T17:42:53.024Z"
size_mb: 1248.0
size: 561266719
sif: "https://datasets.datalad.org/shub/lsx1980/3D_model_traits_measurement/latest/2021-01-11-e19d5465-80a490e6/80a490e6d1a1549a1d75a722489531f0.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/lsx1980/3D_model_traits_measurement/latest/2021-01-11-e19d5465-80a490e6/
recipe: https://datasets.datalad.org/shub/lsx1980/3D_model_traits_measurement/latest/2021-01-11-e19d5465-80a490e6/Singularity
collection: lsx1980/3D_model_traits_measurement
---

# lsx1980/3D_model_traits_measurement:latest

```bash
$ singularity pull shub://lsx1980/3D_model_traits_measurement:latest
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

 - Name: [lsx1980/3D_model_traits_measurement](https://github.com/lsx1980/3D_model_traits_measurement)
 - License: None

