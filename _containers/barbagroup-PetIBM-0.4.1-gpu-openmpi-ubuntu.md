---
id: 9669
name: "barbagroup/PetIBM"
branch: "master"
tag: "0.4.1-gpu-openmpi-ubuntu"
commit: "0d5019299732c5b97bb22ad65808f11e244b9ed5"
version: "a2ef12673f963f11ce58766ef666b2fb"
build_date: "2019-08-13T20:00:13.812Z"
size_mb: 4449
size: 1470746655
sif: "https://datasets.datalad.org/shub/barbagroup/PetIBM/0.4.1-gpu-openmpi-ubuntu/2019-08-13-0d501929-a2ef1267/a2ef12673f963f11ce58766ef666b2fb.simg"
url: https://datasets.datalad.org/shub/barbagroup/PetIBM/0.4.1-gpu-openmpi-ubuntu/2019-08-13-0d501929-a2ef1267/
recipe: https://datasets.datalad.org/shub/barbagroup/PetIBM/0.4.1-gpu-openmpi-ubuntu/2019-08-13-0d501929-a2ef1267/Singularity
collection: barbagroup/PetIBM
---

# barbagroup/PetIBM:0.4.1-gpu-openmpi-ubuntu

```bash
$ singularity pull shub://barbagroup/PetIBM:0.4.1-gpu-openmpi-ubuntu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: barbagroup/petibm:0.4.1-GPU-OpenMPI-ubuntu
IncludeCmd: yes

%labels
    AUTHOR mesnardo@gwu.edu
```

## Collection

 - Name: [barbagroup/PetIBM](https://github.com/barbagroup/PetIBM)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

