---
id: 9092
name: "gdhugo/coral_singularity"
branch: "master"
tag: "1p13p1"
commit: "85af020ca0edb42448d3e158456c47b76d73787b"
version: "eca176a72bd5655857ada86d22067db7"
build_date: "2019-05-22T09:03:46.054Z"
size_mb: 3765
size: 1828061215
sif: "https://datasets.datalad.org/shub/gdhugo/coral_singularity/1p13p1/2019-05-22-85af020c-eca176a7/eca176a72bd5655857ada86d22067db7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/gdhugo/coral_singularity/1p13p1/2019-05-22-85af020c-eca176a7/
recipe: https://datasets.datalad.org/shub/gdhugo/coral_singularity/1p13p1/2019-05-22-85af020c-eca176a7/Singularity
collection: gdhugo/coral_singularity
---

# gdhugo/coral_singularity:1p13p1

```bash
$ singularity pull shub://gdhugo/coral_singularity:1p13p1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.13.1-gpu-py3

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
  # pip3 install scipy scikit-learn scikit-image

  # PIL (pillow for python 3)
  #python3-dev python3-pip python3-tk cmake
  pip install Pillow
  pip install matplotlib

  # SimpleITK
  pip install simpleitk

  # for Xiaoxiao
  pip install tables #pytables
  pip install nilearn
  pip install nibabel

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

