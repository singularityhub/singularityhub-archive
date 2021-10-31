---
id: 7679
name: "bouthilx/flow"
branch: "master"
tag: "pytorch.1.0.1"
commit: "af88091cab5cf6ca8ae152aacf6f2ddc479a276f"
version: "a871c4108dd06d8a187268ec1e947945"
build_date: "2019-10-10T17:22:24.404Z"
size_mb: 2111
size: 1337241631
sif: "https://datasets.datalad.org/shub/bouthilx/flow/pytorch.1.0.1/2019-10-10-af88091c-a871c410/a871c4108dd06d8a187268ec1e947945.simg"
url: https://datasets.datalad.org/shub/bouthilx/flow/pytorch.1.0.1/2019-10-10-af88091c-a871c410/
recipe: https://datasets.datalad.org/shub/bouthilx/flow/pytorch.1.0.1/2019-10-10-af88091c-a871c410/Singularity
collection: bouthilx/flow
---

# bouthilx/flow:pytorch.1.0.1

```bash
$ singularity pull shub://bouthilx/flow:pytorch.1.0.1
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
    echo "Installing PyTorch 1.0.1"
    echo "------------------------------------------------------"
    echo ${CUDA_VISIBLE_DEVICES}
    pip3 install torch==v1.0.1
```

## Collection

 - Name: [bouthilx/flow](https://github.com/bouthilx/flow)
 - License: None

