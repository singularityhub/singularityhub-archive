---
id: 8084
name: "darachm/bartender_munge"
branch: "master"
tag: "latest"
commit: "f10756137cfe16665a2f09be2486b562e6e2de53"
version: "7cec9e9ba03f721e4ce9539da8f1b889"
build_date: "2019-04-03T00:18:37.743Z"
size_mb: 1157
size: 663027743
sif: "https://datasets.datalad.org/shub/darachm/bartender_munge/latest/2019-04-03-f1075613-7cec9e9b/7cec9e9ba03f721e4ce9539da8f1b889.simg"
url: https://datasets.datalad.org/shub/darachm/bartender_munge/latest/2019-04-03-f1075613-7cec9e9b/
recipe: https://datasets.datalad.org/shub/darachm/bartender_munge/latest/2019-04-03-f1075613-7cec9e9b/Singularity
collection: darachm/bartender_munge
---

# darachm/bartender_munge:latest

```bash
$ singularity pull shub://darachm/bartender_munge:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
MAINTAINER darachm

%help

    This container is for providing `bartender` for some bioinformatic pipelines.
    
%post

    apt-get -y update
    apt-get -y update
    apt-get -y install python3 python3-biopython python3-pip
    apt-get -y install gcc-4.8 git make g++ python
    pip3 install regex numpy pandas jellyfish
    git clone https://github.com/LaoZZZZZ/bartender-1.1.git
    cd bartender-1.1
    make all
    make install

%test

    /usr/bin/python3 -V
```

## Collection

 - Name: [darachm/bartender_munge](https://github.com/darachm/bartender_munge)
 - License: None

