---
id: 4415
name: "dominik-handler/AP_singu"
branch: "master"
tag: "racon"
commit: "11da4aee8f163e3881405ac0d50f2fefb4f5f185"
version: "7f441221c74177b0e7281aaf034a95e2833d7d11d3b8db445144d168b2b3a66e"
build_date: "2020-06-18T12:04:02.490Z"
size_mb: 278.8984375
size: 292446208
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/racon/2020-06-18-11da4aee-7f441221/7f441221c74177b0e7281aaf034a95e2833d7d11d3b8db445144d168b2b3a66e.sif"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/racon/2020-06-18-11da4aee-7f441221/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/racon/2020-06-18-11da4aee-7f441221/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:racon

```bash
$ singularity pull shub://dominik-handler/AP_singu:racon
```

## Singularity Recipe

```singularity
#Racon in singularity

Bootstrap: docker
From: ubuntu:16.04

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at>
  racon v1.4.3 (871c8de)

%runscript
    racon "$@"

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
    # apt-get -y install mummer     
    # apt-get -y install python-numpy  
    # apt-get -y install python-matplotlib      
     apt-get -y install git-core   

    cd / 
    git clone --recursive https://github.com/isovic/racon.git racon
    cd racon
    mkdir build
    cd build
    cmake -DCMAKE_BUILD_TYPE=Release -Dracon_build_wrapper=ON ..
    make install

    apt-get autoremove
    
%test
    racon -h
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

