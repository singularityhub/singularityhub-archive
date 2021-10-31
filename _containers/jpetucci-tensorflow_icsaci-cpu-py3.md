---
id: 9865
name: "jpetucci/tensorflow_icsaci"
branch: "master"
tag: "cpu-py3"
commit: "7e32b432d4dcd9e733f0db110a487abd2a85571f"
version: "b09b0ff5658bb1bdebfa5f9ad2adc823"
build_date: "2019-06-18T17:08:05.122Z"
size_mb: 1055
size: 422490143
sif: "https://datasets.datalad.org/shub/jpetucci/tensorflow_icsaci/cpu-py3/2019-06-18-7e32b432-b09b0ff5/b09b0ff5658bb1bdebfa5f9ad2adc823.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jpetucci/tensorflow_icsaci/cpu-py3/2019-06-18-7e32b432-b09b0ff5/
recipe: https://datasets.datalad.org/shub/jpetucci/tensorflow_icsaci/cpu-py3/2019-06-18-7e32b432-b09b0ff5/Singularity
collection: jpetucci/tensorflow_icsaci
---

# jpetucci/tensorflow_icsaci:cpu-py3

```bash
$ singularity pull shub://jpetucci/tensorflow_icsaci:cpu-py3
```

## Singularity Recipe

```singularity
# latest tensorflow_gpu for ICS-ACI

BootStrap: docker
From: tensorflow/tensorflow:latest-py3

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

