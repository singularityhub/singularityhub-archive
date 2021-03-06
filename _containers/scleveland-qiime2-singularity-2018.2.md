---
id: 2637
name: "scleveland/qiime2-singularity"
branch: "master"
tag: "2018.2"
commit: "f26ba988c0d231a81276cac397258b32adc922b4"
version: "1e1bb5831900d1a19e90742f1b7de709"
build_date: "2018-11-27T20:50:55.275Z"
size_mb: 7285
size: 3089481759
sif: "https://datasets.datalad.org/shub/scleveland/qiime2-singularity/2018.2/2018-11-27-f26ba988-1e1bb583/1e1bb5831900d1a19e90742f1b7de709.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/scleveland/qiime2-singularity/2018.2/2018-11-27-f26ba988-1e1bb583/
recipe: https://datasets.datalad.org/shub/scleveland/qiime2-singularity/2018.2/2018-11-27-f26ba988-1e1bb583/Singularity
collection: scleveland/qiime2-singularity
---

# scleveland/qiime2-singularity:2018.2

```bash
$ singularity pull shub://scleveland/qiime2-singularity:2018.2
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/ 
Include: yum

%environment
PATH=/opt/conda/envs/qiime2-2018.2/bin:/opt/conda/bin:$PATH
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

wget https://data.qiime2.org/distro/core/qiime2-2018.2-py35-linux-conda.yml
conda env create -n qiime2-2018.2 --file qiime2-2018.2-py35-linux-conda.yml
rm qiime2-2018.2-py35-linux-conda.yml
source activate qiime2-2018.2

%runscript
exec qiime "$@"
```

## Collection

 - Name: [scleveland/qiime2-singularity](https://github.com/scleveland/qiime2-singularity)
 - License: None

