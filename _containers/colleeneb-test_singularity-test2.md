---
id: 9085
name: "colleeneb/test_singularity"
branch: "master"
tag: "test2"
commit: "84195d6e67333ca2cf2583135fdd0b7509a2c16e"
version: "043d1156dd901b0b4a3c1a7daa43dc69"
build_date: "2019-05-16T02:35:17.291Z"
size_mb: 620
size: 224092191
sif: "https://datasets.datalad.org/shub/colleeneb/test_singularity/test2/2019-05-16-84195d6e-043d1156/043d1156dd901b0b4a3c1a7daa43dc69.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/colleeneb/test_singularity/test2/2019-05-16-84195d6e-043d1156/
recipe: https://datasets.datalad.org/shub/colleeneb/test_singularity/test2/2019-05-16-84195d6e-043d1156/Singularity
collection: colleeneb/test_singularity
---

# colleeneb/test_singularity:test2

```bash
$ singularity pull shub://colleeneb/test_singularity:test2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%post
    apt-get -y update
    apt-get -y install locales
    apt-get -y install build-essential
    apt-get -y install tcl
    apt-get -y install environment-modules
    apt-get -y install python3 libtool autotools-dev automake autoconf make cmake
    apt-get -y install gcc-8 gfortran-8 g++-8
    apt-get -y install vim
    apt-get -y install strace
    apt-get update
    
%environment
    export LC_ALL=C
    export MODULESHOME=/usr/share/modules
```

## Collection

 - Name: [colleeneb/test_singularity](https://github.com/colleeneb/test_singularity)
 - License: None

