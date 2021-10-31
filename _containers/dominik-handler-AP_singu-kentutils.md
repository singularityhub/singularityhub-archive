---
id: 4804
name: "dominik-handler/AP_singu"
branch: "master"
tag: "kentutils"
commit: "65d3ee3c2d4f42f544cc987646be86d31b9ade9d"
version: "881f23eb840ac6c7561ec99181e5d0b1"
build_date: "2020-03-31T12:55:23.512Z"
size_mb: 1750
size: 633561119
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/kentutils/2020-03-31-65d3ee3c-881f23eb/881f23eb840ac6c7561ec99181e5d0b1.simg"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/kentutils/2020-03-31-65d3ee3c-881f23eb/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/kentutils/2020-03-31-65d3ee3c-881f23eb/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:kentutils

```bash
$ singularity pull shub://dominik-handler/AP_singu:kentutils
```

## Singularity Recipe

```singularity
#ngmlr in singularity

Bootstrap: docker
From: ubuntu:16.04

%runscript

   "$@"

%post
    apt-get update
    apt-get --assume-yes install build-essential zlib1g libpng-dev cmake git-core wget zlib1g-dev uuid-dev

    apt-get clean && apt-get update && apt-get install -y \
       locales \
       language-pack-fi  \
       language-pack-en && \
       export LANGUAGE=en_US.UTF-8 && \
       export LANG=en_US.UTF-8 && \
       export LC_ALL=en_US.UTF-8 && \
       locale-gen en_US.UTF-8 && \
       dpkg-reconfigure --frontend noninteractive locales

    
    apt-get update
    apt-get --assume-yes install mysql-client libssl-dev openssl libmysqlclient-dev  
    
    mkdir -p /Software
    cd /Software
    #git clone git://github.com/ENCODE-DCC/kentUtils.git
    wget http://hgdownload.soe.ucsc.edu/admin/exe/userApps.v358.src.tgz
    tar zxvf userApps.v358.src.tgz 
    mv userApps kentUtils

    cd kentUtils
    make
    
    mkdir /groups
    mkdir /clustertmp
    mkdir /scratch
    mkdir /scratch-ii2

%environment
  export  PATH="/Software/kentUtils/bin:$PATH"
  export HOME="/Software/kentUtils/"

%test
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

