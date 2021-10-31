---
id: 4081
name: "dominik-handler/AP_singu"
branch: "master"
tag: "mummer"
commit: "d1ba2e26976dcd2b36ab6ebbf27d4d45e875668f"
version: "f088f6e930c0af1d836160dc78715710"
build_date: "2021-02-26T21:44:07.319Z"
size_mb: 1164
size: 499740703
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/mummer/2021-02-26-d1ba2e26-f088f6e9/f088f6e930c0af1d836160dc78715710.simg"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/mummer/2021-02-26-d1ba2e26-f088f6e9/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/mummer/2021-02-26-d1ba2e26-f088f6e9/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:mummer

```bash
$ singularity pull shub://dominik-handler/AP_singu:mummer
```

## Singularity Recipe

```singularity
#graphmap in singularity

BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%runscript
    mummerpath=/mummer-4.0.0beta2/
    export PATH=:$mummerpath:$PATH
    exec "$@"

%post
    apt-get --assume-yes install wget
    apt-get --assume-yes install sudo

    sudo apt-get update
    sudo apt-get -y install build-essential
    sudo apt-get -y install zlib1g
    sudo apt-get -y install cmake
    sudo apt-get update

    sudo apt-get -y install git-core   
    sudo apt-get -y install zlib1g-dev     
    
    sudo apt-get -y install software-properties-common
    sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main universe restricted multiverse"
    sudo apt-get update
    
    sudo apt-get -y install gnuplot gnuplot-x11 gnuplot-doc 
    sudo apt-get -y install xfig transfig xfig-libs
           
    cd /
    wget https://github.com/mummer4/mummer/releases/download/v4.0.0beta2/mummer-4.0.0beta2.tar.gz
    tar -zxvf mummer-4.0.0beta2.tar.gz
    cd /mummer-4.0.0beta2/
    ./configure LDFLAGS=-static
    make
    sudo make install
    sudo ldconfig
    
    mummerpath=/mummer-4.0.0beta2/
    export PATH=:$mummerpath:$PATH
    nucmer -h
    delta-filter -h
    
    sudo mkdir /groups
    sudo mkdir /scratch
    sudo mkdir /scratch-ii2
    sudo mkdir /clustertmp

%test
    #mummerpath=/mummer-4.0.0beta2/
    #export PATH=:$mummerpath:$PATH
    #mummer -h
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

