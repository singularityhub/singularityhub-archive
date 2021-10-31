---
id: 9878
name: "karltayeb/gp_fine_mapping"
branch: "master"
tag: "gpu"
commit: "5252e00f94c909e41767c21f69da4e4bb208c343"
version: "ddc5fd6dbdca1f22739b5e4c0859791a"
build_date: "2019-06-24T14:48:05.229Z"
size_mb: 3903
size: 1962504223
sif: "https://datasets.datalad.org/shub/karltayeb/gp_fine_mapping/gpu/2019-06-24-5252e00f-ddc5fd6d/ddc5fd6dbdca1f22739b5e4c0859791a.simg"
url: https://datasets.datalad.org/shub/karltayeb/gp_fine_mapping/gpu/2019-06-24-5252e00f-ddc5fd6d/
recipe: https://datasets.datalad.org/shub/karltayeb/gp_fine_mapping/gpu/2019-06-24-5252e00f-ddc5fd6d/Singularity
collection: karltayeb/gp_fine_mapping
---

# karltayeb/gp_fine_mapping:gpu

```bash
$ singularity pull shub://karltayeb/gp_fine_mapping:gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.13.1-gpu-py3-jupyter

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
  apt-get install -y python3-tk

  apt-get install -y libsm6 libxext6
  pip install selenium
  pip install moviepy
  pip install lmdb
  pip install opencv-contrib-python
  pip install cryptography
  
  pip install gpflow
  pip install sklearn
  pip install tensorflow-probability
  pip install matplotlib
  pip install seaborn
  
%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [karltayeb/gp_fine_mapping](https://github.com/karltayeb/gp_fine_mapping)
 - License: None

