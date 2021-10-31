---
id: 8706
name: "netcatninja/fashionMNIST"
branch: "master"
tag: "latest"
commit: "fe5b32cb5d34953e18c890a4a7302a644a042e43"
version: "8a29455bac47b39af235e9d89327a82e"
build_date: "2019-04-29T05:02:48.486Z"
size_mb: 1419
size: 482754591
sif: "https://datasets.datalad.org/shub/netcatninja/fashionMNIST/latest/2019-04-29-fe5b32cb-8a29455b/8a29455bac47b39af235e9d89327a82e.simg"
url: https://datasets.datalad.org/shub/netcatninja/fashionMNIST/latest/2019-04-29-fe5b32cb-8a29455b/
recipe: https://datasets.datalad.org/shub/netcatninja/fashionMNIST/latest/2019-04-29-fe5b32cb-8a29455b/Singularity
collection: netcatninja/fashionMNIST
---

# netcatninja/fashionMNIST:latest

```bash
$ singularity pull shub://netcatninja/fashionMNIST:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%help
    Install Python 3.6 and TensorFlow
    Try out fashion MNIST.

%files
    fashionmnist.py /opt

%runscript
    /opt/python3/bin/python3.6 -V
    /opt/python3/bin/python3.6 /opt/fashionmnist.py
    
%environment
    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8
    export PATH=/opt/python3/bin:/usr/bin:/usr/local/sbin:/bin:/usr/local/bin:/usr/sbin:/sbin

%post
    apt-get -y update && apt-get install -y --no-install-recommends  \
    build-essential ca-certificates git libssl-dev wget zlib1g-dev
    cd /opt && wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tar.xz && \
    tar xf Python-3.6.8.tar.xz && cd Python-3.6.8 && ./configure --prefix=/opt/python3 && \
    make && make altinstall && ln -s /opt/python3/bin/python3.6 /opt/python3/bin/python3
    /opt/python3/bin/pip3.6 install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.13.1-cp36-cp36m-linux_x86_64.whl
    /opt/python3/bin/pip3.6 install matplotlib

%labels
    Author Brie Carranza
```

## Collection

 - Name: [netcatninja/fashionMNIST](https://github.com/netcatninja/fashionMNIST)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

