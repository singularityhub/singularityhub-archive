---
id: 14690
name: "alex-chunhui-yang/container"
branch: "master"
tag: "ubuntu_tf"
commit: "5a24284f6178c7128b597de84fb66b899e0fa4c4"
version: "200eb3af7690cd3e14fb4281e7ff8067e93338cf447e16bf2a322f1a61aaabca"
build_date: "2021-03-03T07:03:25.679Z"
size_mb: 4383.578125
size: 4596514816
sif: "https://datasets.datalad.org/shub/alex-chunhui-yang/container/ubuntu_tf/2021-03-03-5a24284f-200eb3af/200eb3af7690cd3e14fb4281e7ff8067e93338cf447e16bf2a322f1a61aaabca.sif"
url: https://datasets.datalad.org/shub/alex-chunhui-yang/container/ubuntu_tf/2021-03-03-5a24284f-200eb3af/
recipe: https://datasets.datalad.org/shub/alex-chunhui-yang/container/ubuntu_tf/2021-03-03-5a24284f-200eb3af/Singularity
collection: alex-chunhui-yang/container
---

# alex-chunhui-yang/container:ubuntu_tf

```bash
$ singularity pull shub://alex-chunhui-yang/container:ubuntu_tf
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
  
%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [alex-chunhui-yang/container](https://github.com/alex-chunhui-yang/container)
 - License: None

