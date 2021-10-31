---
id: 7884
name: "bouthilx/mahler.scheduler.remoteflow"
branch: "master"
tag: "latest"
commit: "1cc34e26d149d3c16351d7ba4315821419bc4f30"
version: "e93860437ec5cbd5eeb3491411827074"
build_date: "2019-03-23T22:36:04.844Z"
size_mb: 510
size: 196157471
sif: "https://datasets.datalad.org/shub/bouthilx/mahler.scheduler.remoteflow/latest/2019-03-23-1cc34e26-e9386043/e93860437ec5cbd5eeb3491411827074.simg"
url: https://datasets.datalad.org/shub/bouthilx/mahler.scheduler.remoteflow/latest/2019-03-23-1cc34e26-e9386043/
recipe: https://datasets.datalad.org/shub/bouthilx/mahler.scheduler.remoteflow/latest/2019-03-23-1cc34e26-e9386043/Singularity
collection: bouthilx/mahler.scheduler.remoteflow
---

# bouthilx/mahler.scheduler.remoteflow:latest

```bash
$ singularity pull shub://bouthilx/mahler.scheduler.remoteflow:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%setup
    mkdir -p ${SINGULARITY_ROOTFS}/certs
    mkdir -p ${SINGULARITY_ROOTFS}/data
    mkdir -p ${SINGULARITY_ROOTFS}/repos

%environment
	export LC_ALL="C"  # Fix locales for pip3 install

%labels
    AUTHOR xavier.bouthillier@umontreal.ca

%post
    echo "------------------------------------------------------"
    echo "Installing Python 3.6"
    echo "------------------------------------------------------"
    apt-get -y update
    apt-get install -y build-essential
    apt-get install -y python3.6 python3.6-dev python3-virtualenv virtualenv git python3-pip

    echo "------------------------------------------------------"
    echo "Installing Mahler"
    echo "------------------------------------------------------"
    pip3 install 'setuptools>=v40.1.0'
    pip3 install git+https://github.com/bouthilx/mahler.git

    echo "------------------------------------------------------"
    echo "Installing Mahler MongoDB Registry"
    echo "------------------------------------------------------"
    pip3 install git+https://github.com/bouthilx/mahler.registry.mongodb.git

    echo "------------------------------------------------------"
    echo "Installing functional test repo"
    echo "------------------------------------------------------"
    git clone https://github.com/bouthilx/mahler.scheduler.remoteflow.git
    pip3 install -e mahler.scheduler.remoteflow/test/functional/repo

    echo "------------------------------------------------------"
    echo "Cleaning up"
    echo "------------------------------------------------------"
    apt-get clean
    apt-get autoclean
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [bouthilx/mahler.scheduler.remoteflow](https://github.com/bouthilx/mahler.scheduler.remoteflow)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

