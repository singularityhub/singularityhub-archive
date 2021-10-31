---
id: 5286
name: "dominik-handler/AP_singu"
branch: "master"
tag: "ngmlr"
commit: "fad2f9686182d0f4360ef6feef654d8326800612"
version: "8664ef69ded501fb18f90ecbf1f808cb"
build_date: "2020-01-30T14:23:06.134Z"
size_mb: 604
size: 309137439
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/ngmlr/2020-01-30-fad2f968-8664ef69/8664ef69ded501fb18f90ecbf1f808cb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/ngmlr/2020-01-30-fad2f968-8664ef69/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/ngmlr/2020-01-30-fad2f968-8664ef69/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:ngmlr

```bash
$ singularity pull shub://dominik-handler/AP_singu:ngmlr
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

