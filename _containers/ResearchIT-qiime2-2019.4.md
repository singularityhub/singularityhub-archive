---
id: 8919
name: "ResearchIT/qiime2"
branch: "master"
tag: "2019.4"
commit: "948e4faccebd289797564d1853dec6e70588ea1f"
version: "ab69ee8739ec34d3fa50768c9a458d13"
build_date: "2019-08-09T20:07:38.422Z"
size_mb: 7163
size: 3052785695
sif: "https://datasets.datalad.org/shub/ResearchIT/qiime2/2019.4/2019-08-09-948e4fac-ab69ee87/ab69ee8739ec34d3fa50768c9a458d13.simg"
url: https://datasets.datalad.org/shub/ResearchIT/qiime2/2019.4/2019-08-09-948e4fac-ab69ee87/
recipe: https://datasets.datalad.org/shub/ResearchIT/qiime2/2019.4/2019-08-09-948e4fac-ab69ee87/Singularity
collection: ResearchIT/qiime2
---

# ResearchIT/qiime2:2019.4

```bash
$ singularity pull shub://ResearchIT/qiime2:2019.4
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
source activate qiime2-2019.4

%post
yum update -y
yum  install -y @"Development Tools"
yum install -y git curl which python3 python3-devel vim htop wget tar bzip2 gzip lz4 lzma mesa-libGL mesa-libGLU
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda
export PATH=/opt/conda/bin:$PATH
conda install -y conda
conda update -y conda
wget https://data.qiime2.org/distro/core/qiime2-2019.4-py36-linux-conda.yml
conda env create -n qiime2-2019.4 --file qiime2-2019.4-py36-linux-conda.yml

%runscript
exec qiime "$@"
```

## Collection

 - Name: [ResearchIT/qiime2](https://github.com/ResearchIT/qiime2)
 - License: None

