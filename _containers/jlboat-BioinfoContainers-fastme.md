---
id: 8891
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "fastme"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "333e2ce84b282bebff803cef51967fe9"
build_date: "2019-05-08T15:11:14.077Z"
size_mb: 318
size: 115388447
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/fastme/2019-05-08-5f15386e-333e2ce8/333e2ce84b282bebff803cef51967fe9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jlboat/BioinfoContainers/fastme/2019-05-08-5f15386e-333e2ce8/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/fastme/2019-05-08-5f15386e-333e2ce8/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:fastme

```bash
$ singularity pull shub://jlboat/BioinfoContainers:fastme
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:latest

%post
    apt-get update --fix-missing && apt-get install -y wget build-essential automake
    cd /opt/
    wget https://gite.lirmm.fr/atgc/FastME/raw/master/tarball/fastme-2.1.6.1.tar.gz
    tar -xvzf fastme-2.1.6.1.tar.gz
    rm fastme-2.1.6.1.tar.gz
    cd fastme-2.1.6.1
    ./configure
    make
    make install
    chmod -R 777 /opt/*

%runscript
    exec "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

