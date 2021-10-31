---
id: 5868
name: "bouthilx/flow"
branch: "master"
tag: "pytorch.1.0.0"
commit: "c66b4c3af51cc055e7c4a2459d749458620d0c6b"
version: "75a020c0a5efcf262d68a92ca143c2e2"
build_date: "2019-11-25T19:57:50.607Z"
size_mb: 2191
size: 1396572191
sif: "https://datasets.datalad.org/shub/bouthilx/flow/pytorch.1.0.0/2019-11-25-c66b4c3a-75a020c0/75a020c0a5efcf262d68a92ca143c2e2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/flow/pytorch.1.0.0/2019-11-25-c66b4c3a-75a020c0/
recipe: https://datasets.datalad.org/shub/bouthilx/flow/pytorch.1.0.0/2019-11-25-c66b4c3a-75a020c0/Singularity
collection: bouthilx/flow
---

# bouthilx/flow:pytorch.1.0.0

```bash
$ singularity pull shub://bouthilx/flow:pytorch.1.0.0
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
    export CUDA_VISIBLE_DEVICES=''

    echo "------------------------------------------------------"
    echo "Installing Python 3.6"
    echo "------------------------------------------------------"
    apt-get -y update
    apt-get install -y build-essential
    apt-get install -y python3.6 python3.6-dev python3-virtualenv virtualenv git gcc wget bzip2 python3-pip

    echo "------------------------------------------------------"
    echo "Installing PyTorch 1.0.0"
    echo "------------------------------------------------------"
    echo ${CUDA_VISIBLE_DEVICES}
    pip3 install torch==v1.0.0
```

## Collection

 - Name: [bouthilx/flow](https://github.com/bouthilx/flow)
 - License: None

