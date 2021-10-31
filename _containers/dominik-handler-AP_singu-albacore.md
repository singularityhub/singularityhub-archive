---
id: 3691
name: "dominik-handler/AP_singu"
branch: "master"
tag: "albacore"
commit: "08fe7e5f51dd94b61684d26eb7193bbcb6443f14"
version: "79bbb58a4a009d06f485c3ab62255b02"
build_date: "2018-10-18T17:22:05.075Z"
size_mb: 357
size: 141283359
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/albacore/2018-10-18-08fe7e5f-79bbb58a/79bbb58a4a009d06f485c3ab62255b02.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/albacore/2018-10-18-08fe7e5f-79bbb58a/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/albacore/2018-10-18-08fe7e5f-79bbb58a/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:albacore

```bash
$ singularity pull shub://dominik-handler/AP_singu:albacore
```

## Singularity Recipe

```singularity
#albacore in singularity

Bootstrap: docker
From: ubuntu:16.04

%runscript
    read_fast5_basecaller.py "$@"

%post
    apt-get update
    apt-get -y install wget
    apt-get -y install sudo

    apt-get update
    apt-get -y install python3.5

    apt-get -y install python3-setuptools
    easy_install3 pip

    mkdir -p /albacore/
    cd /albacore/
    wget https://mirror.oxfordnanoportal.com/software/analysis/ont_albacore-2.3.3-cp35-cp35m-manylinux1_x86_64.whl
          

    pip3 install ont_albacore-*.whl\
    
    mkdir /groups
    mkdir /clustertmp
    mkdir /scratch
    mkdir /scratch-ii2

%test
    read_fast5_basecaller.py -h
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

