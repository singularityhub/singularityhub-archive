---
id: 10040
name: "shreyaskamathkm/Singularity"
branch: "v1.14"
tag: "latest"
commit: "bcdb82883b71a724656d04a86174ecb7a9d34b82"
version: "e5c647b6220e97c665c0b025997b3c24"
build_date: "2019-06-26T22:56:22.144Z"
size_mb: 9462
size: 4574941215
sif: "https://datasets.datalad.org/shub/shreyaskamathkm/Singularity/latest/2019-06-26-bcdb8288-e5c647b6/e5c647b6220e97c665c0b025997b3c24.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/shreyaskamathkm/Singularity/latest/2019-06-26-bcdb8288-e5c647b6/
recipe: https://datasets.datalad.org/shub/shreyaskamathkm/Singularity/latest/2019-06-26-bcdb8288-e5c647b6/Singularity
collection: shreyaskamathkm/Singularity
---

# shreyaskamathkm/Singularity:latest

```bash
$ singularity pull shub://shreyaskamathkm/Singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: shreyaskamathkm/nvidia_v10_python_3.7:latest

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
  /opt/conda/bin/conda update -y --all
  /opt/conda/bin/conda install pytorch torchvision cudatoolkit=10.0 -c pytorch
  /opt/conda/bin/conda install graphviz
  /opt/conda/bin/conda clean -ya
  
  pip install --upgrade pip
  pip install natsort
  pip install tensorflow-gpu
  pip install albumentations
  pip uninstall -y opencv-python-headless
  pip install opencv-python
  pip install opencv-contrib-python
  pip install tensorboardX
  pip install deepdish
  pip install PyContracts

  
%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [shreyaskamathkm/Singularity](https://github.com/shreyaskamathkm/Singularity)
 - License: None

