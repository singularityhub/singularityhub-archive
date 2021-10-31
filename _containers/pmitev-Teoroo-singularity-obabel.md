---
id: 7938
name: "pmitev/Teoroo-singularity"
branch: "master"
tag: "obabel"
commit: "f57ca151e831a7d742716c481e8b683d0aca8a62"
version: "477dc798a0509ec9d868739515d7b6da"
build_date: "2019-03-25T23:16:30.295Z"
size_mb: 250
size: 99803167
sif: "https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/obabel/2019-03-25-f57ca151-477dc798/477dc798a0509ec9d868739515d7b6da.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pmitev/Teoroo-singularity/obabel/2019-03-25-f57ca151-477dc798/
recipe: https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/obabel/2019-03-25-f57ca151-477dc798/Singularity
collection: pmitev/Teoroo-singularity
---

# pmitev/Teoroo-singularity:obabel

```bash
$ singularity pull shub://pmitev/Teoroo-singularity:obabel
```

## Singularity Recipe

```singularity
Bootstrap:  docker
From: debian:buster

%runscript
  obabel $*

%setup

%files

%environment

%labels

%post
  echo 'deb http://deb.debian.org/debian experimental main' >> /etc/apt/sources.list

  apt-get update -y && apt-get upgrade -y &&\
  apt-get install -y --no-install-recommends zip unzip &&\
  apt-get install -y -t experimental openbabel python-openbabel &&\
  apt-get clean
```

## Collection

 - Name: [pmitev/Teoroo-singularity](https://github.com/pmitev/Teoroo-singularity)
 - License: None

