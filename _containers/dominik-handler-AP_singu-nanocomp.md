---
id: 6198
name: "dominik-handler/AP_singu"
branch: "master"
tag: "nanocomp"
commit: "8bf52d42433c89e374dbf53a358270fa6c8c5b2e"
version: "6dde5ece9a6d7b59e13c3bae7d49d609"
build_date: "2020-03-31T11:42:46.964Z"
size_mb: 1050
size: 431546399
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/nanocomp/2020-03-31-8bf52d42-6dde5ece/6dde5ece9a6d7b59e13c3bae7d49d609.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/nanocomp/2020-03-31-8bf52d42-6dde5ece/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/nanocomp/2020-03-31-8bf52d42-6dde5ece/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:nanocomp

```bash
$ singularity pull shub://dominik-handler/AP_singu:nanocomp
```

## Singularity Recipe

```singularity
#nanoplot in singularity

Bootstrap: docker
From: ubuntu:16.04


%runscript
    NanoComp "$@"

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

    pip install setuptools --upgrade
    pip install NanoComp
    
    mkdir /groups
    mkdir /scratch
    mkdir /scratch-ii2


%test
    NanoComp -h
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

