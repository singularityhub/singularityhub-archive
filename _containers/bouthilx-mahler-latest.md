---
id: 6098
name: "bouthilx/mahler"
branch: "master"
tag: "latest"
commit: "9ae6f95bc1965eb16ca84300fbf8dc091d24e966"
version: "1571fb7e19d8b7e9c1017059b9038205"
build_date: "2019-01-03T04:17:35.703Z"
size_mb: 505
size: 194678815
sif: "https://datasets.datalad.org/shub/bouthilx/mahler/latest/2019-01-03-9ae6f95b-1571fb7e/1571fb7e19d8b7e9c1017059b9038205.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/mahler/latest/2019-01-03-9ae6f95b-1571fb7e/
recipe: https://datasets.datalad.org/shub/bouthilx/mahler/latest/2019-01-03-9ae6f95b-1571fb7e/Singularity
collection: bouthilx/mahler
---

# bouthilx/mahler:latest

```bash
$ singularity pull shub://bouthilx/mahler:latest
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
    echo "Cleaning up"
    echo "------------------------------------------------------"
    apt-get clean
    apt-get autoclean
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [bouthilx/mahler](https://github.com/bouthilx/mahler)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

