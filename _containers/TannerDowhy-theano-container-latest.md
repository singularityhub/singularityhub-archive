---
id: 5617
name: "TannerDowhy/theano-container"
branch: "master"
tag: "latest"
commit: "495329ca60a9037a65a264e22178e4d968b0eef5"
version: "68242e645fda1ea714394d8eea46b149"
build_date: "2018-11-16T10:50:08.447Z"
size_mb: 2070
size: 938860575
sif: "https://datasets.datalad.org/shub/TannerDowhy/theano-container/latest/2018-11-16-495329ca-68242e64/68242e645fda1ea714394d8eea46b149.simg"
url: https://datasets.datalad.org/shub/TannerDowhy/theano-container/latest/2018-11-16-495329ca-68242e64/
recipe: https://datasets.datalad.org/shub/TannerDowhy/theano-container/latest/2018-11-16-495329ca-68242e64/Singularity
collection: TannerDowhy/theano-container
---

# TannerDowhy/theano-container:latest

```bash
$ singularity pull shub://TannerDowhy/theano-container:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: kaixhin/cuda-theano:7.5

%post

    # create bind points for NIH HPC environment
    mkdir /gpfs /spin1 /gs2 /gs3 /gs4 /gs5 /gs6 /data /scratch /fdb /lscratch
    pip install --upgrade six

%environment

    PATH=/usr/local/cuda-7.5/bin:$PATH
    LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
    LD_LIBRARY_PATH=/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
    CUDA_HOME=/usr/local/cuda
    export PATH LD_LIBRARY_PATH CUDA_HOME
```

## Collection

 - Name: [TannerDowhy/theano-container](https://github.com/TannerDowhy/theano-container)
 - License: None

