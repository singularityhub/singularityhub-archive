---
id: 6360
name: "gapicare/singularity"
branch: "master"
tag: "latest"
commit: "41baeb14f19f16744d0f5fbe5990e64988161998"
version: "fe3352b8f9e0fa865d41e9403b7ec53c"
build_date: "2019-01-21T15:26:42.092Z"
size_mb: 3056
size: 1560698911
sif: "https://datasets.datalad.org/shub/gapicare/singularity/latest/2019-01-21-41baeb14-fe3352b8/fe3352b8f9e0fa865d41e9403b7ec53c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/gapicare/singularity/latest/2019-01-21-41baeb14-fe3352b8/
recipe: https://datasets.datalad.org/shub/gapicare/singularity/latest/2019-01-21-41baeb14-fe3352b8/Singularity
collection: gapicare/singularity
---

# gapicare/singularity:latest

```bash
$ singularity pull shub://gapicare/singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04

%labels

%environment
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
export PATH=/bin:/usr/bin:/usr/local/bin:/usr/local/cuda/bin:
export LC_ALL=C

%post
apt-get update
apt-get install -y libhdf5-dev graphviz locales python3-dev python3-pip
apt-get clean

pip3 install tensorflow-gpu==1.8.0
pip3 install keras==2.1.6
pip3 install numpy Pillow scikit-learn pandas\
 matplotlib notebook ipython h5py liac-arff openpyxl xlsxwriter

# create some generic mount points
mkdir -p /var/spool/slurm
mkdir /cvmfs /grid /data1 /data2 /data0
touch /bin/nvidia-smi
# jost and nsc
mkdir -p /net/jost/home /d/hpc/session /d/hpc/cache
mkdir -p /net/hold/data1
```

## Collection

 - Name: [gapicare/singularity](https://github.com/gapicare/singularity)
 - License: None

