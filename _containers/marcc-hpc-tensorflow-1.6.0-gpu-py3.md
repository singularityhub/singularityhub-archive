---
id: 1903
name: "marcc-hpc/tensorflow"
branch: "1.6.0-gpu-py3"
tag: "1.6.0-gpu-py3"
commit: "e5ff4558e67c32f61e5a727741143a24991436c1"
version: "22f22c81fcfcc9cdf00dc2c7de48e380"
build_date: "2018-03-01T21:03:57.753Z"
size_mb: 2907
size: 1210064927
sif: "https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.6.0-gpu-py3/2018-03-01-e5ff4558-22f22c81/22f22c81fcfcc9cdf00dc2c7de48e380.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/marcc-hpc/tensorflow/1.6.0-gpu-py3/2018-03-01-e5ff4558-22f22c81/
recipe: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.6.0-gpu-py3/2018-03-01-e5ff4558-22f22c81/Singularity
collection: marcc-hpc/tensorflow
---

# marcc-hpc/tensorflow:1.6.0-gpu-py3

```bash
$ singularity pull shub://marcc-hpc/tensorflow:1.6.0-gpu-py3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.6.0-gpu-py3

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

