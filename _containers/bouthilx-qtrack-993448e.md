---
id: 2532
name: "bouthilx/qtrack"
branch: "master"
tag: "993448e"
commit: "06cee549191c577cfe8a0032923f7efaa14bc63d"
version: "76605585ffb56cabf0b2afcde8390ffa"
build_date: "2018-04-14T16:56:55.266Z"
size_mb: 2217
size: 1013133343
sif: "https://datasets.datalad.org/shub/bouthilx/qtrack/993448e/2018-04-14-06cee549-76605585/76605585ffb56cabf0b2afcde8390ffa.simg"
url: https://datasets.datalad.org/shub/bouthilx/qtrack/993448e/2018-04-14-06cee549-76605585/
recipe: https://datasets.datalad.org/shub/bouthilx/qtrack/993448e/2018-04-14-06cee549-76605585/Singularity
collection: bouthilx/qtrack
---

# bouthilx/qtrack:993448e

```bash
$ singularity pull shub://bouthilx/qtrack:993448e
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%runscript
    exec echo "The runscript is the containers default runtime command!"

%setup
    mkdir -p ${SINGULARITY_ROOTFS}/certs
    mkdir -p ${SINGULARITY_ROOTFS}/data
    mkdir -p ${SINGULARITY_ROOTFS}/repos

%environment
	export LC_ALL="C"  # Fix locales for pip3 install

%labels
   AUTHOR xavier.bouthillier@umontreal.ca

%post
	export GITHUB_TOKEN="e209b24443c2fefa895c81d80957b838df6c68d7"
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

    echo "------------------------------------------------------"
    echo "Installing Tensorflow for tensor-board"
    echo "------------------------------------------------------"
	pip3 install tensorflow==1.5

    echo "------------------------------------------------------"
    echo "Installing custom Sacred"
    echo "------------------------------------------------------"
    cd /repos
	git clone https://${GITHUB_TOKEN}@github.com/bouthilx/impn.git qtrack
    cd qtrack
        git fetch
        git checkout --track origin/qtrack
        git reset --hard 993448e
        git submodule init
        git submodule update
        cd protopt
            git submodule init
            git submodule update
        cd ..

        pip3 install protopt/sacred

        echo "------------------------------------------------------"
        echo "Installing custom SmartDispatch"
        echo "------------------------------------------------------"

        pip3 install protopt/smartdispatch

    cd ..

    echo "------------------------------------------------------"
    echo "Installing Protopt"
    echo "------------------------------------------------------"
    pip3 install qtrack/protopt

    echo "------------------------------------------------------"
    echo "Installing IMPN"
    echo "------------------------------------------------------"
    pip3 install qtrack/

    echo "------------------------------------------------------"
    echo "Cleaning up"
    echo "------------------------------------------------------"
    apt-get clean
    apt-get autoclean
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [bouthilx/qtrack](https://github.com/bouthilx/qtrack)
 - License: None

