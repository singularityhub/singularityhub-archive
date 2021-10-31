---
id: 2721
name: "sbutcher/container-python"
branch: "master"
tag: "latest"
commit: "7582beb21ac013e6c8da15f1eeaf9fb6105fcce1"
version: "b7905585f5af003370ba447519c421c7"
build_date: "2021-01-27T21:34:29.586Z"
size_mb: 1108
size: 335343647
sif: "https://datasets.datalad.org/shub/sbutcher/container-python/latest/2021-01-27-7582beb2-b7905585/b7905585f5af003370ba447519c421c7.simg"
url: https://datasets.datalad.org/shub/sbutcher/container-python/latest/2021-01-27-7582beb2-b7905585/
recipe: https://datasets.datalad.org/shub/sbutcher/container-python/latest/2021-01-27-7582beb2-b7905585/Singularity
collection: sbutcher/container-python
---

# sbutcher/container-python:latest

```bash
$ singularity pull shub://sbutcher/container-python:latest
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: https://www.mirrorservice.org/sites/mirror.centos.org/%{OSVERSION}/os/$basearch/
UpdateURL: https://www.mirrorservice.org/sites/mirror.centos.org/%{OSVERSION}/updates/$basearch/
Include: yum


%post
    yum -y groupinstall "Development Tools"
    yum -y install wget

#variables section

VER="2.7.15"
FTPSRV="https://www.python.org/ftp/python/${VER}"
FTP_FILE="Python-${VER}.tgz"
PYTHON_SHORT_VERSION=${VER%.*}

#get , config and make

/usr/bin/wget ${FTPSRV}/${FTP_FILE}
tar xzf ${FTP_FILE}
cd Python-${VER}
./configure
make
make install

%runscript
    python $@
```

## Collection

 - Name: [sbutcher/container-python](https://github.com/sbutcher/container-python)
 - License: None

