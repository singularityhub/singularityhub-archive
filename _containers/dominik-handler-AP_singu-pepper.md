---
id: 14493
name: "dominik-handler/AP_singu"
branch: "master"
tag: "pepper"
commit: "7b74327f526918785c965e271133df6684342fbd"
version: "a32bcfad4bffca9d0ad3a6f3397f9ebed622bf6fea94d44e7fb85af7eb41807d"
build_date: "2020-09-29T13:49:58.705Z"
size_mb: 4411.46484375
size: 4625756160
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/pepper/2020-09-29-7b74327f-a32bcfad/a32bcfad4bffca9d0ad3a6f3397f9ebed622bf6fea94d44e7fb85af7eb41807d.sif"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/pepper/2020-09-29-7b74327f-a32bcfad/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/pepper/2020-09-29-7b74327f-a32bcfad/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:pepper

```bash
$ singularity pull shub://dominik-handler/AP_singu:pepper
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: kishwars/pepper

#@ Bootstrap: docker
#@ From: pytorch/pytorch:1.1.0-cuda10.0-cudnn7.5-runtime

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at  
  PEPPER 

%post
    set -e 

    # apt-get update 
    # apt-get -y install software-properties-common
    # add-apt-repository universe
    # apt-get update
    # apt-get -y install time git cmake make wget autoconf gcc g++ zlib1g-dev libcurl4-openssl-dev libbz2-dev python3 python3-dev python3-pip python3-virtualenv virtualenv bzip2 lzma-dev liblzma-dev libpthread-stubs0-dev libhdf5-dev
 
    # cd /
    # git clone https://github.com/kishwarshafin/helen.git && \
    # cd /helen && \
    # make install


    #@ cd /tmp
    #@ mkdir /opt/cmake && \
    #@ wget https://github.com/Kitware/CMake/releases/download/v3.14.4/cmake-3.14.4-Linux-x86_64.sh && \
    #@ sh /tmp/cmake-3.14.4-Linux-x86_64.sh --prefix=/opt/cmake --skip-license && \
    #@ ln -s /opt/cmake/bin/cmake /usr/local/bin/cmake


    #@ mkdir /opt/helen/build
    #@ cd /opt/helen/build
    #@ cmake .. -Wno-deprecated && make

    #@ python3 -m pip install h5py tqdm numpy pyyaml
    #python3 -m pip install https://download.pytorch.org/whl/cpu/torch-1.1.0-cp36-cp36m-linux_x86_64.whl
    #python3 -m pip install https://download.pytorch.org/whl/cpu/torchvision-0.3.0-cp36-cp36m-linux_x86_64.whl

    #cd /opt/helen
    #cp helen_wrapper.sh /opt/helen_wrapper.sh

  #clean up
    # apt-get autoremove
    # apt-get clean

%environment

%runscript
    $@
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

