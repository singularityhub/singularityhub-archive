---
id: 9935
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "pychopper_0.6.1"
commit: "9863633dab653d12e138228e5a9ba491b88de3e5"
version: "2dc7b13692543bbe86fe95442fd8a7d1"
build_date: "2019-06-21T06:30:04.015Z"
size_mb: 1224
size: 441507871
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/pychopper_0.6.1/2019-06-21-9863633d-2dc7b136/2dc7b13692543bbe86fe95442fd8a7d1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/pychopper_0.6.1/2019-06-21-9863633d-2dc7b136/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/pychopper_0.6.1/2019-06-21-9863633d-2dc7b136/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:pychopper_0.6.1

```bash
$ singularity pull shub://TomHarrop/singularity-containers:pychopper_0.6.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.7.3-stretch

%help
    Python 3.7.3 with pychopper 0.6.1
    
%labels
    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "pychopper 0.6.1"

%runscript
    exec /usr/local/bin/cdna_classifier.py "$@"

%post
    /usr/local/bin/pip3 install \
        git+https://github.com/nanoporetech/pychopper.git@v0.6.1
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

