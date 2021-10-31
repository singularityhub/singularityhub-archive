---
id: 2380
name: "marcc-hpc/tensorflow"
branch: "1.7.0-gpu-py3"
tag: "1.7.0-gpu-py3"
commit: "db8b6b89638d90fd815bf355669d7eb2e745cc79"
version: "9e3fbfed3f1c1fa2a7f1e9228d1f0c4a"
build_date: "2018-04-03T16:39:18.110Z"
size_mb: 2630
size: 1191546911
sif: "https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.7.0-gpu-py3/2018-04-03-db8b6b89-9e3fbfed/9e3fbfed3f1c1fa2a7f1e9228d1f0c4a.simg"
url: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.7.0-gpu-py3/2018-04-03-db8b6b89-9e3fbfed/
recipe: https://datasets.datalad.org/shub/marcc-hpc/tensorflow/1.7.0-gpu-py3/2018-04-03-db8b6b89-9e3fbfed/Singularity
collection: marcc-hpc/tensorflow
---

# marcc-hpc/tensorflow:1.7.0-gpu-py3

```bash
$ singularity pull shub://marcc-hpc/tensorflow:1.7.0-gpu-py3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.7.0-gpu-py3

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

