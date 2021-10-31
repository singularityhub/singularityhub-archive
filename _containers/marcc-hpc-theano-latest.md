---
id: 816
name: "marcc-hpc/theano"
branch: "master"
tag: "latest"
commit: "974385999850975551ae731bcb4ccd89d9fa3c2f"
version: "0f9a11f4288b9d3f025ae24796bb7d7f"
build_date: "2020-04-15T22:29:38.861Z"
size_mb: 5630
size: 3161509919
sif: "https://datasets.datalad.org/shub/marcc-hpc/theano/latest/2020-04-15-97438599-0f9a11f4/0f9a11f4288b9d3f025ae24796bb7d7f.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/theano/latest/2020-04-15-97438599-0f9a11f4/
recipe: https://datasets.datalad.org/shub/marcc-hpc/theano/latest/2020-04-15-97438599-0f9a11f4/Singularity
collection: marcc-hpc/theano
---

# marcc-hpc/theano:latest

```bash
$ singularity pull shub://marcc-hpc/theano:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

%environment

  # use bash as default shell
  SHELL=/bin/bash

  # add CUDA paths
  CPATH="/usr/local/cuda/include:$CPATH"
  PATH="/usr/local/cuda/bin:$PATH"
  LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"
  CUDA_HOME="/usr/local/cuda"

  # add Anaconda path
  PATH="/usr/local/anaconda3/bin:$PATH"

  export PATH LD_LIBRARY_PATH CPATH CUDA_HOME

%setup
  # runs on host
  # the path to the image is $SINGULARITY_ROOTFS

%post
  # post-setup script

  # load environment variables
  . /environment

  # use bash as default shell
  echo "\n #Using bash as default shell \n" >> /environment
  echo 'SHELL=/bin/bash' >> /environment

  # make environment file executable
  chmod +x /environment

  # default mount paths
  mkdir /scratch /data 

  #Add CUDA paths
  echo "\n #Cuda paths \n" >> /environment
  echo 'export CPATH="/usr/local/cuda/include:$CPATH"' >> /environment
  echo 'export PATH="/usr/local/cuda/bin:$PATH"' >> /environment
  echo 'export LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"' >> /environment
  echo 'export CUDA_HOME="/usr/local/cuda"' >> /environment

  # updating and getting required packages
  apt-get update
  apt-get install -y wget git vim

  # creates a build directory
  mkdir build
  cd build

  # download and install Anaconda
  CONDA_INSTALL_PATH="/usr/local/anaconda3"
  wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
  chmod +x Anaconda3-5.0.1-Linux-x86_64.sh
  ./Anaconda3-5.0.1-Linux-x86_64.sh -b -p $CONDA_INSTALL_PATH

  # install theano rc
  conda install -c mila-udem -c mila-udem/labels/pre theano pygpu

  # install keras
  pip install keras

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [marcc-hpc/theano](https://github.com/marcc-hpc/theano)
 - License: None

