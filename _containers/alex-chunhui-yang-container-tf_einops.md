---
id: 15862
name: "alex-chunhui-yang/container"
branch: "master"
tag: "tf_einops"
commit: "968bcbc2986d57352ddd6c2fa6b808acb2c09100"
version: "da07ad299800ff3bb98d9619335595a94121b632f9b7302b0c7efaa322e85f91"
build_date: "2021-04-04T23:08:49.085Z"
size_mb: 4370.3984375
size: 4582694912
sif: "https://datasets.datalad.org/shub/alex-chunhui-yang/container/tf_einops/2021-04-04-968bcbc2-da07ad29/da07ad299800ff3bb98d9619335595a94121b632f9b7302b0c7efaa322e85f91.sif"
url: https://datasets.datalad.org/shub/alex-chunhui-yang/container/tf_einops/2021-04-04-968bcbc2-da07ad29/
recipe: https://datasets.datalad.org/shub/alex-chunhui-yang/container/tf_einops/2021-04-04-968bcbc2-da07ad29/Singularity
collection: alex-chunhui-yang/container
---

# alex-chunhui-yang/container:tf_einops

```bash
$ singularity pull shub://alex-chunhui-yang/container:tf_einops
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
  pip install einops

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [alex-chunhui-yang/container](https://github.com/alex-chunhui-yang/container)
 - License: None

