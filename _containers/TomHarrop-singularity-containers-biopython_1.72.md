---
id: 5683
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "biopython_1.72"
commit: "87c95e887641a0f7b4caf384c1a8661a8f8f9e9d"
version: "950b59af71aced8b0bcca297af4fef49"
build_date: "2018-11-22T17:35:47.743Z"
size_mb: 1036
size: 356179999
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/biopython_1.72/2018-11-22-87c95e88-950b59af/950b59af71aced8b0bcca297af4fef49.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/biopython_1.72/2018-11-22-87c95e88-950b59af/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/biopython_1.72/2018-11-22-87c95e88-950b59af/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:biopython_1.72

```bash
$ singularity pull shub://TomHarrop/singularity-containers:biopython_1.72
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.6.6-stretch

%help

    Python 3.6.6 with Biopython 1.72
    
%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "Biopython 1.72"

%runscript

    exec /usr/local/bin/python "$@"

%post
    pip3 install biopython==1.72 intermine
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

