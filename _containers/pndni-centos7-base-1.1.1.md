---
id: 8099
name: "pndni/centos7-base"
branch: "1.1.1"
tag: "1.1.1"
commit: "35a54bf07a55458f2e086a9035133543cc9e1a72"
version: "6c9c56c85a9e05da1a8eaa81c687f12e"
build_date: "2019-04-03T19:40:20.289Z"
size_mb: 977
size: 316862495
sif: "https://datasets.datalad.org/shub/pndni/centos7-base/1.1.1/2019-04-03-35a54bf0-6c9c56c8/6c9c56c85a9e05da1a8eaa81c687f12e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/centos7-base/1.1.1/2019-04-03-35a54bf0-6c9c56c8/
recipe: https://datasets.datalad.org/shub/pndni/centos7-base/1.1.1/2019-04-03-35a54bf0-6c9c56c8/Singularity
collection: pndni/centos7-base
---

# pndni/centos7-base:1.1.1

```bash
$ singularity pull shub://pndni/centos7-base:1.1.1
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/x86_64/
Include: yum

%post
    yum install -y wget file bc tar gzip libquadmath which bzip2 libgomp tcsh perl less vim
    yum groupinstall -y "Development Tools"
    wget https://github.com/Kitware/CMake/releases/download/v3.14.0/cmake-3.14.0-Linux-x86_64.sh
    mkdir -p /opt/cmake
    /bin/bash cmake-3.14.0-Linux-x86_64.sh --prefix=/opt/cmake --skip-license
    rm cmake-3.14.0-Linux-x86_64.sh

%labels
    Maintainer Steven Tilley
    Version 1.1.1
```

## Collection

 - Name: [pndni/centos7-base](https://github.com/pndni/centos7-base)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

