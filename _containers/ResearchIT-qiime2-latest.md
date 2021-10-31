---
id: 1991
name: "ResearchIT/qiime2"
branch: "master"
tag: "latest"
commit: "1945772101c0bbeff0b46e2bc58072d0f6b14e6d"
version: "67da376d3efd1ab56b318e914bef370d"
build_date: "2021-03-16T17:50:31.943Z"
size_mb: 7151
size: 3037179935
sif: "https://datasets.datalad.org/shub/ResearchIT/qiime2/latest/2021-03-16-19457721-67da376d/67da376d3efd1ab56b318e914bef370d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ResearchIT/qiime2/latest/2021-03-16-19457721-67da376d/
recipe: https://datasets.datalad.org/shub/ResearchIT/qiime2/latest/2021-03-16-19457721-67da376d/Singularity
collection: ResearchIT/qiime2
---

# ResearchIT/qiime2:latest

```bash
$ singularity pull shub://ResearchIT/qiime2:latest
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

wget https://data.qiime2.org/distro/core/qiime2-2018.2-py35-linux-conda.yml
conda env create -n qiime2-2018.2 --file qiime2-2018.2-py35-linux-conda.yml
rm qiime2-2018.2-py35-linux-conda.yml
source activate qiime2-2018.2

%runscript
exec qiime "$@"
```

## Collection

 - Name: [ResearchIT/qiime2](https://github.com/ResearchIT/qiime2)
 - License: None

