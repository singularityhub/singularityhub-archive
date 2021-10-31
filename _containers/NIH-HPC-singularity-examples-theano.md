---
id: 877
name: "NIH-HPC/singularity-examples"
branch: "master"
tag: "theano"
commit: "2ccdc4a334b5e669dd6eab2099623f8b0d5f5af8"
version: "ad5b3d3a8bbdb356796d2e62a7e2d4c9"
build_date: "2017-11-22T19:08:50.802Z"
size_mb: 2103
size: 946704415
sif: "https://datasets.datalad.org/shub/NIH-HPC/singularity-examples/theano/2017-11-22-2ccdc4a3-ad5b3d3a/ad5b3d3a8bbdb356796d2e62a7e2d4c9.simg"
url: https://datasets.datalad.org/shub/NIH-HPC/singularity-examples/theano/2017-11-22-2ccdc4a3-ad5b3d3a/
recipe: https://datasets.datalad.org/shub/NIH-HPC/singularity-examples/theano/2017-11-22-2ccdc4a3-ad5b3d3a/Singularity
collection: NIH-HPC/singularity-examples
---

# NIH-HPC/singularity-examples:theano

```bash
$ singularity pull shub://NIH-HPC/singularity-examples:theano
```

## Singularity Recipe

```singularity
BootStrap: docker
From: kaixhin/cuda-theano:7.5

%post

    # create bind points for NIH HPC environment
    mkdir /gpfs /spin1 /gs2 /gs3 /gs4 /gs5 /gs6 /data /scratch /fdb /lscratch

%environment

    PATH=/usr/local/cuda-7.5/bin:$PATH
    LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
    LD_LIBRARY_PATH=/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH
    CUDA_HOME=/usr/local/cuda
    export PATH LD_LIBRARY_PATH CUDA_HOME
```

## Collection

 - Name: [NIH-HPC/singularity-examples](https://github.com/NIH-HPC/singularity-examples)
 - License: None

