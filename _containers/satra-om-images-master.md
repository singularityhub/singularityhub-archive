---
id: 418
name: "satra/om-images"
branch: "master"
tag: "master"
commit: "6131a481f9707d1b8f53bf62ebe9b8098de4d0ff"
version: "738db56316e4fa20f3dba7ac379fd821"
build_date: "2020-07-28T13:17:25.799Z"
size_mb: 471
size: 157551869
sif: "https://datasets.datalad.org/shub/satra/om-images/master/2020-07-28-6131a481-738db563/738db56316e4fa20f3dba7ac379fd821.img.gz"
datalad_url: https://datasets.datalad.org?dir=/shub/satra/om-images/master/2020-07-28-6131a481-738db563/
recipe: https://datasets.datalad.org/shub/satra/om-images/master/2020-07-28-6131a481-738db563/Singularity
collection: satra/om-images
---

# satra/om-images:master

```bash
$ singularity pull shub://satra/om-images:master
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:8.5

%post
    export LANG=C.UTF-8
    export LC_ALL=C
    apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 git
    mkdir /om
    mkdir /cm
```

## Collection

 - Name: [satra/om-images](https://github.com/satra/om-images)
 - License: None

