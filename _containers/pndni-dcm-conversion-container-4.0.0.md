---
id: 8383
name: "pndni/dcm-conversion-container"
branch: "4.0.0"
tag: "4.0.0"
commit: "b0df0e67fe5313a2b6e77fd52eeb41b6dada8dd6"
version: "0ce20af12410aad1ef0b1c439c510bca"
build_date: "2019-04-12T14:59:18.635Z"
size_mb: 1497
size: 518479903
sif: "https://datasets.datalad.org/shub/pndni/dcm-conversion-container/4.0.0/2019-04-12-b0df0e67-0ce20af1/0ce20af12410aad1ef0b1c439c510bca.simg"
url: https://datasets.datalad.org/shub/pndni/dcm-conversion-container/4.0.0/2019-04-12-b0df0e67-0ce20af1/
recipe: https://datasets.datalad.org/shub/pndni/dcm-conversion-container/4.0.0/2019-04-12-b0df0e67-0ce20af1/Singularity
collection: pndni/dcm-conversion-container
---

# pndni/dcm-conversion-container:4.0.0

```bash
$ singularity pull shub://pndni/dcm-conversion-container:4.0.0
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
    git clone --branch v1.0.20190410 https://github.com/rordenlab/dcm2niix.git
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
    Version 4.0.0
```

## Collection

 - Name: [pndni/dcm-conversion-container](https://github.com/pndni/dcm-conversion-container)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

