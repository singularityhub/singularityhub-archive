---
id: 3987
name: "dominik-handler/AP_singu"
branch: "master"
tag: "flye"
commit: "f2c01761558cefb04d5418e2bb552db0def30735"
version: "882fd607dfa7eba42f515b2092a3061a"
build_date: "2021-01-25T02:38:16.667Z"
size_mb: 748
size: 228524063
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/flye/2021-01-25-f2c01761-882fd607/882fd607dfa7eba42f515b2092a3061a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/flye/2021-01-25-f2c01761-882fd607/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/flye/2021-01-25-f2c01761-882fd607/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:flye

```bash
$ singularity pull shub://dominik-handler/AP_singu:flye
```

## Singularity Recipe

```singularity
#nanoplot in singularity

Bootstrap: docker
From: ubuntu:16.04

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at  
  flye v.2.4.1

%runscript
    flye "$@"

%post
     apt-get update
     apt-get -y install wget

     apt-get update
     apt-get -y install software-properties-common
     add-apt-repository universe
     apt-get update

     apt-get update
     apt-get -y install build-essential cmake
     apt-get -y install zlib1g-dev   
     apt-get -y install git-core   

    apt-get update
    apt-get install bzip2
    apt-get -y install python2.7

    apt-get -y install python-setuptools build-essential
    
    git clone https://github.com/fenderglass/Flye
    cd Flye
    python setup.py build
    python setup.py install

    mkdir /groups
    mkdir /scratch
    mkdir /scratch-ii2


%test

    flye -h
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

