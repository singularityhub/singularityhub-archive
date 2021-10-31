---
id: 5728
name: "nuitrcs/fenics"
branch: "master"
tag: "latest"
commit: "eaf17fbac5f1d1c17038caf6c6b9e87725ec9f0a"
version: "779bfc6c43cb5b1d71fb1e009e85d678"
build_date: "2021-02-08T21:59:59.309Z"
size_mb: 1841
size: 576983071
sif: "https://datasets.datalad.org/shub/nuitrcs/fenics/latest/2021-02-08-eaf17fba-779bfc6c/779bfc6c43cb5b1d71fb1e009e85d678.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/nuitrcs/fenics/latest/2021-02-08-eaf17fba-779bfc6c/
recipe: https://datasets.datalad.org/shub/nuitrcs/fenics/latest/2021-02-08-eaf17fba-779bfc6c/Singularity
collection: nuitrcs/fenics
---

# nuitrcs/fenics:latest

```bash
$ singularity pull shub://nuitrcs/fenics:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: quay.io/fenicsproject/stable:current

%post
    apt-get update && apt-get -y install python3-tk
    ldconfig

%files
    WELCOME /usr/local/share/WELCOME

%runscript
    cat /usr/local/share/WELCOME 
    exec /bin/bash -i
```

## Collection

 - Name: [nuitrcs/fenics](https://github.com/nuitrcs/fenics)
 - License: None

