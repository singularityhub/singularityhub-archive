---
id: 9866
name: "jpetucci/tensorflow_icsaci"
branch: "master"
tag: "gpu-py3"
commit: "7e32b432d4dcd9e733f0db110a487abd2a85571f"
version: "90d239e1cd18d4d7df5a6b333ce4bcaa"
build_date: "2019-09-10T13:37:02.132Z"
size_mb: 3237
size: 1651580959
sif: "https://datasets.datalad.org/shub/jpetucci/tensorflow_icsaci/gpu-py3/2019-09-10-7e32b432-90d239e1/90d239e1cd18d4d7df5a6b333ce4bcaa.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jpetucci/tensorflow_icsaci/gpu-py3/2019-09-10-7e32b432-90d239e1/
recipe: https://datasets.datalad.org/shub/jpetucci/tensorflow_icsaci/gpu-py3/2019-09-10-7e32b432-90d239e1/Singularity
collection: jpetucci/tensorflow_icsaci
---

# jpetucci/tensorflow_icsaci:gpu-py3

```bash
$ singularity pull shub://jpetucci/tensorflow_icsaci:gpu-py3
```

## Singularity Recipe

```singularity
# latest tensorflow_gpu for ICS-ACI

BootStrap: docker
From: tensorflow/tensorflow:latest-gpu-py3

%labels
Author jmp579

#%runscript
#    exec /usr/local/bin/python "$@"

%post
    #------------------------------------------------------------------------------
    # Create local binding point for our HPC
    #------------------------------------------------------------------------------
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/scratch
    mkdir -p /gpfs/group
mkdir -p /var/spool/torque
```

## Collection

 - Name: [jpetucci/tensorflow_icsaci](https://github.com/jpetucci/tensorflow_icsaci)
 - License: None

