---
id: 14480
name: "cyang31/containers"
branch: "master"
tag: "ubuntu_tf"
commit: "30fa3bd66997b1541ef076e9614b45b23726a3f3"
version: "56ef8a3999947f583ac3597a9d28712aa6211da3b7be15179cdcd98515c7f323"
build_date: "2021-04-04T22:43:36.033Z"
size_mb: 4388.8125
size: 4602003456
sif: "https://datasets.datalad.org/shub/cyang31/containers/ubuntu_tf/2021-04-04-30fa3bd6-56ef8a39/56ef8a3999947f583ac3597a9d28712aa6211da3b7be15179cdcd98515c7f323.sif"
url: https://datasets.datalad.org/shub/cyang31/containers/ubuntu_tf/2021-04-04-30fa3bd6-56ef8a39/
recipe: https://datasets.datalad.org/shub/cyang31/containers/ubuntu_tf/2021-04-04-30fa3bd6-56ef8a39/Singularity
collection: cyang31/containers
---

# cyang31/containers:ubuntu_tf

```bash
$ singularity pull shub://cyang31/containers:ubuntu_tf
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:2.3.0-custom-op-gpu-ubuntu16

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
  apt-get install -y python3-scipy python3-sklearn python3-sklearn-lib

  pip install --upgrade pip
  
  pip uninstall -y numpy
  pip install numpy
  
  #pip install -U scikit-learn
  
  pip install Pillow
  pip install matplotlib
  pip install simpleitk
  pip install comet_ml
  pip install pandas
  pip install tqdm
  pip install h5py
  pip install spektral
  pip install -e git+https://github.com/marcoancona/DeepExplain.git#egg=deepexplain
  pip install tf-explain
  pip install tensorflow-addons
  pip install imgaug
  #pip install einops

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [cyang31/containers](https://github.com/cyang31/containers)
 - License: None

