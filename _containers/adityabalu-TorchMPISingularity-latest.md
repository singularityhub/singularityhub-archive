---
id: 8266
name: "adityabalu/TorchMPISingularity"
branch: "master"
tag: "latest"
commit: "e16af9a44067041b90a93849258e419db712ae88"
version: "c974f0b1bd6824a8f9e1201512f2772b"
build_date: "2020-03-21T19:54:17.831Z"
size_mb: 8396
size: 3913941023
sif: "https://datasets.datalad.org/shub/adityabalu/TorchMPISingularity/latest/2020-03-21-e16af9a4-c974f0b1/c974f0b1bd6824a8f9e1201512f2772b.simg"
url: https://datasets.datalad.org/shub/adityabalu/TorchMPISingularity/latest/2020-03-21-e16af9a4-c974f0b1/
recipe: https://datasets.datalad.org/shub/adityabalu/TorchMPISingularity/latest/2020-03-21-e16af9a4-c974f0b1/Singularity
collection: adityabalu/TorchMPISingularity
---

# adityabalu/TorchMPISingularity:latest

```bash
$ singularity pull shub://adityabalu/TorchMPISingularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04

%environment

  # use bash as default shell
  SHELL=/bin/bash

  # add CUDA paths
  CPATH="/usr/local/cuda/include:$CPATH"
  PATH="/usr/local/cuda/bin:$PATH"
  LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"
  CUDA_HOME="/usr/local/cuda"

  # add Anaconda path
  PATH="/usr/local/miniconda3/bin:$PATH"

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
  echo 'export PATH="/usr/local/cuda/bin:/usr/openmpi/bin:$PATH"' >> /environment
  echo 'export LD_LIBRARY_PATH="/usr/local/cuda/lib64:/usr/openmpi/lib:$LD_LIBRARY_PATH"' >> /environment
  echo 'export CUDA_HOME="/usr/local/cuda"' >> /environment

  # updating and getting required packages
  apt-get update
  apt-get install -y software-properties-common
  add-apt-repository main
  add-apt-repository universe
  add-apt-repository restricted
  add-apt-repository multiverse
  apt-get update
  apt-get install -y wget git vim build-essential cmake
  apt-get autoremove -y && apt-get clean


  # creates a build directory
  mkdir build
  cd build

  # download and install Anaconda
  CONDA_INSTALL_PATH="/usr/local/miniconda3"
  wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
  chmod +x Miniconda3-latest-Linux-x86_64.sh
  ./Miniconda3-latest-Linux-x86_64.sh -b -p $CONDA_INSTALL_PATH
  conda install python=3.6 pip cudatoolkit cudnn numba
  conda clean --tarballs
  wget -O openmpi.tar.gz  https://www.open-mpi.org/software/ompi/v4.0/downloads/openmpi-4.0.0.tar.gz
  tar xvzf openmpi.tar.gz && rm openmpi.tar.gz
  ls
  cd openmpi-4.0.0 && ./configure --prefix=/usr/openmpi && make all install
  PATH="$PATH:/home/usr/openmpi/bin"
  LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/home/usr/openmpi/lib/"

  conda clean --tarballs
  pip --no-cache-dir install \
            h5py \
            ipykernel \
            jupyter \
            matplotlib \
            numpy \
            pandas \
            Pillow \
            scipy \
            sklearn \
            python-utils \
            requests \
            future \
            hypothesis \
            scikit-learn \
            scikit-image \
            visdom \
            tqdm
  #          mpi4py
  conda install -c conda-forge/label/cf201901 opencv 
  conda clean --tarballs
  conda install numpy pyyaml mkl mkl-include setuptools cmake cffi typing
  conda clean --tarballs
  #git clone --recursive -b v1.0.0 https://github.com/pytorch/pytorch
  #CMAKE_PREFIX_PATH=$CONDA_INSTALL_PATH/bin
  #cd pytorch && python setup.py install

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [adityabalu/TorchMPISingularity](https://github.com/adityabalu/TorchMPISingularity)
 - License: None

