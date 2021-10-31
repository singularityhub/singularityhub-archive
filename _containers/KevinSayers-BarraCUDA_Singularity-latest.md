---
id: 396
name: "KevinSayers/BarraCUDA_Singularity"
branch: "master"
tag: "latest"
commit: "e80961de865eb5a66c4db972af1371120826437a"
version: "ee404afe5ed61527b5ea131b6c96cf92"
build_date: "2017-10-18T17:55:06.048Z"
size_mb: 1755
size: 982384671
sif: "https://datasets.datalad.org/shub/KevinSayers/BarraCUDA_Singularity/latest/2017-10-18-e80961de-ee404afe/ee404afe5ed61527b5ea131b6c96cf92.simg"
url: https://datasets.datalad.org/shub/KevinSayers/BarraCUDA_Singularity/latest/2017-10-18-e80961de-ee404afe/
recipe: https://datasets.datalad.org/shub/KevinSayers/BarraCUDA_Singularity/latest/2017-10-18-e80961de-ee404afe/Singularity
collection: KevinSayers/BarraCUDA_Singularity
---

# KevinSayers/BarraCUDA_Singularity:latest

```bash
$ singularity pull shub://KevinSayers/BarraCUDA_Singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:8.0-devel

%post
    apt-get update
    apt-get -y install wget build-essential zlib1g-dev
    wget https://vorboss.dl.sourceforge.net/project/seqbarracuda/Source%20Code/Version%200.7.0/barracuda_0.7.107h.tar.gz
    tar xvf barracuda_0.7.107h.tar.gz 
    cd barracuda
    make all
    mv bin/barracuda /usr/local/bin/barracuda
```

## Collection

 - Name: [KevinSayers/BarraCUDA_Singularity](https://github.com/KevinSayers/BarraCUDA_Singularity)
 - License: None

