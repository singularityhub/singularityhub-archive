---
id: 2014
name: "TomRoussel/Bazel-Singularity"
branch: "master"
tag: "latest"
commit: "b90bff3c4b037519e959945da90033451f68d01a"
version: "24296ecf252450058f47ba6feea647b7"
build_date: "2018-03-09T10:25:28.085Z"
size_mb: 3542
size: 1828089887
sif: "https://datasets.datalad.org/shub/TomRoussel/Bazel-Singularity/latest/2018-03-09-b90bff3c-24296ecf/24296ecf252450058f47ba6feea647b7.simg"
url: https://datasets.datalad.org/shub/TomRoussel/Bazel-Singularity/latest/2018-03-09-b90bff3c-24296ecf/
recipe: https://datasets.datalad.org/shub/TomRoussel/Bazel-Singularity/latest/2018-03-09-b90bff3c-24296ecf/Singularity
collection: TomRoussel/Bazel-Singularity
---

# TomRoussel/Bazel-Singularity:latest

```bash
$ singularity pull shub://TomRoussel/Bazel-Singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.1-cudnn7-devel-ubuntu16.04

%setup
%post
    # Make sure cuda is in the right place
    ln -s /usr/local/cuda/lib64/stubs/libcuda.so /usr/local/cuda/lib64/libcuda.so.1 
    # apt install -y python3-numpy python3-dev python3-pip python3-wheel
    apt update && apt upgrade -y
    apt install -y git libcupti-dev locales openjdk-8-jdk curl openssl libssl-dev
    echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list
    curl https://bazel.build/bazel-release.pub.gpg | apt-key add -
    apt update && apt install -y bazel

    # Locales were messed up for some reason, manually setting otherwise pip will complain
    dpkg-reconfigure locales
    locale-gen en_US.UTF-8
    export LC_ALL=en_US.UTF-8

    # Install python 3.6
    curl https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tar.xz | tar xJf -
    cd Python-3.6.4
    ./configure
    make -j6
    make install
    # Clean up python source code
    cd / && rm -rf Python-3.6.4

    yes | pip3 install six numpy wheel numpy

    # TF dependency TODO: Try linking python to python3
    apt install -y python2.7-minimal

    ln -s /usr/bin/python2.7 /usr/bin/python
```

## Collection

 - Name: [TomRoussel/Bazel-Singularity](https://github.com/TomRoussel/Bazel-Singularity)
 - License: None

