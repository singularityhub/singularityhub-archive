---
id: 15054
name: "mdzik/TCLB_singularity"
branch: "master"
tag: "ubuntu2004_cuda11"
commit: "e913b5a732e7a07b45b77cfcf24c7ad2e4aeb03e"
version: "ef3a01d82277d431d04116ad49e337979697edc3c506ec93133247a80eec0814"
build_date: "2020-12-17T09:23:24.078Z"
size_mb: 810.83984375
size: 850227200
sif: "https://datasets.datalad.org/shub/mdzik/TCLB_singularity/ubuntu2004_cuda11/2020-12-17-e913b5a7-ef3a01d8/ef3a01d82277d431d04116ad49e337979697edc3c506ec93133247a80eec0814.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/mdzik/TCLB_singularity/ubuntu2004_cuda11/2020-12-17-e913b5a7-ef3a01d8/
recipe: https://datasets.datalad.org/shub/mdzik/TCLB_singularity/ubuntu2004_cuda11/2020-12-17-e913b5a7-ef3a01d8/Singularity
collection: mdzik/TCLB_singularity
---

# mdzik/TCLB_singularity:ubuntu2004_cuda11

```bash
$ singularity pull shub://mdzik/TCLB_singularity:ubuntu2004_cuda11
```

## Singularity Recipe

```singularity
BootStrap: library
From: ubuntu:20.04

#debug
#BootStrap: localimage
#From: ./test.sif

%post
    apt-get -y update
    apt-get -y install wget git software-properties-common 
    add-apt-repository universe
    add-apt-repository multiverse
    add-apt-repository restricted
    
    apt-get -y update
    apt-get -y install openmpi-bin libopenmpi-dev python-numpy python-dev r-base-dev r-recommended libhdf5-openmpi-dev cmake


    
    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
    mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
    apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
    add-apt-repository "deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
    apt-get -y update
    apt-get -y install cuda-minimal-build-11-0 cuda-command-line-tools-11-0

 
%environment
    export LC_ALL=C
    export PATH=/TCLB:/usr/local/cuda-10.0/bin:$PATH
    export R_LIBS_USER=/opt/r_libs  
    export LDFLAGS="-L/usr/lib/x86_64-linux-gnu/hdf5/openmpi/  $LDFLAGS" 
    export CPPFLAGS="-I /usr/include/hdf5/openmpi $CPPFLAGS"
    export TSD=/opt/TCLB_STABLE

%runscript
    echo "Plain environment for TCLB/CUDA run and build"

%labels
    Author llaniewski , mdzik , and others TCLB.IO
```

## Collection

 - Name: [mdzik/TCLB_singularity](https://github.com/mdzik/TCLB_singularity)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

