---
id: 4977
name: "bbbbbrie/moses-container"
branch: "master"
tag: "latest"
commit: "299683af97ded8af5c9b6237a3516660549807e1"
version: "16491a4aac1883d8ddbab732e927fb94"
build_date: "2018-09-26T06:55:03.875Z"
size_mb: 2004
size: 813482015
sif: "https://datasets.datalad.org/shub/bbbbbrie/moses-container/latest/2018-09-26-299683af-16491a4a/16491a4aac1883d8ddbab732e927fb94.simg"
url: https://datasets.datalad.org/shub/bbbbbrie/moses-container/latest/2018-09-26-299683af-16491a4a/
recipe: https://datasets.datalad.org/shub/bbbbbrie/moses-container/latest/2018-09-26-299683af-16491a4a/Singularity
collection: bbbbbrie/moses-container
---

# bbbbbrie/moses-container:latest

```bash
$ singularity pull shub://bbbbbrie/moses-container:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%runscript
    echo "I have Moses installed..."
    /opt/moses/built/bin/moses --version

#%environment
#    LD_LIBRARY_PATH=/usr/local/cuda-9.0/cuda/lib64:/usr/local/cuda-9.0/lib64

# %setup

%post
    sed -i 's/$/ universe/' /etc/apt/sources.list
    mkdir /projects /scratch
    apt-get -y update
    apt-get -y install build-essential git-core pkg-config automake libtool wget zlib1g-dev python-dev libbz2-dev libsoap-lite-perl
    mkdir -p /opt/moses
    cd /opt/moses/ && git clone https://github.com/moses-smt/mosesdecoder.git  && cd mosesdecoder && make -f contrib/Makefiles/install-dependencies.gmake && ./compile.sh --prefix=/opt/moses/built
```

## Collection

 - Name: [bbbbbrie/moses-container](https://github.com/bbbbbrie/moses-container)
 - License: None

