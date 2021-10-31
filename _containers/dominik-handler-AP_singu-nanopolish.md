---
id: 3695
name: "dominik-handler/AP_singu"
branch: "master"
tag: "nanopolish"
commit: "5648d69b61853100663977696bf3315de2e54fbd"
version: "a68ed6909317feb58319c77fbacf77fc"
build_date: "2019-04-03T14:45:46.265Z"
size_mb: 927
size: 304865311
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/nanopolish/2019-04-03-5648d69b-a68ed690/a68ed6909317feb58319c77fbacf77fc.simg"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/nanopolish/2019-04-03-5648d69b-a68ed690/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/nanopolish/2019-04-03-5648d69b-a68ed690/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:nanopolish

```bash
$ singularity pull shub://dominik-handler/AP_singu:nanopolish
```

## Singularity Recipe

```singularity
#nanopolish in singularity

Bootstrap: docker
From: ubuntu:16.04

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at  
  Nanopolish v0.11.1

%runscript
    /nanopolish/nanopolish "$@"

%post
    apt-get update
    apt-get -y install wget
    apt-get -y install sudo

    apt-get update
    apt-get -y install build-essential
    apt-get -y install zlib1g
    apt-get install zlib1g-dev
    apt-get -y install git-core  

    apt-get -y install python3.5
    apt-get -y install python3-setuptools
    easy_install3 pip
    pip install biopython

    cd /
    git clone --recursive https://github.com/jts/nanopolish.git
    cd nanopolish

    make 
    mkdir /groups
    mkdir /clustertmp
    mkdir /scratch
    mkdir /scratch-ii2

%test
    /nanopolish/nanopolish
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

