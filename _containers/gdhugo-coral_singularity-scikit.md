---
id: 4747
name: "gdhugo/coral_singularity"
branch: "master"
tag: "scikit"
commit: "227504c4f3ea6342e94d3367e2f294b2bfc24399"
version: "6be085fb5f6b82160f3fa2c68e7e079e"
build_date: "2018-11-26T17:12:51.770Z"
size_mb: 3662
size: 1781964831
sif: "https://datasets.datalad.org/shub/gdhugo/coral_singularity/scikit/2018-11-26-227504c4-6be085fb/6be085fb5f6b82160f3fa2c68e7e079e.simg"
url: https://datasets.datalad.org/shub/gdhugo/coral_singularity/scikit/2018-11-26-227504c4-6be085fb/
recipe: https://datasets.datalad.org/shub/gdhugo/coral_singularity/scikit/2018-11-26-227504c4-6be085fb/Singularity
collection: gdhugo/coral_singularity
---

# gdhugo/coral_singularity:scikit

```bash
$ singularity pull shub://gdhugo/coral_singularity:scikit
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
  # python3-dev python3-pip python3-tk cmake
  apt-get clean

  # apt-get install -y libcupti-dev
  # pip3 install --upgrade
  # pip3 install keras

  # scikit, scipy
  pip3 install --upgrade scipy scikit-learn scikit-image

  # SimpleITK
  pip3 install --upgrade simpleitk

  # TODO: SimpleElastix
  # git clone https://github.com/SuperElastix/SimpleElastix
  # mkdir SimpleElastix.build
  # cd SimpleElastix.build
  # #cmake ../SimpleElastix/SuperBuild
  # cmake -DWRAP_CSHARP:BOOL=OFF -DWRAP_JAVA:BOOL=OFF -DWRAP_LUA:BOOL=OFF -DWRAP_PYTHON:BOOL=ON -DWRAP_R:BOOL=OFF -DWRAP_RUBY:BOOL=OFF -DWRAP_TCL=BOOL=OFF ../SimpleElastix/SuperBuild
  # #make
  # make >/dev/null --jobs=4
  # cd SimpleITK-build/Wrapping/Python/Packaging
  # python setup.py --upgrade install

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [gdhugo/coral_singularity](https://github.com/gdhugo/coral_singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

