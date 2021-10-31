---
id: 3734
name: "ResearchIT/qiime2"
branch: "master"
tag: "2018.2"
commit: "1945772101c0bbeff0b46e2bc58072d0f6b14e6d"
version: "bc1fcd3aad45858260d08f605eb7b4f7"
build_date: "2018-07-27T19:34:58.938Z"
size_mb: 7151
size: 3037175839
sif: "https://datasets.datalad.org/shub/ResearchIT/qiime2/2018.2/2018-07-27-19457721-bc1fcd3a/bc1fcd3aad45858260d08f605eb7b4f7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ResearchIT/qiime2/2018.2/2018-07-27-19457721-bc1fcd3a/
recipe: https://datasets.datalad.org/shub/ResearchIT/qiime2/2018.2/2018-07-27-19457721-bc1fcd3a/Singularity
collection: ResearchIT/qiime2
---

# ResearchIT/qiime2:2018.2

```bash
$ singularity pull shub://ResearchIT/qiime2:2018.2
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

