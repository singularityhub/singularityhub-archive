---
id: 9229
name: "edwardchalstrey1/turingbench"
branch: "master"
tag: "keras"
commit: "fc40b8ed95d1c82870aff8a61a17a323b3298a0e"
version: "5ba1b3153a830c54282bb65c31f88dff"
build_date: "2019-05-23T03:52:52.805Z"
size_mb: 3094
size: 1595330591
sif: "https://datasets.datalad.org/shub/edwardchalstrey1/turingbench/keras/2019-05-23-fc40b8ed-5ba1b315/5ba1b3153a830c54282bb65c31f88dff.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/edwardchalstrey1/turingbench/keras/2019-05-23-fc40b8ed-5ba1b315/
recipe: https://datasets.datalad.org/shub/edwardchalstrey1/turingbench/keras/2019-05-23-fc40b8ed-5ba1b315/Singularity
collection: edwardchalstrey1/turingbench
---

# edwardchalstrey1/turingbench:keras

```bash
$ singularity pull shub://edwardchalstrey1/turingbench:keras
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
pip3 install --upgrade pip
apt-get update

python3 -m pip install tensorflow-gpu==1.8.0
python3 -m pip install keras==2.1.6
python3 -m pip install Pillow scikit-learn pandas matplotlib notebook ipython

# create some generic mount points
mkdir /mnt/data /mnt/input /mnt/output /mnt/ref /mnt/code /mnt/work
```

## Collection

 - Name: [edwardchalstrey1/turingbench](https://github.com/edwardchalstrey1/turingbench)
 - License: None

