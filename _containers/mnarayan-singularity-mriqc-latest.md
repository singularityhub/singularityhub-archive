---
id: 7025
name: "mnarayan/singularity-mriqc"
branch: "master"
tag: "latest"
commit: "88484c04ab951ea8d6935a2eaa103ed68cd479df"
version: "380ff1fef62b91cdf51302e2d01fbbb8"
build_date: "2019-02-08T05:38:46.764Z"
size_mb: 7275
size: 2781982751
sif: "https://datasets.datalad.org/shub/mnarayan/singularity-mriqc/latest/2019-02-08-88484c04-380ff1fe/380ff1fef62b91cdf51302e2d01fbbb8.simg"
url: https://datasets.datalad.org/shub/mnarayan/singularity-mriqc/latest/2019-02-08-88484c04-380ff1fe/
recipe: https://datasets.datalad.org/shub/mnarayan/singularity-mriqc/latest/2019-02-08-88484c04-380ff1fe/Singularity
collection: mnarayan/singularity-mriqc
---

# mnarayan/singularity-mriqc:latest

```bash
$ singularity pull shub://mnarayan/singularity-mriqc:latest
```

## Singularity Recipe

```singularity
# MRIQC from poldracklab

BootStrap: docker
FROM: poldracklab/mriqc:latest

%runscript
    exec /usr/local/miniconda/bin/mriqc "$@"

%environment

%labels
Author mnarayan@noreply.users.github.com
Build-date 2/5/2019
Vendor Ubuntu
Version 16.04

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

