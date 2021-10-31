---
id: 8868
name: "ReproNim/containers"
branch: "master"
tag: "bids-baracus--1.1.2"
commit: "697f419c659db6088f9fb810afdf14b3cf0d3ac2"
version: "11916fef54c4938282b4ab0e924d9872"
build_date: "2019-09-17T14:25:00.521Z"
size_mb: 6504
size: 3064270879
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-baracus--1.1.2/2019-09-17-697f419c-11916fef/11916fef54c4938282b4ab0e924d9872.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ReproNim/containers/bids-baracus--1.1.2/2019-09-17-697f419c-11916fef/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-baracus--1.1.2/2019-09-17-697f419c-11916fef/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-baracus--1.1.2

```bash
$ singularity pull shub://ReproNim/containers:bids-baracus--1.1.2
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/baracus:v1.1.2

%post

# Create commonly present root directories to avoid need in overlays not supported
# on older systems
mkdir -p /ihome /data /data2 /zfs /isi /dartfs /dartfs-hpc

%environment
export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"

# TODO: Take advantage of the fact that it is a bids-app somehow?
```

## Collection

 - Name: [ReproNim/containers](https://github.com/ReproNim/containers)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

