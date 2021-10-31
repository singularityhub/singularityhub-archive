---
id: 8126
name: "pndni/dcm-conversion-container"
branch: "3.0.0"
tag: "3.0.0"
commit: "f74e7b331e5d610b54c8549540b3549fb3c628ba"
version: "35b352a1ea27332541cf385d9aa73ebf"
build_date: "2019-04-04T22:58:11.507Z"
size_mb: 1497
size: 518385695
sif: "https://datasets.datalad.org/shub/pndni/dcm-conversion-container/3.0.0/2019-04-04-f74e7b33-35b352a1/35b352a1ea27332541cf385d9aa73ebf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/dcm-conversion-container/3.0.0/2019-04-04-f74e7b33-35b352a1/
recipe: https://datasets.datalad.org/shub/pndni/dcm-conversion-container/3.0.0/2019-04-04-f74e7b33-35b352a1/Singularity
collection: pndni/dcm-conversion-container
---

# pndni/dcm-conversion-container:3.0.0

```bash
$ singularity pull shub://pndni/dcm-conversion-container:3.0.0
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: pndni/centos7-base:1.2.0

%post
    yum install -y epel-release
    yum install -y python36 python36-pip python36-devel libstdc++-static pigz python36-virtualenv

%appinstall heudiconv
    virtualenv-3.6 /opt/heudiconv
    source /opt/heudiconv/bin/activate
    pip install heudiconv
    deactivate

%appenv heudiconv
    source ${SCIF_APPENV_dcm2niix}
    source /opt/heudiconv/bin/activate

%apprun heudiconv
    heudiconv "$@"

%appinstall dcm2niix
    git clone --branch v1.0.20181125 https://github.com/rordenlab/dcm2niix.git
    cd dcm2niix
    mkdir build && cd build
    /opt/cmake/bin/cmake -DCMAKE_INSTALL_PREFIX=/opt/dcm2niix ..
    make
    make install

%appenv dcm2niix
    export PATH=/opt/dcm2niix/bin:$PATH

%apprun dcm2niix
    dcm2niix "$@"

%labels
    Maintainer Steven Tilley
    Version 3.0.0
```

## Collection

 - Name: [pndni/dcm-conversion-container](https://github.com/pndni/dcm-conversion-container)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

