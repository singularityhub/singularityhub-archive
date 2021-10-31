---
id: 1994
name: "gdhugo/coral_singularity"
branch: "master"
tag: "latest"
commit: "227504c4f3ea6342e94d3367e2f294b2bfc24399"
version: "2dfdd28496c888e17e97d6c43a038692"
build_date: "2019-11-13T17:19:30.510Z"
size_mb: 3313
size: 1628545055
sif: "https://datasets.datalad.org/shub/gdhugo/coral_singularity/latest/2019-11-13-227504c4-2dfdd284/2dfdd28496c888e17e97d6c43a038692.simg"
url: https://datasets.datalad.org/shub/gdhugo/coral_singularity/latest/2019-11-13-227504c4-2dfdd284/
recipe: https://datasets.datalad.org/shub/gdhugo/coral_singularity/latest/2019-11-13-227504c4-2dfdd284/Singularity
collection: gdhugo/coral_singularity
---

# gdhugo/coral_singularity:latest

```bash
$ singularity pull shub://gdhugo/coral_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.12.0-gpu-py3

# adapted from: https://github.com/marcc-hpc/tensorflow

%environment
  # use bash as default shell
  SHELL=/bin/bash
  export SHELL

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

  # keras - still use standalone keras, rather than tf.keras

  apt-get update && apt-get -y install locales
  locale-gen en_US.UTF-8
  apt-get install -y git wget
  # python3-dev python3-pip python3-tk
  apt-get clean

  # apt-get install -y libcupti-dev
  # pip3 install --upgrade
  # pip3 install keras

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [gdhugo/coral_singularity](https://github.com/gdhugo/coral_singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

