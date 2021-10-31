---
id: 874
name: "NIH-HPC/singularity-examples"
branch: "master"
tag: "keras"
commit: "2ccdc4a334b5e669dd6eab2099623f8b0d5f5af8"
version: "0c8c1e1ebb18227cb6a6eb1ea8a79984"
build_date: "2017-11-22T15:36:09.748Z"
size_mb: 2843
size: 1418207263
sif: "https://datasets.datalad.org/shub/NIH-HPC/singularity-examples/keras/2017-11-22-2ccdc4a3-0c8c1e1e/0c8c1e1ebb18227cb6a6eb1ea8a79984.simg"
url: https://datasets.datalad.org/shub/NIH-HPC/singularity-examples/keras/2017-11-22-2ccdc4a3-0c8c1e1e/
recipe: https://datasets.datalad.org/shub/NIH-HPC/singularity-examples/keras/2017-11-22-2ccdc4a3-0c8c1e1e/Singularity
collection: NIH-HPC/singularity-examples
---

# NIH-HPC/singularity-examples:keras

```bash
$ singularity pull shub://NIH-HPC/singularity-examples:keras
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:8.0-cudnn6-runtime-ubuntu16.04

################################################################################
%labels
################################################################################
MAINTAINER Wolfgang Resch
VERSION v3

################################################################################
%environment
################################################################################
export PATH=/bin:/usr/bin:/usr/local/bin:/usr/local/cuda/bin:

################################################################################
%post
################################################################################

###
### install keras + tensorflow + other useful packages
###
apt-get update
apt-get install -y libhdf5-dev graphviz locales python3-dev python3-pip
locale-gen en_US.UTF-8
apt-get clean

pip3 install tensorflow-gpu==1.3.0
pip3 install keras==2.0.8
pip3 install Pillow scikit-learn pandas matplotlib notebook ipython

###
### destination for NIH HPC bind mounts
###

mkdir /gpfs /spin1 /gs2 /gs3 /gs4 /gs5 /gs6 /gs7 /gs8 /data /scratch /fdb /lscratch
```

## Collection

 - Name: [NIH-HPC/singularity-examples](https://github.com/NIH-HPC/singularity-examples)
 - License: None

