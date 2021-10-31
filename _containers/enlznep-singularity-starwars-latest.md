---
id: 5650
name: "enlznep/singularity-starwars"
branch: "master"
tag: "latest"
commit: "ea95f10b80183ea19fd3b14a5f1f512e9313c3f5"
version: "1a41b555732c219e0f2063ca67fc2c53"
build_date: "2018-11-20T15:05:18.710Z"
size_mb: 99
size: 45961247
sif: "https://datasets.datalad.org/shub/enlznep/singularity-starwars/latest/2018-11-20-ea95f10b-1a41b555/1a41b555732c219e0f2063ca67fc2c53.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/enlznep/singularity-starwars/latest/2018-11-20-ea95f10b-1a41b555/
recipe: https://datasets.datalad.org/shub/enlznep/singularity-starwars/latest/2018-11-20-ea95f10b-1a41b555/Singularity
collection: enlznep/singularity-starwars
---

# enlznep/singularity-starwars:latest

```bash
$ singularity pull shub://enlznep/singularity-starwars:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
    MAINTAINER Ray Marc Marcellones

%post
    apt-get -y update
    apt-get -y install telnet

%runscript
    telnet towel.blinkenlights.nl
```

## Collection

 - Name: [enlznep/singularity-starwars](https://github.com/enlznep/singularity-starwars)
 - License: None

