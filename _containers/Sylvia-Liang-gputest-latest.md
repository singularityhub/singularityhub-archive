---
id: 5647
name: "Sylvia-Liang/gputest"
branch: "master"
tag: "latest"
commit: "53185b7547f0ba85b261675260da2af9a576b772"
version: "bd46577e4235f9ae5e40458b5a83f659"
build_date: "2019-02-01T19:07:42.938Z"
size_mb: 3081
size: 1417166879
sif: "https://datasets.datalad.org/shub/Sylvia-Liang/gputest/latest/2019-02-01-53185b75-bd46577e/bd46577e4235f9ae5e40458b5a83f659.simg"
url: https://datasets.datalad.org/shub/Sylvia-Liang/gputest/latest/2019-02-01-53185b75-bd46577e/
recipe: https://datasets.datalad.org/shub/Sylvia-Liang/gputest/latest/2019-02-01-53185b75-bd46577e/Singularity
collection: Sylvia-Liang/gputest
---

# Sylvia-Liang/gputest:latest

```bash
$ singularity pull shub://Sylvia-Liang/gputest:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.8.0-gpu

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

 - Name: [Sylvia-Liang/gputest](https://github.com/Sylvia-Liang/gputest)
 - License: None

