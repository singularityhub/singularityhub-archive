---
id: 8123
name: "TurbulentDynamics/TD_env_setup_dev_info"
branch: "master"
tag: "td_base_ml"
commit: "73d53fb355bf1d30bbbb8331184caa967e3dea00"
version: "9dd084ae6dad59de5184ac881941f3ff"
build_date: "2019-06-19T16:10:35.568Z"
size_mb: 8939
size: 5311082527
sif: "https://datasets.datalad.org/shub/TurbulentDynamics/TD_env_setup_dev_info/td_base_ml/2019-06-19-73d53fb3-9dd084ae/9dd084ae6dad59de5184ac881941f3ff.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TurbulentDynamics/TD_env_setup_dev_info/td_base_ml/2019-06-19-73d53fb3-9dd084ae/
recipe: https://datasets.datalad.org/shub/TurbulentDynamics/TD_env_setup_dev_info/td_base_ml/2019-06-19-73d53fb3-9dd084ae/Singularity
collection: TurbulentDynamics/TD_env_setup_dev_info
---

# TurbulentDynamics/TD_env_setup_dev_info:td_base_ml

```bash
$ singularity pull shub://TurbulentDynamics/TD_env_setup_dev_info:td_base_ml
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: docker://nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04

%labels
  MAINTAINER Turbulent Dynamics

%environment
  # build time environment
  SHELL=/bin/bash
  export SHELL
  
%setup
  # runs on host - the path to the image is $SINGULARITY_ROOTFS

%post
  # post-setup script

  # additional packages
  apt update
  apt install -y curl wget vim clang libicu-dev 

  # Install Apple Swift
  wget -nc https://swift.org/builds/swift-4.2.3-release/ubuntu1604/swift-4.2.3-RELEASE/swift-4.2.3-RELEASE-ubuntu16.04.tar.gz
  tar xzf swift-4.2.3-RELEASE-ubuntu16.04.tar.gz -C /opt
  echo 'export PATH=/opt/swift-4.2.3-RELEASE-ubuntu16.04/usr/bin:${PATH}' >>$SINGULARITY_ENVIRONMENT

  # Install any needed python packages
  apt install -y python3 python3-dev
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python3 get-pip.py
  pip3 install tensorflow-gpu

  pip3 install --trusted-host pypi.python.org matplotlib pandas dask pillow keras
  pip3 install https://download.pytorch.org/whl/cu100/torch-1.0.1.post2-cp35-cp35m-linux_x86_64.whl
  pip3 install torchvision


%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command
  alias ll='ls -l'
  alias python=python3

%test
  # test that script is a success
  #python3 -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"
```

## Collection

 - Name: [TurbulentDynamics/TD_env_setup_dev_info](https://github.com/TurbulentDynamics/TD_env_setup_dev_info)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

