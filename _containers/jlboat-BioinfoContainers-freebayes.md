---
id: 8807
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "freebayes"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "5fc46505892206be0be8b6d90f882d96"
build_date: "2019-05-08T15:11:14.174Z"
size_mb: 645
size: 255422495
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/freebayes/2019-05-08-5f15386e-5fc46505/5fc46505892206be0be8b6d90f882d96.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jlboat/BioinfoContainers/freebayes/2019-05-08-5f15386e-5fc46505/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/freebayes/2019-05-08-5f15386e-5fc46505/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:freebayes

```bash
$ singularity pull shub://jlboat/BioinfoContainers:freebayes
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:latest

%help
    singularity run freebayes.simg -h

%post
    apt-get update --fix-missing && apt-get install -y git g++ make zlib1g-dev libbz2-1.0 libbz2-dev liblzma-dev
    cd /opt/
    git clone --recursive git://github.com/ekg/freebayes.git
    cd freebayes
    make
    make install
    chmod -R 777 /opt/freebayes

%runscript
    exec freebayes "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

