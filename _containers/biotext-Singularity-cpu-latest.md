---
id: 3179
name: "biotext/Singularity-cpu"
branch: "master"
tag: "latest"
commit: "5b8ca6f5b1df7c39f07d0401356574bbcb6a612f"
version: "c463d1943144739545cacc667d80cb25"
build_date: "2018-09-19T22:54:39.055Z"
size_mb: 4913
size: 1849155615
sif: "https://datasets.datalad.org/shub/biotext/Singularity-cpu/latest/2018-09-19-5b8ca6f5-c463d194/c463d1943144739545cacc667d80cb25.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/biotext/Singularity-cpu/latest/2018-09-19-5b8ca6f5-c463d194/
recipe: https://datasets.datalad.org/shub/biotext/Singularity-cpu/latest/2018-09-19-5b8ca6f5-c463d194/Singularity
collection: biotext/Singularity-cpu
---

# biotext/Singularity-cpu:latest

```bash
$ singularity pull shub://biotext/Singularity-cpu:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

################################################################################
%labels
################################################################################
MAINTAINER Wolfgang Resch
VERSION v3

################################################################################
%environment
################################################################################
export PATH=/usr/local/sbin:/usr/sbin:/sbin:/bin:/usr/bin:/usr/local/bin:

################################################################################
%post
################################################################################

###
### install keras + tensorflow + other useful packages
###
apt-get update
apt-get install -y libhdf5-dev graphviz locales python3-dev python3-pip python3-tk
locale-gen en_US.UTF-8
apt-get clean

pip3 install --upgrade pip
pip install tensorflow
pip install keras
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

 - Name: [biotext/Singularity-cpu](https://github.com/biotext/Singularity-cpu)
 - License: None

