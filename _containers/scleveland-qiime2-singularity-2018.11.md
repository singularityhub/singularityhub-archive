---
id: 5711
name: "scleveland/qiime2-singularity"
branch: "master"
tag: "2018.11"
commit: "71a23c7c0b9338c31c8086849aa6c7eac904fe13"
version: "318f122ba9e00d5787c24d807df3a3e4"
build_date: "2018-12-03T21:18:09.865Z"
size_mb: 7856
size: 3250962463
sif: "https://datasets.datalad.org/shub/scleveland/qiime2-singularity/2018.11/2018-12-03-71a23c7c-318f122b/318f122ba9e00d5787c24d807df3a3e4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/scleveland/qiime2-singularity/2018.11/2018-12-03-71a23c7c-318f122b/
recipe: https://datasets.datalad.org/shub/scleveland/qiime2-singularity/2018.11/2018-12-03-71a23c7c-318f122b/Singularity
collection: scleveland/qiime2-singularity
---

# scleveland/qiime2-singularity:2018.11

```bash
$ singularity pull shub://scleveland/qiime2-singularity:2018.11
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

wget https://data.qiime2.org/distro/core/qiime2-2018.11-py35-linux-conda.yml
conda env create -n qiime2-2018.11 --file qiime2-2018.11-py35-linux-conda.yml
rm qiime2-2018.11-py35-linux-conda.yml

%runscript
source activate qiime2-2018.11
```

## Collection

 - Name: [scleveland/qiime2-singularity](https://github.com/scleveland/qiime2-singularity)
 - License: None

