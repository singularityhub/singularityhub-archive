---
id: 1846
name: "marcc-hpc/tensorflow"
branch: "1.5.0-gpu"
tag: "1.5.0-gpu"
commit: "fdbdb02129b5c8cbbb88ba0bf7b6bfe47a2cd7bf"
version: "c7a6e8c0d46ac4c77fbd26184c063ddd"
build_date: "2018-02-23T19:46:44.038Z"
size_mb: 2807
size: 1154424863
sif: "https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.5.0-gpu/2018-02-23-fdbdb021-c7a6e8c0/c7a6e8c0d46ac4c77fbd26184c063ddd.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.5.0-gpu/2018-02-23-fdbdb021-c7a6e8c0/
recipe: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.5.0-gpu/2018-02-23-fdbdb021-c7a6e8c0/Singularity
collection: marcc-hpc/tensorflow
---

# marcc-hpc/tensorflow:1.5.0-gpu

```bash
$ singularity pull shub://marcc-hpc/tensorflow:1.5.0-gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.5.0-gpu

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

