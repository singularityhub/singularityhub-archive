---
id: 4858
name: "biotext/Singularity"
branch: "master"
tag: "latest"
commit: "ee37a55044e8410fd60382becab5e7b9164affb7"
version: "b4e973f7ccddbf29012c7ac81326e3a7"
build_date: "2018-09-19T22:54:38.262Z"
size_mb: 6518
size: 2821693471
sif: "https://datasets.datalad.org/shub/biotext/Singularity/latest/2018-09-19-ee37a550-b4e973f7/b4e973f7ccddbf29012c7ac81326e3a7.simg"
url: https://datasets.datalad.org/shub/biotext/Singularity/latest/2018-09-19-ee37a550-b4e973f7/
recipe: https://datasets.datalad.org/shub/biotext/Singularity/latest/2018-09-19-ee37a550-b4e973f7/Singularity
collection: biotext/Singularity
---

# biotext/Singularity:latest

```bash
$ singularity pull shub://biotext/Singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04

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
apt-get install -y libhdf5-dev graphviz locales python3-dev python3-pip python3-tk
apt-get install -y --allow-downgrades --allow-change-held-packages libcudnn7=7.0.5.15-1+cuda9.0
locale-gen en_US.UTF-8
apt-get clean

pip3 install --upgrade pip
pip install tensorflow-gpu==1.6.0
pip install keras==2.1.5
pip install setuptools wheel Pillow scikit-learn pandas matplotlib==2.2.2 notebook ipython tqdm
pip install h5py
pip install gensim
pip install nltk
python3 -m nltk.downloader all

###
### destination for NIH HPC bind mounts
###
mkdir /gpfs /spin1 /gs3 /gs4 /gs5 /gs6 /gs7 /gs8 /gs11 /data /scratch /fdb /lscratch
```

## Collection

 - Name: [biotext/Singularity](https://github.com/biotext/Singularity)
 - License: None

