---
id: 3362
name: "kma/HPC-Container"
branch: "master"
tag: "latest"
commit: "390ee6b05d6dd385d5f4553d265698c3e03e1584"
version: "9cc63e726ba110add5c669a150c3ae94"
build_date: "2018-06-29T20:46:11.670Z"
size_mb: 1335
size: 447762463
sif: "https://datasets.datalad.org/shub/kma/HPC-Container/latest/2018-06-29-390ee6b0-9cc63e72/9cc63e726ba110add5c669a150c3ae94.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kma/HPC-Container/latest/2018-06-29-390ee6b0-9cc63e72/
recipe: https://datasets.datalad.org/shub/kma/HPC-Container/latest/2018-06-29-390ee6b0-9cc63e72/Singularity
collection: kma/HPC-Container
---

# kma/HPC-Container:latest

```bash
$ singularity pull shub://kma/HPC-Container:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:xenial
%help
Fenics from ppa:fenics-packages/fenics
%label
Version 2017
Maintainer kma
%post
    # commands to be executed inside container during bootstrap
     apt-get update
    # install fenics
      apt-get -y install software-properties-common
      add-apt-repository ppa:fenics-packages/fenics
      apt-get update
      apt-get -y install --no-install-recommends fenics
      ## for matplotlib
      apt-get -y install python-tk

%runscript
    # commands to be executed when the container runs
    python "$@"
```

## Collection

 - Name: [kma/HPC-Container](https://github.com/kma/HPC-Container)
 - License: None

