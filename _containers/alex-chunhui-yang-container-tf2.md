---
id: 14317
name: "alex-chunhui-yang/container"
branch: "master"
tag: "tf2"
commit: "5339801313aba2095f3646a1839bc9a54985b299"
version: "35dc0245554bd4d2948ef0453c00d3e672db03c3e9511b6ea850dcf2eacd5bbc"
build_date: "2020-09-25T03:44:31.290Z"
size_mb: 2436.59375
size: 2554953728
sif: "https://datasets.datalad.org/shub/alex-chunhui-yang/container/tf2/2020-09-25-53398013-35dc0245/35dc0245554bd4d2948ef0453c00d3e672db03c3e9511b6ea850dcf2eacd5bbc.sif"
url: https://datasets.datalad.org/shub/alex-chunhui-yang/container/tf2/2020-09-25-53398013-35dc0245/
recipe: https://datasets.datalad.org/shub/alex-chunhui-yang/container/tf2/2020-09-25-53398013-35dc0245/Singularity
collection: alex-chunhui-yang/container
---

# alex-chunhui-yang/container:tf2

```bash
$ singularity pull shub://alex-chunhui-yang/container:tf2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:2.0.0-gpu-py3


# adapted from: https://github.com/marcc-hpc/tensorflow

%environment
  # use bash as default shell
  SHELL=/bin/bash
  export SHELL
  export HDF5_USE_FILE_LOCKING='FALSE'

%setup
  # runs on host
  # the path to the image is $SINGULARITY_ROOTFS

%post
  # post-setup script

  # load environment variables
  . /environment

  # use bash as default shell
  echo 'SHELL=/bin/bash' >> /environment

  # make environment file executable
  chmod +x /environment

  # default mount paths
  mkdir /scratch

  # fix this issue: https://github.com/singularityware/singularity/issues/1182#issuecomment-381796545
  touch /usr/bin/nvidia-smi

  apt-get update && apt-get -y install locales
  locale-gen en_US.UTF-8
  apt-get install -y git wget
  apt-get clean

  # scikit, scipy
  apt-get install -y python3-scipy
  apt-get install -y python3-sklearn 
  apt-get install -y python3-sklearn-lib

  # PIL (pillow for python 3)
  #python3-dev python3-pip python3-tk cmake
  pip install Pillow
  pip install matplotlib

  # SimpleITK
  pip install simpleitk
  
  #comet
  pip install comet_ml
  
  #pandas
  pip install pandas
  pip install spektral
  
  #pip install tables #pytables
  #pip install nilearn
  #pip install nibabel

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [alex-chunhui-yang/container](https://github.com/alex-chunhui-yang/container)
 - License: None

