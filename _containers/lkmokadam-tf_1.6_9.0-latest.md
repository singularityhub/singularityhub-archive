---
id: 2268
name: "lkmokadam/tf_1.6_9.0"
branch: "master"
tag: "latest"
commit: "9d725378b2ef287d94abff6c8354e458b647e10a"
version: "e7cdf21b1d6ed87f7908c5e70f8600b2"
build_date: "2018-03-24T15:18:06.515Z"
size_mb: 3844
size: 1847365663
sif: "https://datasets.datalad.org/shub/lkmokadam/tf_1.6_9.0/latest/2018-03-24-9d725378-e7cdf21b/e7cdf21b1d6ed87f7908c5e70f8600b2.simg"
url: https://datasets.datalad.org/shub/lkmokadam/tf_1.6_9.0/latest/2018-03-24-9d725378-e7cdf21b/
recipe: https://datasets.datalad.org/shub/lkmokadam/tf_1.6_9.0/latest/2018-03-24-9d725378-e7cdf21b/Singularity
collection: lkmokadam/tf_1.6_9.0
---

# lkmokadam/tf_1.6_9.0:latest

```bash
$ singularity pull shub://lkmokadam/tf_1.6_9.0:latest
```

## Singularity Recipe

```singularity
####
# Defines a Singularity container with GPU and MPI enabled TensorFlow
# https://www.tensorflow.org/install/install_sources#tested_source_configurations
####

BootStrap: docker
From: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

%environment
  export PATH=${PATH-}:/usr/lib/jvm/java-8-openjdk-amd64/bin/:/usr/local/cuda/bin
  export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
  export CUDA_HOME=/usr/local/cuda
  export LD_LIBRARY_PATH=${LD_LIBRARY_PATH-}:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64

%post
  apt update 
  apt-get install -y python-pip mpich wget
  pip install mpi4py
  pip install --no-cache-dir tensorflow-gpu

  # Patch container to work on Titan
  wget https://raw.githubusercontent.com/olcf/SingularityTools/master/Titan/TitanBootstrap.sh
  sh TitanBootstrap.sh
  rm TitanBootstrap.sh
```

## Collection

 - Name: [lkmokadam/tf_1.6_9.0](https://github.com/lkmokadam/tf_1.6_9.0)
 - License: None

