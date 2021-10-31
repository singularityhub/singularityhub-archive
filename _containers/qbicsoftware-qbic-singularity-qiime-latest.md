---
id: 1969
name: "qbicsoftware/qbic-singularity-qiime"
branch: "master"
tag: "latest"
commit: "e9f64edf777972c1af7dd75b30ec9c65ac795d9c"
version: "5e58ee00af47a589db312ab7f2c187c4"
build_date: "2021-04-05T23:45:32.037Z"
size_mb: 2895
size: 1133588511
sif: "https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-qiime/latest/2021-04-05-e9f64edf-5e58ee00/5e58ee00af47a589db312ab7f2c187c4.simg"
url: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-qiime/latest/2021-04-05-e9f64edf-5e58ee00/
recipe: https://datasets.datalad.org/shub/qbicsoftware/qbic-singularity-qiime/latest/2021-04-05-e9f64edf-5e58ee00/Singularity
collection: qbicsoftware/qbic-singularity-qiime
---

# qbicsoftware/qbic-singularity-qiime:latest

```bash
$ singularity pull shub://qbicsoftware/qbic-singularity-qiime:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:biocontainers/biocontainers:latest
#Registry: quay.io

%environment
#Set your toolname here and the appropriate version to have this in the metadata of your container
    QIIME=1.9.1
    PATH=/usr/bin/miniconda/envs/qiime1/bin:/usr/bin/miniconda/bin:$PATH
    LC_ALL="C"

%post 
apt-get install -y git wget build-essential curl file git python-setuptools
wget https://repo.continuum.io/miniconda/Miniconda2-4.0.5-Linux-x86_64.sh
chmod +x Miniconda2-4.0.5-Linux-x86_64.sh
./Miniconda2-4.0.5-Linux-x86_64.sh -b -p /usr/bin/miniconda

export PATH="$PATH:/usr/bin/miniconda/envs/qiime1/bin:/usr/bin/miniconda/bin"
conda create -n qiime1 python=2.7 qiime matplotlib=1.4.3 mock vsearch=2.3.4 fastq-join nose -c bioconda
ln -s /usr/bin/miniconda/envs/qiime1/bin/vsearch /usr/bin/miniconda/envs/qiime1/bin/usearch61
%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
```

## Collection

 - Name: [qbicsoftware/qbic-singularity-qiime](https://github.com/qbicsoftware/qbic-singularity-qiime)
 - License: [MIT License](https://api.github.com/licenses/mit)

