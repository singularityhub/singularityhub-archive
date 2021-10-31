---
id: 4197
name: "MPIB/singularity-mriqc"
branch: "master"
tag: "0.10.4"
commit: "a1e6c99baf93d6560cc552c7a8479fddb71c0e50"
version: "31563f904807fc3329ce196ec9d2eaa4"
build_date: "2018-08-28T03:21:34.899Z"
size_mb: 7186
size: 2787733535
sif: "https://datasets.datalad.org/shub/MPIB/singularity-mriqc/0.10.4/2018-08-28-a1e6c99b-31563f90/31563f904807fc3329ce196ec9d2eaa4.simg"
url: https://datasets.datalad.org/shub/MPIB/singularity-mriqc/0.10.4/2018-08-28-a1e6c99b-31563f90/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-mriqc/0.10.4/2018-08-28-a1e6c99b-31563f90/Singularity
collection: MPIB/singularity-mriqc
---

# MPIB/singularity-mriqc:0.10.4

```bash
$ singularity pull shub://MPIB/singularity-mriqc:0.10.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: poldracklab/mriqc:0.10.4




%post
    apt-get update && apt-get -y purge libgsl2 && apt-get -y  install libgsl2
```

## Collection

 - Name: [MPIB/singularity-mriqc](https://github.com/MPIB/singularity-mriqc)
 - License: None

