---
id: 2683
name: "NIH-HPC/singularity-examples"
branch: "master"
tag: "keras-py3"
commit: "967bdfcb602b1f890dcbb2a7186d5408c44bf0b8"
version: "87d998af9507709acbe29908e7e6df8f"
build_date: "2018-04-28T19:11:00.458Z"
size_mb: 3461
size: 1678172191
sif: "https://datasets.datalad.org/shub/NIH-HPC/singularity-examples/keras-py3/2018-04-28-967bdfcb-87d998af/87d998af9507709acbe29908e7e6df8f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/NIH-HPC/singularity-examples/keras-py3/2018-04-28-967bdfcb-87d998af/
recipe: https://datasets.datalad.org/shub/NIH-HPC/singularity-examples/keras-py3/2018-04-28-967bdfcb-87d998af/Singularity
collection: NIH-HPC/singularity-examples
---

# NIH-HPC/singularity-examples:keras-py3

```bash
$ singularity pull shub://NIH-HPC/singularity-examples:keras-py3
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04

#---------------------------------------------------------------------
%labels
#---------------------------------------------------------------------
MAINTAINER Wolfgang Resch

#---------------------------------------------------------------------
%environment
#---------------------------------------------------------------------
export PATH=/bin:/usr/bin:/usr/local/bin:/usr/local/cuda/bin:
export LC_ALL=C

#---------------------------------------------------------------------
%post
#---------------------------------------------------------------------

apt-get update
apt-get install -y libhdf5-dev graphviz locales python3-dev python3-pip
apt-get clean

pip3 install tensorflow-gpu==1.8.0
pip3 install keras==2.1.6
pip3 install Pillow scikit-learn pandas matplotlib notebook ipython

# create some generic mount points
mkdir /mnt/data /mnt/input /mnt/output /mnt/ref /mnt/code /mnt/work
```

## Collection

 - Name: [NIH-HPC/singularity-examples](https://github.com/NIH-HPC/singularity-examples)
 - License: None

