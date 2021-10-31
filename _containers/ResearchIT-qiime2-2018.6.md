---
id: 3733
name: "ResearchIT/qiime2"
branch: "master"
tag: "2018.6"
commit: "75c6fd84189dc7c306c0539d190370ca87b891c5"
version: "ef75c81b37725c63f6a32eb310055797"
build_date: "2018-07-27T19:34:58.946Z"
size_mb: 7313
size: 3115597855
sif: "https://datasets.datalad.org/shub/ResearchIT/qiime2/2018.6/2018-07-27-75c6fd84-ef75c81b/ef75c81b37725c63f6a32eb310055797.simg"
url: https://datasets.datalad.org/shub/ResearchIT/qiime2/2018.6/2018-07-27-75c6fd84-ef75c81b/
recipe: https://datasets.datalad.org/shub/ResearchIT/qiime2/2018.6/2018-07-27-75c6fd84-ef75c81b/Singularity
collection: ResearchIT/qiime2
---

# ResearchIT/qiime2:2018.6

```bash
$ singularity pull shub://ResearchIT/qiime2:2018.6
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/ 
Include: yum

%environment
PATH=/opt/conda/bin:$PATH
export PATH
source activate qiime2-2018.6

%post
yum update -y
yum  install -y @"Development Tools"
yum install -y git curl which python3 python3-devel vim htop wget tar bzip2 gzip lz4 lzma mesa-libGL mesa-libGLU
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda
export PATH=/opt/conda/bin:$PATH
conda install -y conda
conda update -y conda
wget https://data.qiime2.org/distro/core/qiime2-2018.6-py35-linux-conda.yml
conda env create -n qiime2-2018.6 --file qiime2-2018.6-py35-linux-conda.yml

%runscript
exec qiime "$@"
```

## Collection

 - Name: [ResearchIT/qiime2](https://github.com/ResearchIT/qiime2)
 - License: None

