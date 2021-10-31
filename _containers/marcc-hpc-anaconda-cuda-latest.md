---
id: 1001
name: "marcc-hpc/anaconda-cuda"
branch: "master"
tag: "latest"
commit: "27791ff438d5b2c40705fbc54d6e7000482f2cab"
version: "003507adc29ff9676395cfc7a09affa9"
build_date: "2020-10-11T04:58:39.262Z"
size_mb: 6059
size: 3299057695
sif: "https://datasets.datalad.org/shub/marcc-hpc/anaconda-cuda/latest/2020-10-11-27791ff4-003507ad/003507adc29ff9676395cfc7a09affa9.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/anaconda-cuda/latest/2020-10-11-27791ff4-003507ad/
recipe: https://datasets.datalad.org/shub/marcc-hpc/anaconda-cuda/latest/2020-10-11-27791ff4-003507ad/Singularity
collection: marcc-hpc/anaconda-cuda
---

# marcc-hpc/anaconda-cuda:latest

```bash
$ singularity pull shub://marcc-hpc/anaconda-cuda:latest
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
  apt-get install -y wget git vim build-essential cmake

  # creates a build directory
  mkdir build
  cd build

  # download and install Anaconda
  CONDA_INSTALL_PATH="/usr/local/anaconda3"
  wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
  chmod +x Anaconda3-5.0.1-Linux-x86_64.sh
  ./Anaconda3-5.0.1-Linux-x86_64.sh -b -p $CONDA_INSTALL_PATH

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [marcc-hpc/anaconda-cuda](https://github.com/marcc-hpc/anaconda-cuda)
 - License: [MIT License](https://api.github.com/licenses/mit)

