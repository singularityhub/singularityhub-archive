---
id: 8108
name: "pndni/centos7-base"
branch: "1.2.0"
tag: "1.2.0"
commit: "f27ca315f81d7b0d340bbe26b63cfef5232f30f4"
version: "54a51f3b4398372053cb9442152c23ae"
build_date: "2020-01-15T20:38:53.778Z"
size_mb: 977
size: 316944415
sif: "https://datasets.datalad.org/shub/pndni/centos7-base/1.2.0/2020-01-15-f27ca315-54a51f3b/54a51f3b4398372053cb9442152c23ae.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/centos7-base/1.2.0/2020-01-15-f27ca315-54a51f3b/
recipe: https://datasets.datalad.org/shub/pndni/centos7-base/1.2.0/2020-01-15-f27ca315-54a51f3b/Singularity
collection: pndni/centos7-base
---

# pndni/centos7-base:1.2.0

```bash
$ singularity pull shub://pndni/centos7-base:1.2.0
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/x86_64/
Include: yum

%post
    yum install -y wget file bc tar gzip libquadmath which bzip2 libgomp tcsh perl less vim zlib zlib-devel
    yum groupinstall -y "Development Tools"
    wget https://github.com/Kitware/CMake/releases/download/v3.14.0/cmake-3.14.0-Linux-x86_64.sh
    mkdir -p /opt/cmake
    /bin/bash cmake-3.14.0-Linux-x86_64.sh --prefix=/opt/cmake --skip-license
    rm cmake-3.14.0-Linux-x86_64.sh

%labels
    Maintainer Steven Tilley
    Version 1.2.0
```

## Collection

 - Name: [pndni/centos7-base](https://github.com/pndni/centos7-base)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

