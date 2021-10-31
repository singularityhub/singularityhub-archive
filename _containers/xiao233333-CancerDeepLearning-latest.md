---
id: 9889
name: "xiao233333/CancerDeepLearning"
branch: "master"
tag: "latest"
commit: "9cda6e6fe8da886c0c066b86d736e4a6d1185b9a"
version: "1d4420149584e7e1fb774b082aad6985"
build_date: "2019-06-25T05:49:27.539Z"
size_mb: 4720
size: 2419372063
sif: "https://datasets.datalad.org/shub/xiao233333/CancerDeepLearning/latest/2019-06-25-9cda6e6f-1d442014/1d4420149584e7e1fb774b082aad6985.simg"
url: https://datasets.datalad.org/shub/xiao233333/CancerDeepLearning/latest/2019-06-25-9cda6e6f-1d442014/
recipe: https://datasets.datalad.org/shub/xiao233333/CancerDeepLearning/latest/2019-06-25-9cda6e6f-1d442014/Singularity
collection: xiao233333/CancerDeepLearning
---

# xiao233333/CancerDeepLearning:latest

```bash
$ singularity pull shub://xiao233333/CancerDeepLearning:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:2.0.0a0-gpu-py3

%environment
  # use bash as default shell
  SHELL=/bin/bash
  export SHELL

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
  mkdir /scratch /data 

  # additional packages
  apt-get update
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils
  apt-get install -y build-essential checkinstall wget swig monodevelop r-base r-base-dev ruby ruby-dev python3 python3-dev tcl tcl-dev tk tk-dev
  apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
  apt-get install -y git vim
  apt-get install -y openslide-tools
  apt-get install -y libsm6 libxext6
  apt-get install -y python3-tk python3-pip
  python3 -m pip install --upgrade pip
  python3 -m pip install opencv-python
  python3 -m pip install openslide-python
  python3 -m pip install numpy scipy matplotlib ipython jupyter pandas sympy nose pydicom dicom
  python3 -m pip install tensorflow==2.0.0-alpha0 
  python3 -m pip install keras pydot graphviz
  python3 -m pip install scikit-learn scikit-image
  python3 -m pip install xgboost minecart quilt
  quilt install ResidentMario/missingno_data

  apt-get clean
%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [xiao233333/CancerDeepLearning](https://github.com/xiao233333/CancerDeepLearning)
 - License: None

