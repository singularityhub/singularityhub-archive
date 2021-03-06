---
id: 12140
name: "dominik-handler/AP_singu"
branch: "master"
tag: "helen"
commit: "8e6a023eb69d1fa6d196a26aa792b58009817ecb"
version: "eaeda5d9aa1010cffd167756771a1345e1725a110f16963ba04ee915d91453af"
build_date: "2020-07-27T10:24:11.827Z"
size_mb: 2214.67578125
size: 2322255872
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/helen/2020-07-27-8e6a023e-eaeda5d9/eaeda5d9aa1010cffd167756771a1345e1725a110f16963ba04ee915d91453af.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/helen/2020-07-27-8e6a023e-eaeda5d9/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/helen/2020-07-27-8e6a023e-eaeda5d9/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:helen

```bash
$ singularity pull shub://dominik-handler/AP_singu:helen
```

## Singularity Recipe

```singularity
Bootstrap: library
From: ubuntu:18.04

#@ Bootstrap: docker
#@ From: pytorch/pytorch:1.1.0-cuda10.0-cudnn7.5-runtime

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at  
  MarginPolish 

%post
    set -e 

    apt-get update 
    apt-get -y install software-properties-common
    add-apt-repository universe
    apt-get update
    apt-get -y install time git cmake make wget autoconf gcc g++ zlib1g-dev libcurl4-openssl-dev libbz2-dev python3 python3-dev python3-pip python3-virtualenv virtualenv bzip2 lzma-dev liblzma-dev libpthread-stubs0-dev libhdf5-dev
    apt-get clean && \
    apt-get purge && \
    #@ rm --no-preserve-root -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


    #@ cd /tmp
    #@ mkdir /opt/cmake && \
    #@ wget https://github.com/Kitware/CMake/releases/download/v3.14.4/cmake-3.14.4-Linux-x86_64.sh && \
    #@ sh /tmp/cmake-3.14.4-Linux-x86_64.sh --prefix=/opt/cmake --skip-license && \
    #@ ln -s /opt/cmake/bin/cmake /usr/local/bin/cmake

    cd /
    git clone https://github.com/kishwarshafin/helen.git && \
    cd /helen && \
    make install

    #@ mkdir /opt/helen/build
    #@ cd /opt/helen/build
    #@ cmake .. -Wno-deprecated && make

    #@ python3 -m pip install h5py tqdm numpy pyyaml
    #python3 -m pip install https://download.pytorch.org/whl/cpu/torch-1.1.0-cp36-cp36m-linux_x86_64.whl
    #python3 -m pip install https://download.pytorch.org/whl/cpu/torchvision-0.3.0-cp36-cp36m-linux_x86_64.whl

    #cd /opt/helen
    #cp helen_wrapper.sh /opt/helen_wrapper.sh

%environment
    . /helen/venv/bin/activate

%runscript
    $@
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

