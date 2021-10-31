---
id: 8098
name: "pndni/centos7-base"
branch: "1.1.0"
tag: "1.1.0"
commit: "975b4dc79458a46ebe28cd095738e56847abb13a"
version: "334c4e0de9234acc143f146ec92ae411"
build_date: "2019-04-03T19:40:15.578Z"
size_mb: 977
size: 316862495
sif: "https://datasets.datalad.org/shub/pndni/centos7-base/1.1.0/2019-04-03-975b4dc7-334c4e0d/334c4e0de9234acc143f146ec92ae411.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/centos7-base/1.1.0/2019-04-03-975b4dc7-334c4e0d/
recipe: https://datasets.datalad.org/shub/pndni/centos7-base/1.1.0/2019-04-03-975b4dc7-334c4e0d/Singularity
collection: pndni/centos7-base
---

# pndni/centos7-base:1.1.0

```bash
$ singularity pull shub://pndni/centos7-base:1.1.0
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
    Maintainer "Steven Tilley"
```

## Collection

 - Name: [pndni/centos7-base](https://github.com/pndni/centos7-base)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

