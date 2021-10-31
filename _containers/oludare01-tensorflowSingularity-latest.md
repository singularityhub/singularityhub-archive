---
id: 4061
name: "oludare01/tensorflowSingularity"
branch: "master"
tag: "latest"
commit: "f8161ff91642d3c7a49fd1b7dbc1da7fe59e90e9"
version: "d68ceba2d069d2bc242741d2155289f7"
build_date: "2018-08-23T00:50:11.066Z"
size_mb: 8819
size: 4292636703
sif: "https://datasets.datalad.org/shub/oludare01/tensorflowSingularity/latest/2018-08-23-f8161ff9-d68ceba2/d68ceba2d069d2bc242741d2155289f7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/oludare01/tensorflowSingularity/latest/2018-08-23-f8161ff9-d68ceba2/
recipe: https://datasets.datalad.org/shub/oludare01/tensorflowSingularity/latest/2018-08-23-f8161ff9-d68ceba2/Singularity
collection: oludare01/tensorflowSingularity
---

# oludare01/tensorflowSingularity:latest

```bash
$ singularity pull shub://oludare01/tensorflowSingularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: shreyaskamathkm/anaconda-nvidia-cuda:latest


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

  # load environment variables
  . /environment

  # make environment file executable
  mkdir /data
  chmod +x /environment

  # default mount paths, files
  touch /usr/bin/nvidia-smi
  
  # user requests 
  /opt/conda/bin/conda install python=3.6
  /opt/conda/bin/conda install -c anaconda flake8 
  /opt/conda/bin/conda install numpy pyyaml mkl mkl-include setuptools cmake cffi typing
  /opt/conda/bin/conda install -c mingfeima mkldnn
  /opt/conda/bin/conda install -c pytorch magma-cuda90
  /opt/conda/bin/conda install -c conda-forge onnx spectrum nibabel
  /opt/conda/bin/conda update -y --all	
  /opt/conda/bin/conda clean -ya
  pip install --upgrade pip
  pip install --ignore-installed --upgrade tensorflow-gpu 
  pip install keras
  pip install natsort
  pip install torchvision
  pip install opencv-contrib-python
  pip install tensorboardX
  pip install opencv-python
%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
# test that script is a success
```

## Collection

 - Name: [oludare01/tensorflowSingularity](https://github.com/oludare01/tensorflowSingularity)
 - License: None

