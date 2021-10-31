---
id: 11209
name: "peterk87/nf-iav-illumina"
branch: "master"
tag: "latest"
commit: "39610c05d83b9dcdcd43c0d999b1923caf29c3a6"
version: "cb8f2e45d5cb4336df775e73a8fba659"
build_date: "2021-04-19T13:29:39.934Z"
size_mb: 1109.0
size: 398360607
sif: "https://datasets.datalad.org/shub/peterk87/nf-iav-illumina/latest/2021-04-19-39610c05-cb8f2e45/cb8f2e45d5cb4336df775e73a8fba659.sif"
url: https://datasets.datalad.org/shub/peterk87/nf-iav-illumina/latest/2021-04-19-39610c05-cb8f2e45/
recipe: https://datasets.datalad.org/shub/peterk87/nf-iav-illumina/latest/2021-04-19-39610c05-cb8f2e45/Singularity
collection: peterk87/nf-iav-illumina
---

# peterk87/nf-iav-illumina:latest

```bash
$ singularity pull shub://peterk87/nf-iav-illumina:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:debian:latest

%labels
    MAINTAINER Peter Kruczkiewicz
    DESCRIPTION Singularity image containing all requirements for the peterk87/nf-iav-illumina pipeline
    VERSION 1.1.0

%environment
    export PATH=/opt/conda/envs/nf-iav-illumina-1.1.0/bin:/opt/conda/bin:$PATH
    export LANG=C.UTF-8
    export LC_ALL=C.UTF-8

%files
    environment.yml /

%post
    apt-get update --fix-missing
    apt-get install -y wget bzip2 ca-certificates curl git procps
    apt-get clean
    rm -rf /var/lib/apt/lists/*
    wget https://repo.anaconda.com/miniconda/Miniconda3-4.7.10-Linux-x86_64.sh -O /miniconda.sh 
    /bin/bash /miniconda.sh -b -p /opt/conda
    rm /miniconda.sh
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh
    export PATH=/opt/conda/bin:$PATH
    conda install conda=4.7.12
    conda env create -f /environment.yml
    conda clean -tipsy
```

## Collection

 - Name: [peterk87/nf-iav-illumina](https://github.com/peterk87/nf-iav-illumina)
 - License: [MIT License](https://api.github.com/licenses/mit)

