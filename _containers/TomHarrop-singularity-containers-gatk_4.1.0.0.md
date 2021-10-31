---
id: 7420
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "gatk_4.1.0.0"
commit: "4ef3f8ebfa7da5ec51b706feb9bd262dfb400f9b"
version: "0988aabb25d01bdb4a2af5e39c4cc110"
build_date: "2019-02-25T11:54:41.673Z"
size_mb: 3589
size: 1388159007
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/gatk_4.1.0.0/2019-02-25-4ef3f8eb-0988aabb/0988aabb25d01bdb4a2af5e39c4cc110.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/gatk_4.1.0.0/2019-02-25-4ef3f8eb-0988aabb/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/gatk_4.1.0.0/2019-02-25-4ef3f8eb-0988aabb/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:gatk_4.1.0.0

```bash
$ singularity pull shub://TomHarrop/singularity-containers:gatk_4.1.0.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: broadinstitute/gatk:4.1.0.0

%help
    GATK 4.1.0.0

%labels
    VERSION "GATK 4.1.0.0"

%runscript
    exec /gatk/gatk "$@"

%environment
    export PATH="${PATH}:/gatk:/gatk/scripts"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

