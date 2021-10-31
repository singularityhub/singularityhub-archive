---
id: 9901
name: "karltayeb/gp_fine_mapping"
branch: "master"
tag: "cpu"
commit: "8a9fd4143986f20ee3e2a60146b253d51eb2a8e5"
version: "09e6f600ddf1bf54749db87cbdb360ac"
build_date: "2019-06-23T23:32:49.177Z"
size_mb: 1722
size: 733978655
sif: "https://datasets.datalad.org/shub/karltayeb/gp_fine_mapping/cpu/2019-06-23-8a9fd414-09e6f600/09e6f600ddf1bf54749db87cbdb360ac.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/karltayeb/gp_fine_mapping/cpu/2019-06-23-8a9fd414-09e6f600/
recipe: https://datasets.datalad.org/shub/karltayeb/gp_fine_mapping/cpu/2019-06-23-8a9fd414-09e6f600/Singularity
collection: karltayeb/gp_fine_mapping
---

# karltayeb/gp_fine_mapping:cpu

```bash
$ singularity pull shub://karltayeb/gp_fine_mapping:cpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.13.1-py3-jupyter

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
  apt-get -y install python3-tk

  pip install selenium
  pip install moviepy
  pip install lmdb
  pip install opencv-contrib-python
  pip install cryptography
  
  pip install gpflow
  pip install tensorflow-probability
  pip install matplotlib
  pip install sklearn
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

