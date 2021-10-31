---
id: 13540
name: "bast/openmpi"
branch: "master"
tag: "4.0.4-gcc-9.3.0"
commit: "c49ffbed6d937ca6266f25c2fe621e525902c90d"
version: "18e68941f2e58e94d4d8f033e95d18e776f20eace6c6cd79bae1c897455212fc"
build_date: "2021-02-01T15:32:49.604Z"
size_mb: 244.65234375
size: 256536576
sif: "https://datasets.datalad.org/shub/bast/openmpi/4.0.4-gcc-9.3.0/2021-02-01-c49ffbed-18e68941/18e68941f2e58e94d4d8f033e95d18e776f20eace6c6cd79bae1c897455212fc.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/bast/openmpi/4.0.4-gcc-9.3.0/2021-02-01-c49ffbed-18e68941/
recipe: https://datasets.datalad.org/shub/bast/openmpi/4.0.4-gcc-9.3.0/2021-02-01-c49ffbed-18e68941/Singularity
collection: bast/openmpi
---

# bast/openmpi:4.0.4-gcc-9.3.0

```bash
$ singularity pull shub://bast/openmpi:4.0.4-gcc-9.3.0
```

## Singularity Recipe

```singularity
BootStrap: library
From: ubuntu:20.04

%post
    apt-get install -y software-properties-common
    add-apt-repository universe
    apt-get update -y
    apt-get install -y build-essential g++ gfortran wget ssh
    apt-get clean

    wget https://download.open-mpi.org/release/open-mpi/v4.0/openmpi-4.0.4.tar.gz
    tar zxf openmpi-4.0.4.tar.gz
    cd openmpi-4.0.4
    ./configure
    make
    make install
    ldconfig

%environment
    export LC_ALL=C

%labels
    Author radovan.bast@uit.no
```

## Collection

 - Name: [bast/openmpi](https://github.com/bast/openmpi)
 - License: None

