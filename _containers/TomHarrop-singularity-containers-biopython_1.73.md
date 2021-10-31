---
id: 8702
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "biopython_1.73"
commit: "a23222e39e47ad1bfe8150de7666ccdc9f783f49"
version: "4a2a83e0cdff509c33227ef55906c72c"
build_date: "2020-04-27T22:35:30.501Z"
size_mb: 1062
size: 366686239
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/biopython_1.73/2020-04-27-a23222e3-4a2a83e0/4a2a83e0cdff509c33227ef55906c72c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/biopython_1.73/2020-04-27-a23222e3-4a2a83e0/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/biopython_1.73/2020-04-27-a23222e3-4a2a83e0/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:biopython_1.73

```bash
$ singularity pull shub://TomHarrop/singularity-containers:biopython_1.73
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

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

