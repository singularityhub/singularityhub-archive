---
id: 1848
name: "marcc-hpc/tensorflow"
branch: "1.4.0-gpu"
tag: "1.4.0-gpu"
commit: "0ac18adfacb839557cb1fcd6cf6fbd052c5e896a"
version: "067a0963340cad28f66ff3c9c21a88b6"
build_date: "2018-05-06T20:20:26.904Z"
size_mb: 3254
size: 1550139423
sif: "https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.4.0-gpu/2018-05-06-0ac18adf-067a0963/067a0963340cad28f66ff3c9c21a88b6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/marcc-hpc/tensorflow/1.4.0-gpu/2018-05-06-0ac18adf-067a0963/
recipe: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.4.0-gpu/2018-05-06-0ac18adf-067a0963/Singularity
collection: marcc-hpc/tensorflow
---

# marcc-hpc/tensorflow:1.4.0-gpu

```bash
$ singularity pull shub://marcc-hpc/tensorflow:1.4.0-gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.4.0-gpu

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

