---
id: 14309
name: "ArnaudBelcour/metage2metabo-metacom_singularity"
branch: "master"
tag: "latest"
commit: "73eecfcac136af1c4ae502404daf25e3d939ada3"
version: "c6ea7e7b31f52c739aec9c9f0f38b8a8"
build_date: "2021-03-17T18:47:08.735Z"
size_mb: 849.0
size: 318910495
sif: "https://datasets.datalad.org/shub/ArnaudBelcour/metage2metabo-metacom_singularity/latest/2021-03-17-73eecfca-c6ea7e7b/c6ea7e7b31f52c739aec9c9f0f38b8a8.sif"
url: https://datasets.datalad.org/shub/ArnaudBelcour/metage2metabo-metacom_singularity/latest/2021-03-17-73eecfca-c6ea7e7b/
recipe: https://datasets.datalad.org/shub/ArnaudBelcour/metage2metabo-metacom_singularity/latest/2021-03-17-73eecfca-c6ea7e7b/Singularity
collection: ArnaudBelcour/metage2metabo-metacom_singularity
---

# ArnaudBelcour/metage2metabo-metacom_singularity:latest

```bash
$ singularity pull shub://ArnaudBelcour/metage2metabo-metacom_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%labels
    Maintainer Belcour A.
    Version v1.5.0
    Description Metage2Metabo metacom Singularity recipe

%environment
     export PYTHONIOENCODING=utf8

%post
     apt-get -y update && \
     DEBIAN_FRONTEND=noninteractive apt-get install -y \
     curl \
     git \
     python3.8-dev \
     python3.8-distutils ;\
     apt-get clean ;\
     apt-get purge ;\
     curl https://bootstrap.pypa.io/get-pip.py | python3;\
     pip install graphviz;\
     pip install padmet clyngor-with-clingo clyngor pandas pipdeptree==0.13.2;\
     pip install powergrasp ete3;\
     pip install Metage2Metabo==1.5.0
```

## Collection

 - Name: [ArnaudBelcour/metage2metabo-metacom_singularity](https://github.com/ArnaudBelcour/metage2metabo-metacom_singularity)
 - License: None

