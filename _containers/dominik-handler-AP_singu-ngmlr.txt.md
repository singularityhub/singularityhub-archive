---
id: 5285
name: "dominik-handler/AP_singu"
branch: "master"
tag: "ngmlr.txt"
commit: "d1ba2e26976dcd2b36ab6ebbf27d4d45e875668f"
version: "05fd3546dc548192249e5893483a218c"
build_date: "2019-01-15T15:20:37.355Z"
size_mb: 604
size: 309137439
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/ngmlr.txt/2019-01-15-d1ba2e26-05fd3546/05fd3546dc548192249e5893483a218c.simg"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/ngmlr.txt/2019-01-15-d1ba2e26-05fd3546/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/ngmlr.txt/2019-01-15-d1ba2e26-05fd3546/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:ngmlr.txt

```bash
$ singularity pull shub://dominik-handler/AP_singu:ngmlr.txt
```

## Singularity Recipe

```singularity
#ngmlr in singularity

BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%runscript
    /ngmlr/bin/ngmlr-*/ngmlr "$@"

%post
    apt-get --assume-yes install wget
    apt-get --assume-yes install sudo

    sudo apt-get update
    sudo apt-get --assume-yes install build-essential
    sudo apt-get --assume-yes install zlib1g
    sudo apt-get --assume-yes install cmake
    sudo apt-get update
    sudo apt-get --assume-yes install git-core   
    sudo apt-get --assume-yes install zlib1g-dev     
    
    cd /
    git clone https://github.com/philres/ngmlr.git
    cd ngmlr/
    mkdir -p build
    cd build/
    cmake ..
    make

    cd ../bin/ngmlr-*/

    
    sudo mkdir /groups
    sudo mkdir /clustertmp

%test
    /ngmlr/bin/ngmlr-*/ngmlr -h
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

