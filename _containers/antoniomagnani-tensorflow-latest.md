---
id: 7442
name: "antoniomagnani/tensorflow"
branch: "master"
tag: "latest"
commit: "e760bee866eff8f8a486d509373d672249c639f9"
version: "566e6f67a506d8692a2d9ddbfa91c257"
build_date: "2019-02-25T20:22:55.922Z"
size_mb: 3205
size: 1547288607
sif: "https://datasets.datalad.org/shub/antoniomagnani/tensorflow/latest/2019-02-25-e760bee8-566e6f67/566e6f67a506d8692a2d9ddbfa91c257.simg"
url: https://datasets.datalad.org/shub/antoniomagnani/tensorflow/latest/2019-02-25-e760bee8-566e6f67/
recipe: https://datasets.datalad.org/shub/antoniomagnani/tensorflow/latest/2019-02-25-e760bee8-566e6f67/Singularity
collection: antoniomagnani/tensorflow
---

# antoniomagnani/tensorflow:latest

```bash
$ singularity pull shub://antoniomagnani/tensorflow:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.10.1-gpu

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

 - Name: [antoniomagnani/tensorflow](https://github.com/antoniomagnani/tensorflow)
 - License: [MIT License](https://api.github.com/licenses/mit)

