---
id: 9735
name: "jpetucci/tensorflow_icsaci"
branch: "master"
tag: "gpu"
commit: "f8ea1ccdb4c0021982dccba87b528b59a91bd0ff"
version: "b9c99523c9ceb1c7108544eddbb26759"
build_date: "2019-09-10T13:33:19.692Z"
size_mb: 3250
size: 1647173663
sif: "https://datasets.datalad.org/shub/jpetucci/tensorflow_icsaci/gpu/2019-09-10-f8ea1ccd-b9c99523/b9c99523c9ceb1c7108544eddbb26759.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jpetucci/tensorflow_icsaci/gpu/2019-09-10-f8ea1ccd-b9c99523/
recipe: https://datasets.datalad.org/shub/jpetucci/tensorflow_icsaci/gpu/2019-09-10-f8ea1ccd-b9c99523/Singularity
collection: jpetucci/tensorflow_icsaci
---

# jpetucci/tensorflow_icsaci:gpu

```bash
$ singularity pull shub://jpetucci/tensorflow_icsaci:gpu
```

## Singularity Recipe

```singularity
# latest tensorflow_gpu for ICS-ACI

BootStrap: docker
From: tensorflow/tensorflow:latest-gpu

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

