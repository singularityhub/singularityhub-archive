---
id: 3172
name: "adam2392/deeplearning_hubs"
branch: "keras"
tag: "keras"
commit: "b3c6da273331ee6680c694a5f43ebd8bba7be247"
version: "691b7e56d1d63571dc263d31d05fd98d"
build_date: "2018-06-13T15:01:49.023Z"
size_mb: 3159
size: 1438539807
sif: "https://datasets.datalad.org/shub/adam2392/deeplearning_hubs/keras/2018-06-13-b3c6da27-691b7e56/691b7e56d1d63571dc263d31d05fd98d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/adam2392/deeplearning_hubs/keras/2018-06-13-b3c6da27-691b7e56/
recipe: https://datasets.datalad.org/shub/adam2392/deeplearning_hubs/keras/2018-06-13-b3c6da27-691b7e56/Singularity
collection: adam2392/deeplearning_hubs
---

# adam2392/deeplearning_hubs:keras

```bash
$ singularity pull shub://adam2392/deeplearning_hubs:keras
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.8.0-gpu-py3

%environment
  # use bash as default shell
  SHELL=/bin/bash
  export SHELL

  # add CUDA paths
  CPATH="/usr/local/cuda/include:$CPATH"
  PATH="/usr/local/cuda/bin:$PATH"
  LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"
  CUDA_HOME="/usr/local/cuda"
  export CPATH PATH LD_LIBRARY_PATH CUDA_HOME
  
  # make conda accessible
  PATH=/opt/conda/envs/pytorch-py3.6/bin:$PATH
  export PATH

%setup
  # runs on host - the path to the image is $SINGULARITY_ROOTFS

%post
  # post-setup script

  # load environment variables
  . /environment

  # use bash as default shell
  echo 'SHELL=/bin/bash' >> /environment

  # make environment file executable
  chmod +x /environment

  # default mount paths
  mkdir /scratch /data /work-zfs 
  touch /usr/bin/nvidia-smi

  # user requests (contact marcc-help@marcc.jhu.edu)
  # load in extra packages for python
  apt-get update && apt-get -y install locales
  locale-gen en_US.UTF-8
  apt-get install -y git wget python3-dev python3-pip
  apt-get clean

  apt-get install -y libcupti-dev
  pip install --upgrade pip
  pip install keras
  pip install numpy scipy scikit-learn pandas 
  pip install pytest tensorboard scikit-image spectrum nibabel tqdm
  
%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [adam2392/deeplearning_hubs](https://github.com/adam2392/deeplearning_hubs)
 - License: [Other](None)

