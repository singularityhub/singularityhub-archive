---
id: 8769
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "bwa"
commit: "01fd237ed1c7688e532770e499b506f0d189a7b5"
version: "070bd5e1b70d641eba9546b2e3d7f354"
build_date: "2019-09-24T17:40:19.148Z"
size_mb: 302
size: 99827743
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/bwa/2019-09-24-01fd237e-070bd5e1/070bd5e1b70d641eba9546b2e3d7f354.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/bwa/2019-09-24-01fd237e-070bd5e1/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/bwa/2019-09-24-01fd237e-070bd5e1/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:bwa

```bash
$ singularity pull shub://jlboat/BioinfoContainers:bwa
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:latest

%labels
    Topic Bioinformatics
    Input FASTQ
    Output BAM
    Use Alignment
    Version latest

%post
    apt-get update --fix-missing && apt-get install -y git g++ zlib1g gcc make zlib1g-dev curl && rm -rf /var/lib/apt/lists/*
    cd /opt/
    git clone https://github.com/lh3/bwa.git
    cd bwa; make
    apt-get autoclean
    apt-get remove -y git g++ gcc make curl
    chmod -R 777 /opt/bwa

%runscript
    exec /opt/bwa/bwa "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

