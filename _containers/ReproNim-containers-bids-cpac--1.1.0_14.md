---
id: 8871
name: "ReproNim/containers"
branch: "master"
tag: "bids-cpac--1.1.0_14"
commit: "697f419c659db6088f9fb810afdf14b3cf0d3ac2"
version: "9b682ad1bd73d10e3fd7dd333411a840"
build_date: "2021-03-19T23:51:53.703Z"
size_mb: 4088
size: 1598369823
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-cpac--1.1.0_14/2021-03-19-697f419c-9b682ad1/9b682ad1bd73d10e3fd7dd333411a840.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ReproNim/containers/bids-cpac--1.1.0_14/2021-03-19-697f419c-9b682ad1/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-cpac--1.1.0_14/2021-03-19-697f419c-9b682ad1/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-cpac--1.1.0_14

```bash
$ singularity pull shub://ReproNim/containers:bids-cpac--1.1.0_14
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/cpac:v1.1.0_14

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

