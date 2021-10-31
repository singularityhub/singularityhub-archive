---
id: 5778
name: "darachm/singularity_bwa"
branch: "master"
tag: "latest"
commit: "7530cad6890917f7dc58f9fdd5b68ce7b0ff060e"
version: "f700be3d309d518105678a05c001076c"
build_date: "2021-03-17T14:26:46.655Z"
size_mb: 99
size: 46104607
sif: "https://datasets.datalad.org/shub/darachm/singularity_bwa/latest/2021-03-17-7530cad6-f700be3d/f700be3d309d518105678a05c001076c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/darachm/singularity_bwa/latest/2021-03-17-7530cad6-f700be3d/
recipe: https://datasets.datalad.org/shub/darachm/singularity_bwa/latest/2021-03-17-7530cad6-f700be3d/Singularity
collection: darachm/singularity_bwa
---

# darachm/singularity_bwa:latest

```bash
$ singularity pull shub://darachm/singularity_bwa:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
MAINTAINER darachm

%help

    This container is for providing `bwa`  for some bioinformatic pipelines.
    
%post

    apt-get -y update
    apt-get -y install bwa

%test

    # ?
```

## Collection

 - Name: [darachm/singularity_bwa](https://github.com/darachm/singularity_bwa)
 - License: None

