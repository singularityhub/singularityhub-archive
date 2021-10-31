---
id: 8915
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "vg"
commit: "01fd237ed1c7688e532770e499b506f0d189a7b5"
version: "4eb3bb2dbc3e11035a0dbf96d9a79e11"
build_date: "2019-09-24T17:34:52.539Z"
size_mb: 157
size: 61243423
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/vg/2019-09-24-01fd237e-4eb3bb2d/4eb3bb2dbc3e11035a0dbf96d9a79e11.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/vg/2019-09-24-01fd237e-4eb3bb2d/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/vg/2019-09-24-01fd237e-4eb3bb2d/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:vg

```bash
$ singularity pull shub://jlboat/BioinfoContainers:vg
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: debian:latest

%labels
    Topic Bioinformatics
    vg v1.15.0

%post
    apt-get update --fix-missing && apt-get install -y wget && rm -rf /var/lib/apt/lists/*
    wget https://github.com/vgteam/vg/releases/download/v1.15.0/vg
    mv vg /usr/bin/
    apt-get remove -y wget
    chmod 777 /usr/bin/vg

%runscript
    exec vg "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

