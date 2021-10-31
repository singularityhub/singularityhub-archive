---
id: 6154
name: "GregoryAshton/containers"
branch: "master"
tag: "psrchive"
commit: "4a335777771893ba88e80e8f075809c00a0997e7"
version: "a52e7c82a20b06ccd38b3c1c76089992"
build_date: "2021-02-23T16:43:43.843Z"
size_mb: 3616
size: 1582309407
sif: "https://datasets.datalad.org/shub/GregoryAshton/containers/psrchive/2021-02-23-4a335777-a52e7c82/a52e7c82a20b06ccd38b3c1c76089992.simg"
url: https://datasets.datalad.org/shub/GregoryAshton/containers/psrchive/2021-02-23-4a335777-a52e7c82/
recipe: https://datasets.datalad.org/shub/GregoryAshton/containers/psrchive/2021-02-23-4a335777-a52e7c82/Singularity
collection: GregoryAshton/TestBilbySingularity
---

# GregoryAshton/containers:psrchive

```bash
$ singularity pull shub://GregoryAshton/containers:psrchive
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: mpifrpsr/dspsr

%help

A singularity container with psrchive, python-psrchive, and some useful python modules

%post
    pip install pandas
    pip install gwpy
    pip install tables
    pip install ipython
```

## Collection

 - Name: [GregoryAshton/containers](https://github.com/GregoryAshton/containers)
 - License: None

