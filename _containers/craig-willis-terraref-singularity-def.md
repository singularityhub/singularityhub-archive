---
id: 5689
name: "craig-willis/terraref-singularity"
branch: "master"
tag: "def"
commit: "b292f11ab550132f581b6accdd355149556c4bdc"
version: "f6b4584a5e26f9eddbfddb4ee24f5dbe"
build_date: "2018-11-22T17:35:50.418Z"
size_mb: 1553
size: 610099231
sif: "https://datasets.datalad.org/shub/craig-willis/terraref-singularity/def/2018-11-22-b292f11a-f6b4584a/f6b4584a5e26f9eddbfddb4ee24f5dbe.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/craig-willis/terraref-singularity/def/2018-11-22-b292f11a-f6b4584a/
recipe: https://datasets.datalad.org/shub/craig-willis/terraref-singularity/def/2018-11-22-b292f11a-f6b4584a/Singularity
collection: craig-willis/terraref-singularity
---

# craig-willis/terraref-singularity:def

```bash
$ singularity pull shub://craig-willis/terraref-singularity:def
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: terraref/workflow-pilot

%post
   mkdir /data
```

## Collection

 - Name: [craig-willis/terraref-singularity](https://github.com/craig-willis/terraref-singularity)
 - License: None

