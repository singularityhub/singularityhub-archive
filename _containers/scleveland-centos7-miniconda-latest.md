---
id: 5791
name: "scleveland/centos7-miniconda"
branch: "master"
tag: "latest"
commit: "f5db452a700f921adfbc13ce00c223763e75c85e"
version: "fc59f744792e0c0b37a371ff17c61e5c"
build_date: "2021-04-02T13:52:23.002Z"
size_mb: 1431
size: 593027103
sif: "https://datasets.datalad.org/shub/scleveland/centos7-miniconda/latest/2021-04-02-f5db452a-fc59f744/fc59f744792e0c0b37a371ff17c61e5c.simg"
url: https://datasets.datalad.org/shub/scleveland/centos7-miniconda/latest/2021-04-02-f5db452a-fc59f744/
recipe: https://datasets.datalad.org/shub/scleveland/centos7-miniconda/latest/2021-04-02-f5db452a-fc59f744/Singularity
collection: scleveland/centos7-miniconda
---

# scleveland/centos7-miniconda:latest

```bash
$ singularity pull shub://scleveland/centos7-miniconda:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: scleveland/centos7-base-singularity

%environment
export PATH=/opt/conda/bin:$PATH

%post
yum update -y
yum  install -y @"Development Tools"
yum install -y git curl which python3 python3-devel vim htop wget tar bzip2 gzip lz4 lzma mesa-libGL mesa-libGLU
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda
export PATH=/opt/conda/bin:$PATH
conda update -y conda
```

## Collection

 - Name: [scleveland/centos7-miniconda](https://github.com/scleveland/centos7-miniconda)
 - License: None

