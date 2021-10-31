---
id: 8124
name: "pndni/dcm-conversion-container"
branch: "2.0.0"
tag: "2.0.0"
commit: "29511f0c7de607794ba4e461fe88fad8251331dc"
version: "05cbe5496b20acb44f80a9039b2e0a00"
build_date: "2019-04-04T22:58:11.513Z"
size_mb: 1497
size: 519082015
sif: "https://datasets.datalad.org/shub/pndni/dcm-conversion-container/2.0.0/2019-04-04-29511f0c-05cbe549/05cbe5496b20acb44f80a9039b2e0a00.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/dcm-conversion-container/2.0.0/2019-04-04-29511f0c-05cbe549/
recipe: https://datasets.datalad.org/shub/pndni/dcm-conversion-container/2.0.0/2019-04-04-29511f0c-05cbe549/Singularity
collection: pndni/dcm-conversion-container
---

# pndni/dcm-conversion-container:2.0.0

```bash
$ singularity pull shub://pndni/dcm-conversion-container:2.0.0
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: pndni/centos7-base:1.2.0

%post
    yum install -y epel-release
    yum install -y python36 python36-pip python36-devel libstdc++-static pigz

%appinstall heudiconv
    pip3.6 install virtualenv
    virtualenv /opt/heudiconv
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
    Version 2.0.0
```

## Collection

 - Name: [pndni/dcm-conversion-container](https://github.com/pndni/dcm-conversion-container)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

