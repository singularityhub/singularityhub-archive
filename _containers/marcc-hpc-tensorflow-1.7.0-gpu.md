---
id: 2379
name: "marcc-hpc/tensorflow"
branch: "1.7.0-gpu"
tag: "1.7.0-gpu"
commit: "b6ebe4ed78b7ba95ee5fd8cbb801f182391c54a6"
version: "b68a1ee16e4495dd50f9c78c3350b151"
build_date: "2018-04-03T16:39:18.118Z"
size_mb: 2624
size: 1181823007
sif: "https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.7.0-gpu/2018-04-03-b6ebe4ed-b68a1ee1/b68a1ee16e4495dd50f9c78c3350b151.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.7.0-gpu/2018-04-03-b6ebe4ed-b68a1ee1/
recipe: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.7.0-gpu/2018-04-03-b6ebe4ed-b68a1ee1/Singularity
collection: marcc-hpc/tensorflow
---

# marcc-hpc/tensorflow:1.7.0-gpu

```bash
$ singularity pull shub://marcc-hpc/tensorflow:1.7.0-gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.7.0-gpu

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

