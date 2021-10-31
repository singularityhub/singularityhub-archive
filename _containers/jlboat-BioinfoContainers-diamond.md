---
id: 8858
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "diamond"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "69da9f24f3962bf1ac3d20770991e468"
build_date: "2019-05-08T15:11:14.053Z"
size_mb: 153
size: 65265695
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/diamond/2019-05-08-5f15386e-69da9f24/69da9f24f3962bf1ac3d20770991e468.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jlboat/BioinfoContainers/diamond/2019-05-08-5f15386e-69da9f24/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/diamond/2019-05-08-5f15386e-69da9f24/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:diamond

```bash
$ singularity pull shub://jlboat/BioinfoContainers:diamond
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: debian:latest

%post
    apt-get update --fix-missing && apt-get install -y wget
    wget https://github.com/bbuchfink/diamond/releases/download/v0.9.22/diamond-linux64.tar.gz
    tar xzf diamond-linux64.tar.gz
    cp diamond /usr/local/bin

%runscript
    exec "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

