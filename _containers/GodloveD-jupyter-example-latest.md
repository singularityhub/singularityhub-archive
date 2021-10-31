---
id: 45
name: "GodloveD/jupyter-example"
branch: "master"
tag: "latest"
commit: "2d45408d77fcf9654399e4a4a48f1201843f3f14"
version: "c9fbcba8b012dc3fc80bce8b8d98a8a5"
build_date: "2020-01-22T16:02:59.654Z"
size_mb: 625
size: 226410527
sif: "https://datasets.datalad.org/shub/GodloveD/jupyter-example/latest/2020-01-22-2d45408d-c9fbcba8/c9fbcba8b012dc3fc80bce8b8d98a8a5.simg"
url: https://datasets.datalad.org/shub/GodloveD/jupyter-example/latest/2020-01-22-2d45408d-c9fbcba8/
recipe: https://datasets.datalad.org/shub/GodloveD/jupyter-example/latest/2020-01-22-2d45408d-c9fbcba8/Singularity
collection: GodloveD/jupyter-example
---

# GodloveD/jupyter-example:latest

```bash
$ singularity pull shub://GodloveD/jupyter-example:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:latest

%post
    apt-get update
    apt-get -y install python3 python3-pip
    pip3 install jupyter
```

## Collection

 - Name: [GodloveD/jupyter-example](https://github.com/GodloveD/jupyter-example)
 - License: None

