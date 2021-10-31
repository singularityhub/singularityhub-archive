---
id: 8690
name: "marcc-hpc/tensorflow"
branch: "master"
tag: "2.0.0a0-gpu-py3"
commit: "40865f40d39231bc934d5e9f3b382f3801630f52"
version: "c70fde3c2d8934bf668ad3eba5f888df"
build_date: "2020-06-11T19:56:50.656Z"
size_mb: 3488
size: 1791176735
sif: "https://datasets.datalad.org/shub/marcc-hpc/tensorflow/2.0.0a0-gpu-py3/2020-06-11-40865f40-c70fde3c/c70fde3c2d8934bf668ad3eba5f888df.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/2.0.0a0-gpu-py3/2020-06-11-40865f40-c70fde3c/
recipe: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/2.0.0a0-gpu-py3/2020-06-11-40865f40-c70fde3c/Singularity
collection: marcc-hpc/tensorflow
---

# marcc-hpc/tensorflow:2.0.0a0-gpu-py3

```bash
$ singularity pull shub://marcc-hpc/tensorflow:2.0.0a0-gpu-py3
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
  apt-get install -y python-tk
  apt-get install -y libsm6 libxext6
  pip install selenium
  pip install moviepy
  pip install lmdb
  pip install opencv-contrib-python
  pip install cryptography

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [marcc-hpc/tensorflow](https://github.com/marcc-hpc/tensorflow)
 - License: [MIT License](https://api.github.com/licenses/mit)

