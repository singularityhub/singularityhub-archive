---
id: 8359
name: "pndni/centos7-base"
branch: "master"
tag: "dev"
commit: "464281874fb9ecfa980737eeac70c831091e4b79"
version: "32d3ed6717b8aa7e3aa5f88cefb450d9"
build_date: "2019-04-10T23:02:51.983Z"
size_mb: 977
size: 316936223
sif: "https://datasets.datalad.org/shub/pndni/centos7-base/dev/2019-04-10-46428187-32d3ed67/32d3ed6717b8aa7e3aa5f88cefb450d9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/centos7-base/dev/2019-04-10-46428187-32d3ed67/
recipe: https://datasets.datalad.org/shub/pndni/centos7-base/dev/2019-04-10-46428187-32d3ed67/Singularity
collection: pndni/centos7-base
---

# pndni/centos7-base:dev

```bash
$ singularity pull shub://pndni/centos7-base:dev
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
    Version dev
```

## Collection

 - Name: [pndni/centos7-base](https://github.com/pndni/centos7-base)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

