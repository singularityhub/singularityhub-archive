---
id: 8402
name: "pndni/centos7-base"
branch: "1.4.0"
tag: "1.4.0"
commit: "1f57bc52f4376eaca764bb714e28027ed1d235f2"
version: "bf3356d3e3dabf41be99cc67cc0ac866"
build_date: "2020-12-09T04:29:34.934Z"
size_mb: 977
size: 316936223
sif: "https://datasets.datalad.org/shub/pndni/centos7-base/1.4.0/2020-12-09-1f57bc52-bf3356d3/bf3356d3e3dabf41be99cc67cc0ac866.simg"
url: https://datasets.datalad.org/shub/pndni/centos7-base/1.4.0/2020-12-09-1f57bc52-bf3356d3/
recipe: https://datasets.datalad.org/shub/pndni/centos7-base/1.4.0/2020-12-09-1f57bc52-bf3356d3/Singularity
collection: pndni/centos7-base
---

# pndni/centos7-base:1.4.0

```bash
$ singularity pull shub://pndni/centos7-base:1.4.0
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/x86_64/
Include: yum

%post
    yum install -y wget file bc tar gzip libquadmath which bzip2 libgomp tcsh perl less vim zlib zlib-devel hostname
    yum groupinstall -y "Development Tools"
    wget https://github.com/Kitware/CMake/releases/download/v3.14.0/cmake-3.14.0-Linux-x86_64.sh
    mkdir -p /opt/cmake
    /bin/bash cmake-3.14.0-Linux-x86_64.sh --prefix=/opt/cmake --skip-license
    rm cmake-3.14.0-Linux-x86_64.sh

%labels
    Maintainer Steven Tilley
    Version 1.4.0
```

## Collection

 - Name: [pndni/centos7-base](https://github.com/pndni/centos7-base)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

