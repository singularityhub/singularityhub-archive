---
id: 11474
name: "TomHarrop/ont-containers"
branch: "master"
tag: "clairvoyante_1.01"
commit: "a178eadd1dfde2e18a644ada4d9c01edce58508b"
version: "8b10ad063726de241f9383a1510cdf80ab22b6af9dd30aa68e45d50d62ce5795"
build_date: "2019-11-03T22:57:52.704Z"
size_mb: 6698.0
size: 3240517632
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/clairvoyante_1.01/2019-11-03-a178eadd-8b10ad06/8b10ad063726de241f9383a1510cdf80ab22b6af9dd30aa68e45d50d62ce5795.sif"
url: https://datasets.datalad.org/shub/TomHarrop/ont-containers/clairvoyante_1.01/2019-11-03-a178eadd-8b10ad06/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/clairvoyante_1.01/2019-11-03-a178eadd-8b10ad06/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:clairvoyante_1.01

```bash
$ singularity pull shub://TomHarrop/ont-containers:clairvoyante_1.01
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: opensciencegrid/osgvo-tensorflow-gpu:latest

%help
    Clairvoyante 1.01
    https://github.com/aquaskyline/Clairvoyante/releases
    
%labels
    MAINTAINER "Tom Harrop (twharrop@gmail.com) "
    VERSION "Clairvoyante 1.01"

%runscript
    exec /usr/bin/python2 /clairvoyante/clairvoyante.py "$@"

%post
    # dependencies
    /usr/local/bin/pip2 install --upgrade \
        blosc \
        intervaltree==2.1.0

    /usr/local/bin/pip3 install --upgrade \
        blosc \
        intervaltree==2.1.0

    # pypy
    apt-get update
    apt-get install -y \
        pypy \
        pypy-dev

    wget https://bootstrap.pypa.io/get-pip.py && \
        pypy get-pip.py &&\
        rm get-pip.py
    pypy -m pip install intervaltree 

    # install clairvoyante
    mkdir clairvoyante
    wget -O "clairvoyante.tar.gz" \
        --no-check-certificate \
        https://github.com/aquaskyline/Clairvoyante/archive/v1.01.tar.gz
    tar -zxf clairvoyante.tar.gz \
        -C clairvoyante \
        --strip-components 1

    cd clairvoyante || exit 1
    curl http://www.bio8.cs.hku.hk/trainedModels.tbz | tar -jxf -

%environment
    export PATH="${PATH}:/clairvoyante/clairvoyante:/clairvoyante/dataPrepScripts"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

