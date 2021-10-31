---
id: 8112
name: "pndni/dcm-conversion-container"
branch: "1.0.0"
tag: "1.0.0"
commit: "1c98d8aa953aa55cd7cb0e13832315d7a74a2d4c"
version: "6c951d892c6cb6b1994f6152b39e46a7"
build_date: "2019-04-04T14:43:43.325Z"
size_mb: 1477
size: 509276191
sif: "https://datasets.datalad.org/shub/pndni/dcm-conversion-container/1.0.0/2019-04-04-1c98d8aa-6c951d89/6c951d892c6cb6b1994f6152b39e46a7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/dcm-conversion-container/1.0.0/2019-04-04-1c98d8aa-6c951d89/
recipe: https://datasets.datalad.org/shub/pndni/dcm-conversion-container/1.0.0/2019-04-04-1c98d8aa-6c951d89/Singularity
collection: pndni/dcm-conversion-container
---

# pndni/dcm-conversion-container:1.0.0

```bash
$ singularity pull shub://pndni/dcm-conversion-container:1.0.0
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: pndni/centos7-base:1.2.0

%post
    yum install -y epel-release
    yum install -y python36 python36-pip python36-devel libstdc++-static pigz
    pip3.6 install heudiconv
    git clone --branch v1.0.20181125 https://github.com/rordenlab/dcm2niix.git
    cd dcm2niix
    mkdir build && cd build
    /opt/cmake/bin/cmake -DCMAKE_INSTALL_PREFIX=/opt/dcm2niix ..
    make
    make install

%environment
    export PATH=/opt/dcm2niix/bin:$PATH

%apprun heudiconv
    heudiconv "$@"

%apprun dcm2niix
    dcm2niix "$@"

%labels
    Maintainer Steven Tilley
    Version 1.0.0
```

## Collection

 - Name: [pndni/dcm-conversion-container](https://github.com/pndni/dcm-conversion-container)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

