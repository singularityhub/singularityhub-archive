---
id: 5777
name: "darachm/singularity_csvkit"
branch: "master"
tag: "latest"
commit: "98746952259b4c0ac43d75851049807cc98281cf"
version: "80522af98dc5db7e5697e8dcc97fe57f"
build_date: "2018-12-02T07:01:43.842Z"
size_mb: 256
size: 93904927
sif: "https://datasets.datalad.org/shub/darachm/singularity_csvkit/latest/2018-12-02-98746952-80522af9/80522af98dc5db7e5697e8dcc97fe57f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/darachm/singularity_csvkit/latest/2018-12-02-98746952-80522af9/
recipe: https://datasets.datalad.org/shub/darachm/singularity_csvkit/latest/2018-12-02-98746952-80522af9/Singularity
collection: darachm/singularity_csvkit
---

# darachm/singularity_csvkit:latest

```bash
$ singularity pull shub://darachm/singularity_csvkit:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
MAINTAINER darachm

%help

    This container is for providing `csvkit` for a nextflow pipeline.
    
%post

    apt -y update
    apt -y install csvkit

%test

    /usr/bin/in2csv -h
```

## Collection

 - Name: [darachm/singularity_csvkit](https://github.com/darachm/singularity_csvkit)
 - License: None

