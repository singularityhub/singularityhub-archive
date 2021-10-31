---
id: 4196
name: "MPIB/singularity-mriqc"
branch: "master"
tag: "0.11.0"
commit: "450fe071bdf5fba3c3adf7b0362bf83aae02ac3f"
version: "416563bca4c33f8de0cef097ede80f87"
build_date: "2018-08-28T03:21:34.905Z"
size_mb: 7163
size: 2778464287
sif: "https://datasets.datalad.org/shub/MPIB/singularity-mriqc/0.11.0/2018-08-28-450fe071-416563bc/416563bca4c33f8de0cef097ede80f87.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/MPIB/singularity-mriqc/0.11.0/2018-08-28-450fe071-416563bc/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-mriqc/0.11.0/2018-08-28-450fe071-416563bc/Singularity
collection: MPIB/singularity-mriqc
---

# MPIB/singularity-mriqc:0.11.0

```bash
$ singularity pull shub://MPIB/singularity-mriqc:0.11.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: poldracklab/mriqc:0.11.0




%post
    apt-get update && apt-get -y purge libgsl2 && apt-get -y  install libgsl2
```

## Collection

 - Name: [MPIB/singularity-mriqc](https://github.com/MPIB/singularity-mriqc)
 - License: None

