---
id: 394
name: "edraizen/Singularity"
branch: "master"
tag: "latest"
commit: "0ace0aebbede9e50c29a6a7dcf5da72080c5f4ce"
version: "ee98bc7eff9b294be30a8fe6388353fe"
build_date: "2017-11-16T10:30:37.337Z"
size_mb: 3051
size: 1491283999
sif: "https://datasets.datalad.org/shub/edraizen/Singularity/latest/2017-11-16-0ace0aeb-ee98bc7e/ee98bc7eff9b294be30a8fe6388353fe.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/edraizen/Singularity/latest/2017-11-16-0ace0aeb-ee98bc7e/
recipe: https://datasets.datalad.org/shub/edraizen/Singularity/latest/2017-11-16-0ace0aeb-ee98bc7e/Singularity
collection: edraizen/Singularity
---

# edraizen/Singularity:latest

```bash
$ singularity pull shub://edraizen/Singularity:latest
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
export PYTHONPATH=/usr/share/pdb2pqr:

################################################################################
%post
################################################################################

###
### install keras + tensorflow + other useful packages
###
apt-get update
apt-get install -y wget libhdf5-dev graphviz locales python python-pip git xvfb python-vtk pdb2pqr python-pandas
locale-gen en_US.UTF-8
apt-get clean

wget ftp://ftp.cmbi.ru.nl/pub/software/dssp/dssp-2.0.4-linux-i386 -O /usr/local/bin/dssp
chmod a+x /usr/local/bin/dssp

wget ftp://ftp.icgeb.trieste.it/pub/CX/CX.c.gz -O /usr/local/bin/CX.c.gz
gunzip /usr/local/bin/CX.c.gz
gcc -o /usr/local/bin/cx /usr/local/bin/CX.c -lm
rm /usr/local/bin/CX.c

pip install --upgrade pip
pip install tensorflow-gpu==1.4.0
pip install keras==2.0.8
pip install setuptools wheel Pillow scikit-learn matplotlib ipython==5.5.0
pip install h5py
pip install mayavi
pip install --upgrade notebook
pip install cython
pip install Biopython

wget http://freesasa.github.io/freesasa-2.0.2.tar.gz
tar -xzf freesasa-2.0.2.tar.gz
cd freesasa-2.0.2
./configure CFLAGS=-fPIC --enable-python-bindings --disable-json --disable-xml
make && make install

###
### destination for NIH HPC bind mounts
###
mkdir /gpfs /spin1 /gs2 /gs3 /gs4 /gs5 /gs6 /gs7 /gs8 /data /scratch /fdb /lscratch /pdb
```

## Collection

 - Name: [edraizen/Singularity](https://github.com/edraizen/Singularity)
 - License: None

