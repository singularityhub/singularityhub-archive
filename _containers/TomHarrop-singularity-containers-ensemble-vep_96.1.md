---
id: 9606
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "ensemble-vep_96.1"
commit: "58c3785cbeed157eb4ed0a52a0830e24eb506e6d"
version: "3b3c862c36d3dadc500b82c1e07e4751"
build_date: "2019-06-06T09:15:14.841Z"
size_mb: 647
size: 174727199
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/ensemble-vep_96.1/2019-06-06-58c3785c-3b3c862c/3b3c862c36d3dadc500b82c1e07e4751.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/ensemble-vep_96.1/2019-06-06-58c3785c-3b3c862c/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/ensemble-vep_96.1/2019-06-06-58c3785c-3b3c862c/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:ensemble-vep_96.1

```bash
$ singularity pull shub://TomHarrop/singularity-containers:ensemble-vep_96.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ensemblorg/ensembl-vep:release_96.1

%help

    ensembl-vep 96.1
    https://github.com/Ensembl/ensembl-vep#haplo
    
%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "ensembl-vep 96.1"

%runscript

    exec /opt/vep/src/ensembl-vep/vep "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

