---
id: 12080
name: "TomHarrop/py-containers"
branch: "master"
tag: "pandas_0.25.3"
commit: "fb14371bdbe651e7ca8587e3737e4cfd8b2a636f"
version: "26646bc455f8c15d2b94d5dcf7976cb546bf5e6192b6703199e52de14d962600"
build_date: "2020-11-11T22:00:31.096Z"
size_mb: 127.04296875
size: 133214208
sif: "https://datasets.datalad.org/shub/TomHarrop/py-containers/pandas_0.25.3/2020-11-11-fb14371b-26646bc4/26646bc455f8c15d2b94d5dcf7976cb546bf5e6192b6703199e52de14d962600.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/py-containers/pandas_0.25.3/2020-11-11-fb14371b-26646bc4/
recipe: https://datasets.datalad.org/shub/TomHarrop/py-containers/pandas_0.25.3/2020-11-11-fb14371b-26646bc4/Singularity
collection: TomHarrop/py-containers
---

# TomHarrop/py-containers:pandas_0.25.3

```bash
$ singularity pull shub://TomHarrop/py-containers:pandas_0.25.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.8.1-slim-buster

%help

    Python 3.8.1 with Pandas 0.25.3
    
%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "Pandas 0.25.3"

%runscript

    exec /usr/local/bin/python "$@"

%post
    /usr/local/bin/pip3 install --upgrade pip
    /usr/local/bin/pip3 install \
        pandas==0.25.3
```

## Collection

 - Name: [TomHarrop/py-containers](https://github.com/TomHarrop/py-containers)
 - License: None

