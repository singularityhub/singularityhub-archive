---
id: 6101
name: "bouthilx/mahler.registry.mongodb"
branch: "master"
tag: "latest"
commit: "f830e5f85deefc27581e64b7c235c3777df14728"
version: "33d65c11d3b8e17ac70dad15e8288e5c"
build_date: "2020-12-18T18:28:41.801Z"
size_mb: 508
size: 195956767
sif: "https://datasets.datalad.org/shub/bouthilx/mahler.registry.mongodb/latest/2020-12-18-f830e5f8-33d65c11/33d65c11d3b8e17ac70dad15e8288e5c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/mahler.registry.mongodb/latest/2020-12-18-f830e5f8-33d65c11/
recipe: https://datasets.datalad.org/shub/bouthilx/mahler.registry.mongodb/latest/2020-12-18-f830e5f8-33d65c11/Singularity
collection: bouthilx/mahler.registry.mongodb
---

# bouthilx/mahler.registry.mongodb:latest

```bash
$ singularity pull shub://bouthilx/mahler.registry.mongodb:latest
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
    echo "Cleaning up"
    echo "------------------------------------------------------"
    apt-get clean
    apt-get autoclean
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [bouthilx/mahler.registry.mongodb](https://github.com/bouthilx/mahler.registry.mongodb)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

