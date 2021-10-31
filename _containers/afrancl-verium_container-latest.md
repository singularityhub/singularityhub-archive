---
id: 1301
name: "afrancl/verium_container"
branch: "master"
tag: "latest"
commit: "824d8c3dbe3b719e4d806b30e8dea2b916ad4f0c"
version: "7b9630ff231c94ee0dc9c0a7e75072ef"
build_date: "2018-01-15T15:00:26.285Z"
size_mb: 416
size: 163967007
sif: "https://datasets.datalad.org/shub/afrancl/verium_container/latest/2018-01-15-824d8c3d-7b9630ff/7b9630ff231c94ee0dc9c0a7e75072ef.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/afrancl/verium_container/latest/2018-01-15-824d8c3d-7b9630ff/
recipe: https://datasets.datalad.org/shub/afrancl/verium_container/latest/2018-01-15-824d8c3d-7b9630ff/Singularity
collection: afrancl/verium_container
---

# afrancl/verium_container:latest

```bash
$ singularity pull shub://afrancl/verium_container:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%post
    apt-get update && apt-get -y install locales
    locale-gen en_US.UTF-8
    apt-get -y install automake autoconf pkg-config libcurl4-openssl-dev libjansson-dev libssl-dev libgmp-dev zlib1g-dev
    apt-get clean
```

## Collection

 - Name: [afrancl/verium_container](https://github.com/afrancl/verium_container)
 - License: None

