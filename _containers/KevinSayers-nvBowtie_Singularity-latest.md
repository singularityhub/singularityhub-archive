---
id: 662
name: "KevinSayers/nvBowtie_Singularity"
branch: "master"
tag: "latest"
commit: "857863c536871885c43aa7507a23e883616fa9be"
version: "302f49037dbdd5596eb6baed242b0629"
build_date: "2017-11-04T04:49:58.762Z"
size_mb: 2141
size: 1063931935
sif: "https://datasets.datalad.org/shub/KevinSayers/nvBowtie_Singularity/latest/2017-11-04-857863c5-302f4903/302f49037dbdd5596eb6baed242b0629.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/KevinSayers/nvBowtie_Singularity/latest/2017-11-04-857863c5-302f4903/
recipe: https://datasets.datalad.org/shub/KevinSayers/nvBowtie_Singularity/latest/2017-11-04-857863c5-302f4903/Singularity
collection: KevinSayers/nvBowtie_Singularity
---

# KevinSayers/nvBowtie_Singularity:latest

```bash
$ singularity pull shub://KevinSayers/nvBowtie_Singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: nvidia/cuda:8.0-devel

%post
    apt-get update
    apt-get -y install wget build-essential zlib1g-dev
    wget http://www.cmake.org/files/v3.2/cmake-3.2.2.tar.gz
    tar xf cmake-3.2.2.tar.gz
    cd cmake-3.2.2
    ./configure
    make install
    wget https://github.com/NVlabs/nvbio/archive/v1.1.00.tar.gz
    tar -xvf v1.1.00.tar.gz 
    cd nvbio-1.1.00/
    mkdir build
    cd build/
    cmake ..
    cd nvBowtie/
    make
    mv nvBowtie /usr/local/bin/nvBowtie
    cd ../nvBWT
    make
    mv nvBWT /usr/local/bin/nvBWT
```

## Collection

 - Name: [KevinSayers/nvBowtie_Singularity](https://github.com/KevinSayers/nvBowtie_Singularity)
 - License: None

