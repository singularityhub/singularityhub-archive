---
id: 1376
name: "ResearchIT/qiime2"
branch: "master"
tag: "2017.12"
commit: "1945772101c0bbeff0b46e2bc58072d0f6b14e6d"
version: "10400c89865b113e2ee5bbcc92c2c09a"
build_date: "2018-07-28T02:46:39.795Z"
size_mb: 7139
size: 3035914271
sif: "https://datasets.datalad.org/shub/ResearchIT/qiime2/2017.12/2018-07-28-19457721-10400c89/10400c89865b113e2ee5bbcc92c2c09a.simg"
url: https://datasets.datalad.org/shub/ResearchIT/qiime2/2017.12/2018-07-28-19457721-10400c89/
recipe: https://datasets.datalad.org/shub/ResearchIT/qiime2/2017.12/2018-07-28-19457721-10400c89/Singularity
collection: ResearchIT/qiime2
---

# ResearchIT/qiime2:2017.12

```bash
$ singularity pull shub://ResearchIT/qiime2:2017.12
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/ 
Include: yum

%environment
PATH=/opt/conda/envs/qiime2-2017.12/bin:/opt/conda/bin:$PATH
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

wget https://data.qiime2.org/distro/core/qiime2-2017.12-py35-linux-conda.yml
conda env create -n qiime2-2017.12 --file qiime2-2017.12-py35-linux-conda.yml
rm qiime2-2017.12-py35-linux-conda.yml
source activate qiime2-2017.12

%runscript
exec qiime "$@"
```

## Collection

 - Name: [ResearchIT/qiime2](https://github.com/ResearchIT/qiime2)
 - License: None

