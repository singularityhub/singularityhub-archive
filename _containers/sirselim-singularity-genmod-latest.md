---
id: 12510
name: "sirselim/singularity-genmod"
branch: "master"
tag: "latest"
commit: "8b38c623c27c62eeb3d62e46e3fdedc2056e856b"
version: "f733c57041d70e24cba7120a77e2a32f"
build_date: "2020-07-30T01:27:34.891Z"
size_mb: 559.0
size: 218857503
sif: "https://datasets.datalad.org/shub/sirselim/singularity-genmod/latest/2020-07-30-8b38c623-f733c570/f733c57041d70e24cba7120a77e2a32f.sif"
url: https://datasets.datalad.org/shub/sirselim/singularity-genmod/latest/2020-07-30-8b38c623-f733c570/
recipe: https://datasets.datalad.org/shub/sirselim/singularity-genmod/latest/2020-07-30-8b38c623-f733c570/Singularity
collection: sirselim/singularity-genmod
---

# sirselim/singularity-genmod:latest

```bash
$ singularity pull shub://sirselim/singularity-genmod:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help
    This is a container for installing genmod version 3.7.3

%labels
    MAINTAINER Miles Benton
    VERSION 0.1

%environment
    export LC_ALL=C
    export PATH=/usr/games:$PATH

%post
    apt-get -y update
    apt-get -y install python-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev python-pip
    pip install genmod
```

## Collection

 - Name: [sirselim/singularity-genmod](https://github.com/sirselim/singularity-genmod)
 - License: None

