---
id: 3692
name: "dominik-handler/AP_singu"
branch: "master"
tag: "filtlong"
commit: "d1ba2e26976dcd2b36ab6ebbf27d4d45e875668f"
version: "68e6ad6fb5a189f2b7b169f0efbd4546"
build_date: "2020-03-31T12:47:36.534Z"
size_mb: 416
size: 163594271
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/filtlong/2020-03-31-d1ba2e26-68e6ad6f/68e6ad6fb5a189f2b7b169f0efbd4546.simg"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/filtlong/2020-03-31-d1ba2e26-68e6ad6f/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/filtlong/2020-03-31-d1ba2e26-68e6ad6f/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:filtlong

```bash
$ singularity pull shub://dominik-handler/AP_singu:filtlong
```

## Singularity Recipe

```singularity
#filtlong in singularity

Bootstrap: docker
From: ubuntu:16.04

%runscript
    /Filtlong/bin/filtlong "$@"

%post
    apt-get update
    apt-get --assume-yes install wget
    apt-get --assume-yes install sudo

    sudo apt-get update
    sudo apt-get -y install build-essential
    sudo apt-get -y install zlib1g
    sudo apt-get update

    apt-get update
    apt-get install --reinstall -y locales
    sed -i 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen
    locale-gen en_US.UTF-8
    LANG=en_US.UTF-8
    LANGUAGE=en_US 
    LC_ALL=en_US.UTF-8
    dpkg-reconfigure --frontend noninteractive locales


    sudo apt-get -y install git-core   
    sudo apt-get -y install zlib1g-dev 
 
    sudo apt-get update
    sudo apt-get -y install python3.5
    
    cd /
    git clone https://github.com/rrwick/Filtlong.git
    cd Filtlong
    make -j 2    
    
    sudo mkdir /groups
    sudo mkdir /clustertmp
    sudo mkdir /scratch

%test
    /Filtlong/bin/filtlong -h
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

