---
id: 12144
name: "fcatus/hcc"
branch: "master"
tag: "py3-pytorch"
commit: "fff1c40d99dcdcdb3b03d249eb95c81bb3f69337"
version: "bf2802e1224bc9ab1fd5c067ac10ca622a128655a4943f612b88fb96da458e10"
build_date: "2020-01-31T22:50:15.803Z"
size_mb: 4045.62109375
size: 4242141184
sif: "https://datasets.datalad.org/shub/fcatus/hcc/py3-pytorch/2020-01-31-fff1c40d-bf2802e1/bf2802e1224bc9ab1fd5c067ac10ca622a128655a4943f612b88fb96da458e10.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/fcatus/hcc/py3-pytorch/2020-01-31-fff1c40d-bf2802e1/
recipe: https://datasets.datalad.org/shub/fcatus/hcc/py3-pytorch/2020-01-31-fff1c40d-bf2802e1/Singularity
collection: fcatus/hcc
---

# fcatus/hcc:py3-pytorch

```bash
$ singularity pull shub://fcatus/hcc:py3-pytorch
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
  apt-get install -y ffmpeg
  apt-get install -y sudo
  apt-get install -y zsh
  
  # creates a build directory
  mkdir build
  cd build

  # download and install Anaconda
  CONDA_INSTALL_PATH="/usr/local/anaconda3"
  wget https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh
  chmod +x Anaconda3-2019.07-Linux-x86_64.sh
  ./Anaconda3-2019.07-Linux-x86_64.sh -b -p $CONDA_INSTALL_PATH

  #install pytorch
  /usr/local/anaconda3/bin/conda install pytorch torchvision cudatoolkit=10.0 -c pytorch
  
  #install nice stuff
  /usr/local/anaconda3/bin/conda install -y numba bcolz networkx dask seaborn pandas numexpr unidecode
  
  #install boolean network stuff
  /usr/local/anaconda3/bin/pip install -U dynpy cana
  
  #install other pip stuff
  /usr/local/anaconda3/bin/pip install fastai matplotlib graphillion

  #install hyperlearn
  #git clone https://github.com/danielhanchen/hyperlearn.git
  #cd hyperlearn
  #/usr/local/anaconda3/bin/python setup.py 

  #install graphblas
  #git clone --recursive https://github.com/gunrock/graphblast.git
  #cd graphblast
  #mkdir build
  #cd build
  #cmake ..
  #make -j$(nproc)

  #conda cleanup
  /usr/local/anaconda3/bin/conda clean -ya

  #apt cleanup
  #apt-get autoremove -y
  #%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [fcatus/hcc](https://github.com/fcatus/hcc)
 - License: None

