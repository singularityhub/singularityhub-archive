---
id: 12079
name: "TomHarrop/py-containers"
branch: "master"
tag: "biopython_1.73"
commit: "fb14371bdbe651e7ca8587e3737e4cfd8b2a636f"
version: "db0d7b249d9f5eca4c3b51f632a5ace5017a382339dd8482f5ed0df30eb43dd4"
build_date: "2020-12-17T21:23:59.628Z"
size_mb: 355.2578125
size: 372514816
sif: "https://datasets.datalad.org/shub/TomHarrop/py-containers/biopython_1.73/2020-12-17-fb14371b-db0d7b24/db0d7b249d9f5eca4c3b51f632a5ace5017a382339dd8482f5ed0df30eb43dd4.sif"
url: https://datasets.datalad.org/shub/TomHarrop/py-containers/biopython_1.73/2020-12-17-fb14371b-db0d7b24/
recipe: https://datasets.datalad.org/shub/TomHarrop/py-containers/biopython_1.73/2020-12-17-fb14371b-db0d7b24/Singularity
collection: TomHarrop/py-containers
---

# TomHarrop/py-containers:biopython_1.73

```bash
$ singularity pull shub://TomHarrop/py-containers:biopython_1.73
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.7.3-stretch

%help

    Python 3.7.3 with Biopython 1.73
    
%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "Biopython 1.73"

%runscript

    exec /usr/local/bin/python "$@"

%post
    /usr/local/bin/pip3 install \
        biopython==1.73 \
        intermine==1.11.0
```

## Collection

 - Name: [TomHarrop/py-containers](https://github.com/TomHarrop/py-containers)
 - License: None

