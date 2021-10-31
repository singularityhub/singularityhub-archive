---
id: 4107
name: "marcc-hpc/tensorflow"
branch: "1.10.0-gpu"
tag: "1.10.0-gpu"
commit: "dec0c1b2586676d605ecc49283b3f0b60b6fbd8f"
version: "ed4bfcd30c213446802cf822326f15ca"
build_date: "2019-08-25T20:43:49.937Z"
size_mb: 3215
size: 1546977311
sif: "https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.10.0-gpu/2019-08-25-dec0c1b2-ed4bfcd3/ed4bfcd30c213446802cf822326f15ca.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.10.0-gpu/2019-08-25-dec0c1b2-ed4bfcd3/
recipe: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.10.0-gpu/2019-08-25-dec0c1b2-ed4bfcd3/Singularity
collection: marcc-hpc/tensorflow
---

# marcc-hpc/tensorflow:1.10.0-gpu

```bash
$ singularity pull shub://marcc-hpc/tensorflow:1.10.0-gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.10.0-gpu

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

