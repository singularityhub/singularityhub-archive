---
id: 1905
name: "marcc-hpc/tensorflow"
branch: "1.6.0-gpu"
tag: "1.6.0-gpu"
commit: "a2a550085479edbd379368d021c0bdea218a8e27"
version: "5b3eb8716694bcc7aafe306e496ca4f2"
build_date: "2018-03-01T21:03:57.743Z"
size_mb: 2901
size: 1200451615
sif: "https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.6.0-gpu/2018-03-01-a2a55008-5b3eb871/5b3eb8716694bcc7aafe306e496ca4f2.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.6.0-gpu/2018-03-01-a2a55008-5b3eb871/
recipe: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.6.0-gpu/2018-03-01-a2a55008-5b3eb871/Singularity
collection: marcc-hpc/tensorflow
---

# marcc-hpc/tensorflow:1.6.0-gpu

```bash
$ singularity pull shub://marcc-hpc/tensorflow:1.6.0-gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.6.0-gpu

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

