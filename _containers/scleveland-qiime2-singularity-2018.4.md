---
id: 3114
name: "scleveland/qiime2-singularity"
branch: "master"
tag: "2018.4"
commit: "ca1ec64ca14694f26229af1d3d1a1e9bcb3e47b5"
version: "3811cacae479fa02a138b926fb64357b"
build_date: "2018-11-27T20:51:05.170Z"
size_mb: 7306
size: 3112730655
sif: "https://datasets.datalad.org/shub/scleveland/qiime2-singularity/2018.4/2018-11-27-ca1ec64c-3811caca/3811cacae479fa02a138b926fb64357b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/scleveland/qiime2-singularity/2018.4/2018-11-27-ca1ec64c-3811caca/
recipe: https://datasets.datalad.org/shub/scleveland/qiime2-singularity/2018.4/2018-11-27-ca1ec64c-3811caca/Singularity
collection: scleveland/qiime2-singularity
---

# scleveland/qiime2-singularity:2018.4

```bash
$ singularity pull shub://scleveland/qiime2-singularity:2018.4
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%environment
PATH=/opt/conda/envs/qiime2-2018.4/bin:/opt/conda/bin:$PATH
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

wget https://data.qiime2.org/distro/core/qiime2-2018.4-py35-linux-conda.yml
conda env create -n qiime2-2018.4 --file qiime2-2018.4-py35-linux-conda.yml
rm qiime2-2018.4-py35-linux-conda.yml
source activate qiime2-2018.4

%runscript
exec qiime "$@"
```

## Collection

 - Name: [scleveland/qiime2-singularity](https://github.com/scleveland/qiime2-singularity)
 - License: None

