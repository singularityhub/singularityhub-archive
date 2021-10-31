---
id: 4736
name: "marcc-hpc/tensorflow"
branch: "1.10.1-gpu"
tag: "latest"
commit: "e760bee866eff8f8a486d509373d672249c639f9"
version: "5e9fe752de149c1cbae442599ae0bdec"
build_date: "2021-04-18T21:15:07.310Z"
size_mb: 3199
size: 1544392735
sif: "https://datasets.datalad.org/shub/marcc-hpc/tensorflow/latest/2021-04-18-e760bee8-5e9fe752/5e9fe752de149c1cbae442599ae0bdec.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/latest/2021-04-18-e760bee8-5e9fe752/
recipe: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/latest/2021-04-18-e760bee8-5e9fe752/Singularity
collection: marcc-hpc/tensorflow
---

# marcc-hpc/tensorflow:latest

```bash
$ singularity pull shub://marcc-hpc/tensorflow:latest
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

 - Name: [marcc-hpc/tensorflow](https://github.com/marcc-hpc/tensorflow)
 - License: [MIT License](https://api.github.com/licenses/mit)

