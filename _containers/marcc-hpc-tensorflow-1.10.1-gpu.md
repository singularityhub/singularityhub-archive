---
id: 4737
name: "marcc-hpc/tensorflow"
branch: "1.10.1-gpu"
tag: "1.10.1-gpu"
commit: "e760bee866eff8f8a486d509373d672249c639f9"
version: "cc8406dbe9689ab5efc2622bf2456807"
build_date: "2018-09-10T04:18:53.013Z"
size_mb: 3199
size: 1544396831
sif: "https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.10.1-gpu/2018-09-10-e760bee8-cc8406db/cc8406dbe9689ab5efc2622bf2456807.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.10.1-gpu/2018-09-10-e760bee8-cc8406db/
recipe: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.10.1-gpu/2018-09-10-e760bee8-cc8406db/Singularity
collection: marcc-hpc/tensorflow
---

# marcc-hpc/tensorflow:1.10.1-gpu

```bash
$ singularity pull shub://marcc-hpc/tensorflow:1.10.1-gpu
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

