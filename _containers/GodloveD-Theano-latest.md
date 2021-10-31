---
id: 50
name: "GodloveD/Theano"
branch: "master"
tag: "latest"
commit: "a7d005c6689119607d41fc45150338681ddbf1f0"
version: "576eff4e31c9d4abe6969fc32026909c"
build_date: "2020-09-21T08:01:27.372Z"
size_mb: 2422
size: 1065652255
sif: "https://datasets.datalad.org/shub/GodloveD/Theano/latest/2020-09-21-a7d005c6-576eff4e/576eff4e31c9d4abe6969fc32026909c.simg"
url: https://datasets.datalad.org/shub/GodloveD/Theano/latest/2020-09-21-a7d005c6-576eff4e/
recipe: https://datasets.datalad.org/shub/GodloveD/Theano/latest/2020-09-21-a7d005c6-576eff4e/Singularity
collection: GodloveD/Theano
---

# GodloveD/Theano:latest

```bash
$ singularity pull shub://GodloveD/Theano:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: kaixhin/cuda-theano:7.5

%setup
    # commands to be executed on host outside container during bootstrap

%post
    # create bind points for NIH HPC environment
    mkdir /gpfs /spin1 /gs2 /gs3 /gs4 /gs5 /gs6 /data /scratch /fdb /lscratch

    # download and run NIH HPC NVIDIA driver installer
    wget ftp://helix.nih.gov/CUDA/cuda4singularity
    chmod 755 cuda4singularity
    ./cuda4singularity --verbose
    rm cuda4singularity

    # set some vars in the environment
    echo "
PATH=/usr/local/cuda-7.5/bin:\$PATH
LD_LIBRARY_PATH=/usr/local/cuda/lib64:\$LD_LIBRARY_PATH
LD_LIBRARY_PATH=/usr/local/cuda/extras/CUPTI/lib64:\$LD_LIBRARY_PATH
CUDA_HOME=/usr/local/cuda
export PATH LD_LIBRARY_PATH CUDA_HOME" >>/environment
 
%runscript
    # commands to be executed when the container runs
 
%test
    # commands to be executed within container at close of bootstrap process
```

## Collection

 - Name: [GodloveD/Theano](https://github.com/GodloveD/Theano)
 - License: None

