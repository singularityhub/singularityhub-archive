---
id: 2539
name: "bouthilx/flow"
branch: "master"
tag: "pytorch.0.3.1"
commit: "73834298aa0bc7c5b40d888a44422cd8220048f3"
version: "8eaba02b6e798a84c7d27b29309e6bf1"
build_date: "2018-09-05T16:47:16.563Z"
size_mb: 1625
size: 801144863
sif: "https://datasets.datalad.org/shub/bouthilx/flow/pytorch.0.3.1/2018-09-05-73834298-8eaba02b/8eaba02b6e798a84c7d27b29309e6bf1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/flow/pytorch.0.3.1/2018-09-05-73834298-8eaba02b/
recipe: https://datasets.datalad.org/shub/bouthilx/flow/pytorch.0.3.1/2018-09-05-73834298-8eaba02b/Singularity
collection: bouthilx/flow
---

# bouthilx/flow:pytorch.0.3.1

```bash
$ singularity pull shub://bouthilx/flow:pytorch.0.3.1
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

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
    echo "Installing Python 3.5"
    echo "------------------------------------------------------"
    apt-get -y update
    apt-get install -y build-essential
    apt-get install -y python3.5 python3.5-dev python3-virtualenv virtualenv git gcc wget bzip2 python3-pip

    echo "------------------------------------------------------"
    echo "Installing PyTorch 0.3.1"
    echo "------------------------------------------------------"
    echo ${CUDA_VISIBLE_DEVICES}
	pip3 install http://download.pytorch.org/whl/cu90/torch-0.3.1-cp35-cp35m-linux_x86_64.whl 
	pip3 install torchvision
    pip3 install git+https://github.com/pytorch/tnt.git@ba256835a4f33d9139a70b6440c3223123132bc8
```

## Collection

 - Name: [bouthilx/flow](https://github.com/bouthilx/flow)
 - License: None

