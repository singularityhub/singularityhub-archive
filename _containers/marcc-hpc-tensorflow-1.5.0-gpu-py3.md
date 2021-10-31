---
id: 1918
name: "marcc-hpc/tensorflow"
branch: "1.5.0-gpu-py3"
tag: "1.5.0-gpu-py3"
commit: "45f75375a983aa494122ab51c12e70d123e716fe"
version: "430e0ff84070079973ff57e2c851a5f8"
build_date: "2018-03-02T21:00:30.586Z"
size_mb: 2814
size: 1164189727
sif: "https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.5.0-gpu-py3/2018-03-02-45f75375-430e0ff8/430e0ff84070079973ff57e2c851a5f8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/marcc-hpc/tensorflow/1.5.0-gpu-py3/2018-03-02-45f75375-430e0ff8/
recipe: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.5.0-gpu-py3/2018-03-02-45f75375-430e0ff8/Singularity
collection: marcc-hpc/tensorflow
---

# marcc-hpc/tensorflow:1.5.0-gpu-py3

```bash
$ singularity pull shub://marcc-hpc/tensorflow:1.5.0-gpu-py3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.5.0-gpu-py3

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

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [marcc-hpc/tensorflow](https://github.com/marcc-hpc/tensorflow)
 - License: [MIT License](https://api.github.com/licenses/mit)

