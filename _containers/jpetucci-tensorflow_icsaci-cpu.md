---
id: 9734
name: "jpetucci/tensorflow_icsaci"
branch: "master"
tag: "cpu"
commit: "f8ea1ccdb4c0021982dccba87b528b59a91bd0ff"
version: "ab49489f048c3400d99ca8d463d6ce94"
build_date: "2019-06-10T18:57:36.647Z"
size_mb: 1038
size: 409128991
sif: "https://datasets.datalad.org/shub/jpetucci/tensorflow_icsaci/cpu/2019-06-10-f8ea1ccd-ab49489f/ab49489f048c3400d99ca8d463d6ce94.simg"
url: https://datasets.datalad.org/shub/jpetucci/tensorflow_icsaci/cpu/2019-06-10-f8ea1ccd-ab49489f/
recipe: https://datasets.datalad.org/shub/jpetucci/tensorflow_icsaci/cpu/2019-06-10-f8ea1ccd-ab49489f/Singularity
collection: jpetucci/tensorflow_icsaci
---

# jpetucci/tensorflow_icsaci:cpu

```bash
$ singularity pull shub://jpetucci/tensorflow_icsaci:cpu
```

## Singularity Recipe

```singularity
# latest tensorflow_gpu for ICS-ACI

BootStrap: docker
From: tensorflow/tensorflow:latest

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

