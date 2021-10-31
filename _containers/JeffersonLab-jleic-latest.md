---
id: 1120
name: "JeffersonLab/jleic"
branch: "master"
tag: "latest"
commit: "3fedef7b71f0f1e475629c461f652eab26f3e431"
version: "658cb70329912303ba317b52071c50a1"
build_date: "2017-12-13T01:42:44.984Z"
size_mb: 5118
size: 1697038367
sif: "https://datasets.datalad.org/shub/JeffersonLab/jleic/latest/2017-12-13-3fedef7b-658cb703/658cb70329912303ba317b52071c50a1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/JeffersonLab/jleic/latest/2017-12-13-3fedef7b-658cb703/
recipe: https://datasets.datalad.org/shub/JeffersonLab/jleic/latest/2017-12-13-3fedef7b-658cb703/Singularity
collection: JeffersonLab/jleic
---

# JeffersonLab/jleic:latest

```bash
$ singularity pull shub://JeffersonLab/jleic:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: jeffersonlab/jleic

%files

%labels
MAINTAINER EIC Softare Consortium Containers Working Group

%environment

%runscript
exec /bin/bash "$@"

%post
```

## Collection

 - Name: [JeffersonLab/jleic](https://github.com/JeffersonLab/jleic)
 - License: None

