---
id: 8724
name: "TheRevanchist/sing-pytorch"
branch: "master"
tag: "latest"
commit: "3df7cd2e555db27a8e73ea1d9312dbdb4362d8ca"
version: "83c997d3da13e0acf0b540f776d62d7b"
build_date: "2019-04-30T20:21:09.572Z"
size_mb: 9641
size: 4877369375
sif: "https://datasets.datalad.org/shub/TheRevanchist/sing-pytorch/latest/2019-04-30-3df7cd2e-83c997d3/83c997d3da13e0acf0b540f776d62d7b.simg"
url: https://datasets.datalad.org/shub/TheRevanchist/sing-pytorch/latest/2019-04-30-3df7cd2e-83c997d3/
recipe: https://datasets.datalad.org/shub/TheRevanchist/sing-pytorch/latest/2019-04-30-3df7cd2e-83c997d3/Singularity
collection: TheRevanchist/sing-pytorch
---

# TheRevanchist/sing-pytorch:latest

```bash
$ singularity pull shub://TheRevanchist/sing-pytorch:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: shreyaskamathkm/deeplearning


%environment
  # use bash as default shell
  SHELL=/bin/bash
  export SHELL
  PATH="/opt/conda/bin:$PATH"
  export PATH


%setup
  # runs on host - the path to the image is $SINGULARITY_ROOTFS

%post
  # post-setup script
  apt update && apt install -y libsm6 libxext6
  apt-get install -y libxrender-dev
  # load environment variables
  . /environment

  # make environment file executable
  mkdir /data
  chmod +x /environment

  # default mount paths, files
  touch /usr/bin/nvidia-smi
  
  # user requests 
  /opt/conda/bin/conda install -c anaconda python=3.6
  /opt/conda/bin/conda install -c conda-forge onnx spectrum nibabel
  /opt/conda/bin/conda update -y --all
  /opt/conda/bin/conda install pytorch torchvision cudatoolkit=10.0 -c pytorch
  /opt/conda/bin/conda clean -ya
  
  pip install --upgrade pip
  pip install natsort
  pip install opencv-python
  pip install opencv-contrib-python
  pip install deepdish
  pip install albumentations
  pip install PyContracts
  pip install easydict
  pip install opencv-python
  pip install numpy scipy scikit-learn
  pip install Cython

  
%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [TheRevanchist/sing-pytorch](https://github.com/TheRevanchist/sing-pytorch)
 - License: None

