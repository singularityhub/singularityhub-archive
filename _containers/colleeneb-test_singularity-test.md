---
id: 9087
name: "colleeneb/test_singularity"
branch: "master"
tag: "test"
commit: "dd2eed4c5111c12c947e0a10d8f71b112feb8014"
version: "c3b5e12ffc896afb1e5945d025092c81"
build_date: "2019-05-16T20:22:33.708Z"
size_mb: 936
size: 320614431
sif: "https://datasets.datalad.org/shub/colleeneb/test_singularity/test/2019-05-16-dd2eed4c-c3b5e12f/c3b5e12ffc896afb1e5945d025092c81.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/colleeneb/test_singularity/test/2019-05-16-dd2eed4c-c3b5e12f/
recipe: https://datasets.datalad.org/shub/colleeneb/test_singularity/test/2019-05-16-dd2eed4c-c3b5e12f/Singularity
collection: colleeneb/test_singularity
---

# colleeneb/test_singularity:test

```bash
$ singularity pull shub://colleeneb/test_singularity:test
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: intelopencl/intel-opencl:ubuntu-18.04-ppa

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

