---
id: 7023
name: "mnarayan/singularity-mriqc"
branch: "master"
tag: "0.14.2"
commit: "6964924a2f58c43287e305c0e5a4defc8af56867"
version: "53eea825d3a7f7e951320e6f00710de2"
build_date: "2019-02-08T05:38:46.771Z"
size_mb: 7275
size: 2781982751
sif: "https://datasets.datalad.org/shub/mnarayan/singularity-mriqc/0.14.2/2019-02-08-6964924a-53eea825/53eea825d3a7f7e951320e6f00710de2.simg"
url: https://datasets.datalad.org/shub/mnarayan/singularity-mriqc/0.14.2/2019-02-08-6964924a-53eea825/
recipe: https://datasets.datalad.org/shub/mnarayan/singularity-mriqc/0.14.2/2019-02-08-6964924a-53eea825/Singularity
collection: mnarayan/singularity-mriqc
---

# mnarayan/singularity-mriqc:0.14.2

```bash
$ singularity pull shub://mnarayan/singularity-mriqc:0.14.2
```

## Singularity Recipe

```singularity
# MRIQC from poldracklab

BootStrap: docker
FROM: poldracklab/mriqc:0.14.2

%runscript
    exec /usr/local/miniconda/bin/mriqc "$@"

%environment

%labels
Author mnarayan@noreply.users.github.com
Build-date 2/5/2019
Vendor Ubuntu
Version 0.14.2

%post
    #------------------------------------------------------------------------------
    # Create local binding point for our HPC
    #------------------------------------------------------------------------------
    mkdir /scratch
    mkdir /share
    mkdir /oak
```

## Collection

 - Name: [mnarayan/singularity-mriqc](https://github.com/mnarayan/singularity-mriqc)
 - License: None

