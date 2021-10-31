---
id: 8995
name: "netcatninja/cookbook"
branch: "master"
tag: "fashionmnist"
commit: "f8be9f1c42ba66351b8530e9942d9a0857d61864"
version: "e3f0e48427be0c92408abc85f0357dda"
build_date: "2019-05-10T10:48:53.380Z"
size_mb: 1418
size: 482525215
sif: "https://datasets.datalad.org/shub/netcatninja/cookbook/fashionmnist/2019-05-10-f8be9f1c-e3f0e484/e3f0e48427be0c92408abc85f0357dda.simg"
url: https://datasets.datalad.org/shub/netcatninja/cookbook/fashionmnist/2019-05-10-f8be9f1c-e3f0e484/
recipe: https://datasets.datalad.org/shub/netcatninja/cookbook/fashionmnist/2019-05-10-f8be9f1c-e3f0e484/Singularity
collection: netcatninja/cookbook
---

# netcatninja/cookbook:fashionmnist

```bash
$ singularity pull shub://netcatninja/cookbook:fashionmnist
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

 - Name: [netcatninja/cookbook](https://github.com/netcatninja/cookbook)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

