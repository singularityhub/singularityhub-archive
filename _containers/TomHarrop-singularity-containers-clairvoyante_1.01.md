---
id: 7832
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "clairvoyante_1.01"
commit: "df886f799b27e6efba6761d844db84e2664b12cb"
version: "ee7b6555fb8153dad761f8251ff74dd0"
build_date: "2019-03-19T05:26:45.999Z"
size_mb: 7289
size: 3239407647
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/clairvoyante_1.01/2019-03-19-df886f79-ee7b6555/ee7b6555fb8153dad761f8251ff74dd0.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/clairvoyante_1.01/2019-03-19-df886f79-ee7b6555/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/clairvoyante_1.01/2019-03-19-df886f79-ee7b6555/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:clairvoyante_1.01

```bash
$ singularity pull shub://TomHarrop/singularity-containers:clairvoyante_1.01
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

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

