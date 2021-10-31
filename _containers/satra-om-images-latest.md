---
id: 415
name: "satra/om-images"
branch: "master"
tag: "latest"
commit: "6131a481f9707d1b8f53bf62ebe9b8098de4d0ff"
version: "05ae942b51bdb3b3541981dbe56eb614"
build_date: "2017-10-19T20:34:17.654Z"
size_mb: 427
size: 111140895
sif: "https://datasets.datalad.org/shub/satra/om-images/latest/2017-10-19-6131a481-05ae942b/05ae942b51bdb3b3541981dbe56eb614.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/satra/om-images/latest/2017-10-19-6131a481-05ae942b/
recipe: https://datasets.datalad.org/shub/satra/om-images/latest/2017-10-19-6131a481-05ae942b/Singularity
collection: satra/om-images
---

# satra/om-images:latest

```bash
$ singularity pull shub://satra/om-images:latest
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

