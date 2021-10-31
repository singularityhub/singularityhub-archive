---
id: 653
name: "OvcharenkoLab/keras_demo"
branch: "master"
tag: "latest"
commit: "9faf2a4640664de8c01a44981d5cbc51ddab4cca"
version: "4ba93c7295966a104e02a139e4b5ebd2"
build_date: "2021-03-13T19:22:24.488Z"
size_mb: 2585
size: 1285648415
sif: "https://datasets.datalad.org/shub/OvcharenkoLab/keras_demo/latest/2021-03-13-9faf2a46-4ba93c72/4ba93c7295966a104e02a139e4b5ebd2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/OvcharenkoLab/keras_demo/latest/2021-03-13-9faf2a46-4ba93c72/
recipe: https://datasets.datalad.org/shub/OvcharenkoLab/keras_demo/latest/2021-03-13-9faf2a46-4ba93c72/Singularity
collection: OvcharenkoLab/keras_demo
---

# OvcharenkoLab/keras_demo:latest

```bash
$ singularity pull shub://OvcharenkoLab/keras_demo:latest
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
export PATH=/usr/local/sbin:/usr/sbin:/sbin:/bin:/usr/bin:/usr/local/bin:/usr/local/cuda/bin:

################################################################################
%post
################################################################################

###
### install keras + tensorflow + other useful packages
###
apt-get update
apt-get install -y wget libhdf5-dev graphviz locales python python-pip git python-pandas
locale-gen en_US.UTF-8
apt-get clean

pip install --upgrade pip
pip install tensorflow-gpu==1.3.0
pip install keras==2.0.8
pip install setuptools wheel Pillow scikit-learn matplotlib ipython==5.5.0
pip install h5py
pip install --upgrade notebook
pip install cython
pip install Biopython

###
### destination for NIH HPC bind mounts
###
mkdir /gpfs /spin1 /gs2 /gs3 /gs4 /gs5 /gs6 /gs7 /gs8 /data /scratch /fdb /lscratch /pdb
```

## Collection

 - Name: [OvcharenkoLab/keras_demo](https://github.com/OvcharenkoLab/keras_demo)
 - License: None

