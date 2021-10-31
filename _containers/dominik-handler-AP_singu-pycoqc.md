---
id: 6321
name: "dominik-handler/AP_singu"
branch: "master"
tag: "pycoqc"
commit: "e2922ff891d0baac1f786da66f7644ce1fe961be"
version: "764a67ae696f62c9dd1ddaf6c416b66c"
build_date: "2020-03-31T12:47:43.046Z"
size_mb: 920
size: 381059103
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/pycoqc/2020-03-31-e2922ff8-764a67ae/764a67ae696f62c9dd1ddaf6c416b66c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/pycoqc/2020-03-31-e2922ff8-764a67ae/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/pycoqc/2020-03-31-e2922ff8-764a67ae/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:pycoqc

```bash
$ singularity pull shub://dominik-handler/AP_singu:pycoqc
```

## Singularity Recipe

```singularity
#nanoplot in singularity

Bootstrap: docker
From: ubuntu:16.04


%runscript
    pycoQC "$@"

%post
    apt-get update
    apt-get -y install wget curl
    apt-get -y install sudo build-essential

    apt-get update
    apt-get install bzip2
    apt-get -y install python3.5-dev

    apt-get -y install python3-setuptools
    
    wget "https://bootstrap.pypa.io/get-pip.py" 
    python3 get-pip.py

    pip3 install setuptools --upgrade
    pip3 install pycoQC
    
    mkdir /groups
    mkdir /scratch
    mkdir /scratch-ii2


%test
    pycoQC -h
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

