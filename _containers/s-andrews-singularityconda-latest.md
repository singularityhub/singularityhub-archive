---
id: 6488
name: "s-andrews/singularityconda"
branch: "master"
tag: "latest"
commit: "e6ee3d8fbdc546865cd3f3d00dabf82a87496d54"
version: "ee9a03912ccc380a7610faa7daa85abd"
build_date: "2020-03-03T12:51:21.002Z"
size_mb: 1511
size: 894365727
sif: "https://datasets.datalad.org/shub/s-andrews/singularityconda/latest/2020-03-03-e6ee3d8f-ee9a0391/ee9a03912ccc380a7610faa7daa85abd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/s-andrews/singularityconda/latest/2020-03-03-e6ee3d8f-ee9a0391/
recipe: https://datasets.datalad.org/shub/s-andrews/singularityconda/latest/2020-03-03-e6ee3d8f-ee9a0391/Singularity
collection: s-andrews/singularityconda
---

# s-andrews/singularityconda:latest

```bash
$ singularity pull shub://s-andrews/singularityconda:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest  

%labels
MAINTAINER Simon Andrews

%environment

%runscript

%post  
apt -y update
apt -y install wget
wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b

echo ". ~/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc
. ~/miniconda3/etc/profile.d/conda.sh

conda config --add channels bioconda
conda config --add channels conda-forge
conda install --yes bwa fastqc
```

## Collection

 - Name: [s-andrews/singularityconda](https://github.com/s-andrews/singularityconda)
 - License: None

