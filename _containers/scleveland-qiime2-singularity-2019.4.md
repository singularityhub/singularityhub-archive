---
id: 9237
name: "scleveland/qiime2-singularity"
branch: "master"
tag: "2019.4"
commit: "6fcb304f8753a7b255bea9903c622b8aed2095dd"
version: "0950a4fd94d1f5f38bf3a1b16cee2b61"
build_date: "2019-05-23T03:52:49.556Z"
size_mb: 7149
size: 3041546271
sif: "https://datasets.datalad.org/shub/scleveland/qiime2-singularity/2019.4/2019-05-23-6fcb304f-0950a4fd/0950a4fd94d1f5f38bf3a1b16cee2b61.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/scleveland/qiime2-singularity/2019.4/2019-05-23-6fcb304f-0950a4fd/
recipe: https://datasets.datalad.org/shub/scleveland/qiime2-singularity/2019.4/2019-05-23-6fcb304f-0950a4fd/Singularity
collection: scleveland/qiime2-singularity
---

# scleveland/qiime2-singularity:2019.4

```bash
$ singularity pull shub://scleveland/qiime2-singularity:2019.4
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: scleveland/centos7-base-singularity
#Bootstrap: debootstrap
#MirrorURL: http://us.archive.ubuntu.com/ubuntu/
#OSVersion: bionic

%environment
PATH=/opt/conda/envs/qiime2-2018.11/bin:/opt/conda/bin:$PATH
export PATH

%post
yum update -y
yum  install -y @"Development Tools"
yum install -y git curl which python3 python3-devel vim htop wget tar bzip2 gzip lz4 lzma mesa-libGL mesa-libGLU
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda
export PATH=/opt/conda/bin:$PATH
conda install -y conda
conda update -y conda
mkdir /lus
mkdir /lus/scratch

wget https://data.qiime2.org/distro/core/qiime2-2019.4-py36-linux-conda.yml
conda env create -n qiime2-2019.4 --file qiime2-2019.4-py36-linux-conda.yml
# OPTIONAL CLEANUP
rm qiime2-2019.4-py36-linux-conda.yml

%runscript
source activate qiime2-2019.4
```

## Collection

 - Name: [scleveland/qiime2-singularity](https://github.com/scleveland/qiime2-singularity)
 - License: None

