---
id: 9540
name: "barbagroup/PetIBM"
branch: "master"
tag: "0.4-gpu-openmpi-ubuntu"
commit: "a8fc7ae8dc069220a822496705aa8cec005858a6"
version: "3a704950b0e8f9743386538877530115"
build_date: "2019-08-13T19:59:16.303Z"
size_mb: 4449
size: 1470709791
sif: "https://datasets.datalad.org/shub/barbagroup/PetIBM/0.4-gpu-openmpi-ubuntu/2019-08-13-a8fc7ae8-3a704950/3a704950b0e8f9743386538877530115.simg"
url: https://datasets.datalad.org/shub/barbagroup/PetIBM/0.4-gpu-openmpi-ubuntu/2019-08-13-a8fc7ae8-3a704950/
recipe: https://datasets.datalad.org/shub/barbagroup/PetIBM/0.4-gpu-openmpi-ubuntu/2019-08-13-a8fc7ae8-3a704950/Singularity
collection: barbagroup/PetIBM
---

# barbagroup/PetIBM:0.4-gpu-openmpi-ubuntu

```bash
$ singularity pull shub://barbagroup/PetIBM:0.4-gpu-openmpi-ubuntu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: barbagroup/petibm:0.4-GPU-OpenMPI-ubuntu
IncludeCmd: yes

%labels
    AUTHOR mesnardo@gwu.edu
```

## Collection

 - Name: [barbagroup/PetIBM](https://github.com/barbagroup/PetIBM)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

