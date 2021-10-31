---
id: 12002
name: "stubbi/nqs"
branch: "master"
tag: "latest"
commit: "9cf8313c920147aa08ea227cad560246f499b0b9"
version: "621e88b9a502a80657ae7a4ec271e109"
build_date: "2021-03-08T05:30:09.388Z"
size_mb: 2200.0
size: 744898591
sif: "https://datasets.datalad.org/shub/stubbi/nqs/latest/2021-03-08-9cf8313c-621e88b9/621e88b9a502a80657ae7a4ec271e109.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/stubbi/nqs/latest/2021-03-08-9cf8313c-621e88b9/
recipe: https://datasets.datalad.org/shub/stubbi/nqs/latest/2021-03-08-9cf8313c-621e88b9/Singularity
collection: stubbi/nqs
---

# stubbi/nqs:latest

```bash
$ singularity pull shub://stubbi/nqs:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.7

%files
    ./ nqs/

%post
    apt-get update
    apt-get install -y --no-install-recommends apt-transport-https ca-certificates gnupg software-properties-common wget
    wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | apt-key add -
    apt-add-repository 'deb https://apt.kitware.com/ubuntu/ bionic main'
    apt-get install -y --no-install-recommends cmake openmpi-bin libopenmpi-dev libatlas-base-dev python-dev python-pip libssl-dev
    pip install -U pip setuptools numpy scipy
    pip install matplotlib
    pip install pandas
    pip install mpi4py
    chmod -R 755 /nqs/
    cd nqs
    python setup.py install
```

## Collection

 - Name: [stubbi/nqs](https://github.com/stubbi/nqs)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

