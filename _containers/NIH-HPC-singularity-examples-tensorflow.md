---
id: 876
name: "NIH-HPC/singularity-examples"
branch: "master"
tag: "tensorflow"
commit: "2ccdc4a334b5e669dd6eab2099623f8b0d5f5af8"
version: "f141ff10195c8e27d6b2491c8584b0d7"
build_date: "2019-11-17T01:21:30.313Z"
size_mb: 1302
size: 361222175
sif: "https://datasets.datalad.org/shub/NIH-HPC/singularity-examples/tensorflow/2019-11-17-2ccdc4a3-f141ff10/f141ff10195c8e27d6b2491c8584b0d7.simg"
url: https://datasets.datalad.org/shub/NIH-HPC/singularity-examples/tensorflow/2019-11-17-2ccdc4a3-f141ff10/
recipe: https://datasets.datalad.org/shub/NIH-HPC/singularity-examples/tensorflow/2019-11-17-2ccdc4a3-f141ff10/Singularity
collection: NIH-HPC/singularity-examples
---

# NIH-HPC/singularity-examples:tensorflow

```bash
$ singularity pull shub://NIH-HPC/singularity-examples:tensorflow
```

## Singularity Recipe

```singularity
BootStrap: docker
From: tensorflow/tensorflow:1.3.0

################################################################################
%labels
################################################################################
TENSORFLOW_VERSION 1.3.0
MAINTAINER Wolfgang Resch

################################################################################
%setup
################################################################################

################################################################################
%post
################################################################################

# create bind points for NIH HPC environment
mkdir /gpfs /spin1 /gs2 /gs3 /gs4 /gs5 /gs6 
mkdir /gs7 /gs8 /data /scratch /fdb /lscratch

################################################################################
%environment
################################################################################
export LC_ALL=C


################################################################################
%runscript
################################################################################
exec ipython "$@"
```

## Collection

 - Name: [NIH-HPC/singularity-examples](https://github.com/NIH-HPC/singularity-examples)
 - License: None

