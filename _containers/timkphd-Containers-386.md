---
id: 10834
name: "timkphd/Containers"
branch: "master"
tag: "386"
commit: "96c5bb9357f5f6cdb91664d8db28d51e64a64ef8"
version: "9da75bb0db3e2bf603d81711fc9f3da7093d1fe07a273ef3de74539602f87874"
build_date: "2019-09-09T18:45:02.201Z"
size_mb: 292.59765625
size: 306810880
sif: "https://datasets.datalad.org/shub/timkphd/Containers/386/2019-09-09-96c5bb93-9da75bb0/9da75bb0db3e2bf603d81711fc9f3da7093d1fe07a273ef3de74539602f87874.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/timkphd/Containers/386/2019-09-09-96c5bb93-9da75bb0/
recipe: https://datasets.datalad.org/shub/timkphd/Containers/386/2019-09-09-96c5bb93-9da75bb0/Singularity
collection: timkphd/stuff
---

# timkphd/Containers:386

```bash
$ singularity pull shub://timkphd/Containers:386
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: i686/python
# Sep 09 12:38 PM
%post
    apt-get -y update --fix-missing
    apt-get -y install wget
    apt-get -y install gawk
    apt-get -y install apt-transport-https

# Intalling Fortran also gives us C.    
    apt install -y gfortran 
    apt install -y g++
    apt install -y make
date

# Install editors
  apt install -y nano
  apt install -y vim


%environment
    export LC_ALL=C

%labels
    Author thkphd
```

## Collection

 - Name: [timkphd/Containers](https://github.com/timkphd/Containers)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

