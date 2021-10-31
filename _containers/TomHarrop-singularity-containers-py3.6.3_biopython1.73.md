---
id: 8801
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "py3.6.3_biopython1.73"
commit: "b1a188ec3225be702035ca8fbca5f1e79a8626a2"
version: "98d1b75009a4e2eba88d834787d37dcb"
build_date: "2019-05-03T14:43:26.233Z"
size_mb: 1037
size: 359714847
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/py3.6.3_biopython1.73/2019-05-03-b1a188ec-98d1b750/98d1b75009a4e2eba88d834787d37dcb.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/py3.6.3_biopython1.73/2019-05-03-b1a188ec-98d1b750/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/py3.6.3_biopython1.73/2019-05-03-b1a188ec-98d1b750/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:py3.6.3_biopython1.73

```bash
$ singularity pull shub://TomHarrop/singularity-containers:py3.6.3_biopython1.73
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.6.3-stretch

%help

    Python 3.6.3 with Biopython 1.73
    
%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "Biopython 1.73"

%runscript

    exec /usr/local/bin/python "$@"

%post
    /usr/local/bin/pip3 install \
        biopython==1.73
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

