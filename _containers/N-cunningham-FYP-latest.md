---
id: 7779
name: "N-cunningham/FYP"
branch: "master"
tag: "latest"
commit: "11a124e3a0e1ebbe800e10e16ba7746fe41da13b"
version: "2c0fb76c72f26942065d3a8e4bb56ac5"
build_date: "2019-03-26T16:54:25.213Z"
size_mb: 3041
size: 1407197215
sif: "https://datasets.datalad.org/shub/N-cunningham/FYP/latest/2019-03-26-11a124e3-2c0fb76c/2c0fb76c72f26942065d3a8e4bb56ac5.simg"
url: https://datasets.datalad.org/shub/N-cunningham/FYP/latest/2019-03-26-11a124e3-2c0fb76c/
recipe: https://datasets.datalad.org/shub/N-cunningham/FYP/latest/2019-03-26-11a124e3-2c0fb76c/Singularity
collection: N-cunningham/FYP
---

# N-cunningham/FYP:latest

```bash
$ singularity pull shub://N-cunningham/FYP:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.9.0-gpu-py3

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
  apt-get install -y python3-numpy python3-scipy
  apt-get install -y python3-pip python3-dev build-essential
  apt-get install python3-tk


  pip install scikit-learn
  pip install nltk
  pip install matplotlib

%runscript
  RUN python -m nltk.downloader punkt
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [N-cunningham/FYP](https://github.com/N-cunningham/FYP)
 - License: None

