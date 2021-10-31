---
id: 11473
name: "TomHarrop/ont-containers"
branch: "master"
tag: "qcat_1.0.1"
commit: "8da36bb7bb56009a4263f05bcd0f5e4d06fe5e75"
version: "40d727a5e6aa199a69f3eec7f8d8c813bc9795e73a6c9e23dfe0ac539bf51805"
build_date: "2019-11-03T22:32:26.318Z"
size_mb: 180.796875
size: 189579264
sif: "https://datasets.datalad.org/shub/TomHarrop/ont-containers/qcat_1.0.1/2019-11-03-8da36bb7-40d727a5/40d727a5e6aa199a69f3eec7f8d8c813bc9795e73a6c9e23dfe0ac539bf51805.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/ont-containers/qcat_1.0.1/2019-11-03-8da36bb7-40d727a5/
recipe: https://datasets.datalad.org/shub/TomHarrop/ont-containers/qcat_1.0.1/2019-11-03-8da36bb7-40d727a5/Singularity
collection: TomHarrop/ont-containers
---

# TomHarrop/ont-containers:qcat_1.0.1

```bash
$ singularity pull shub://TomHarrop/ont-containers:qcat_1.0.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.7.3-alpine3.9

%help
    qcat 1.0.1

%labels
    MAINTAINER "Tom Harrop"
    VERSION "qcat 1.0.1"


%post
    apk add -u \
        bash \
        build-base \
        perl

    pip3 install qcat==1.0.1

%runscript
    exec /usr/local/bin/qcat "$@"
```

## Collection

 - Name: [TomHarrop/ont-containers](https://github.com/TomHarrop/ont-containers)
 - License: None

