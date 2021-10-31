---
id: 4579
name: "bouthilx/flow"
branch: "master"
tag: "pytorch.0.4.0"
commit: "7a12010a9b104a1b3ac3f2aeab17f2467c3a61ba"
version: "496699665b4b4a5c394b448fd6bb321d"
build_date: "2018-09-05T16:47:16.595Z"
size_mb: 1642
size: 750276639
sif: "https://datasets.datalad.org/shub/bouthilx/flow/pytorch.0.4.0/2018-09-05-7a12010a-49669966/496699665b4b4a5c394b448fd6bb321d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/flow/pytorch.0.4.0/2018-09-05-7a12010a-49669966/
recipe: https://datasets.datalad.org/shub/bouthilx/flow/pytorch.0.4.0/2018-09-05-7a12010a-49669966/Singularity
collection: bouthilx/flow
---

# bouthilx/flow:pytorch.0.4.0

```bash
$ singularity pull shub://bouthilx/flow:pytorch.0.4.0
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
    echo "Installing PyTorch 0.4.0"
    echo "------------------------------------------------------"
    echo ${CUDA_VISIBLE_DEVICES}
    pip3 install http://download.pytorch.org/whl/cu90/torch-0.4.0-cp36-cp36m-linux_x86_64.whl
```

## Collection

 - Name: [bouthilx/flow](https://github.com/bouthilx/flow)
 - License: None

