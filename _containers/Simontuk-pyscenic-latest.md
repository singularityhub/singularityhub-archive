---
id: 11178
name: "Simontuk/pyscenic"
branch: "master"
tag: "latest"
commit: "4b433c23c51f64472e99f86425d759fd7199ce14"
version: "57980fc249af605e4e37ca1447fee720"
build_date: "2021-04-19T17:18:31.654Z"
size_mb: 1550.0
size: 512151583
sif: "https://datasets.datalad.org/shub/Simontuk/pyscenic/latest/2021-04-19-4b433c23-57980fc2/57980fc249af605e4e37ca1447fee720.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/Simontuk/pyscenic/latest/2021-04-19-4b433c23-57980fc2/
recipe: https://datasets.datalad.org/shub/Simontuk/pyscenic/latest/2021-04-19-4b433c23-57980fc2/Singularity
collection: Simontuk/pyscenic
---

# Simontuk/pyscenic:latest

```bash
$ singularity pull shub://Simontuk/pyscenic:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: python:3.7.4-slim

%files
    ./requirements_docker.txt /tmp/

%post
    BUILDPKGS="build-essential apt-utils \
        python3-dev libhdf5-dev libfreetype6-dev libtool \
        m4 autoconf automake patch bison flex libpng-dev libopenblas-dev \
        tcl-dev tk-dev libxml2-dev zlib1g-dev libffi-dev cmake"
    apt-get update
    apt-get install -y debconf locales && dpkg-reconfigure locales
    apt-get install -y zlib1g hdf5-tools gfortran libgcc1 libstdc++6 musl \
        libopenblas-base tcl tk libxml2 libffi6 less procps
    apt-get install -y $BUILDPKGS

    pip install --no-cache-dir -r /tmp/requirements_docker.txt
    pip install --no-cache-dir  --no-dependencies --upgrade pyscenic==0.9.18
    pip install --no-cache-dir scanpy==1.4.4.post1

    apt-get remove --purge -y $BUILDPKGS && \
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [Simontuk/pyscenic](https://github.com/Simontuk/pyscenic)
 - License: None

