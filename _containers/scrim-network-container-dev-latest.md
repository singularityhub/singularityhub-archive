---
id: 7724
name: "scrim-network/container-dev"
branch: "master"
tag: "latest"
commit: "e29cdb5f54be50e90814a357d5c6ca036e0c060e"
version: "bc8eb652975fdf31b13878c669faab74"
build_date: "2019-03-13T03:34:53.267Z"
size_mb: 418
size: 172736543
sif: "https://datasets.datalad.org/shub/scrim-network/container-dev/latest/2019-03-13-e29cdb5f-bc8eb652/bc8eb652975fdf31b13878c669faab74.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/scrim-network/container-dev/latest/2019-03-13-e29cdb5f-bc8eb652/
recipe: https://datasets.datalad.org/shub/scrim-network/container-dev/latest/2019-03-13-e29cdb5f-bc8eb652/Singularity
collection: scrim-network/container-dev
---

# scrim-network/container-dev:latest

```bash
$ singularity pull shub://scrim-network/container-dev:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: singularityhub/ubuntu

%runscript
    exec echo "The runscript is the containers default runtime command!"

%environment
    VARIABLE=MEATBALLVALUE
    export VARIABLE

%labels
   AUTHOR vsochat@stanford.edu

%post
    apt-get update && apt-get -y install python3 git wget
    mkdir /data
    echo "The post section is where you can install, and configure your container."
```

## Collection

 - Name: [scrim-network/container-dev](https://github.com/scrim-network/container-dev)
 - License: None

