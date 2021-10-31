---
id: 8870
name: "ReproNim/containers"
branch: "master"
tag: "bids-broccoli--1.0.1"
commit: "697f419c659db6088f9fb810afdf14b3cf0d3ac2"
version: "fcd1915ed808029b0f792b634ac1261c"
build_date: "2021-03-19T23:51:52.757Z"
size_mb: 6140
size: 3125166111
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-broccoli--1.0.1/2021-03-19-697f419c-fcd1915e/fcd1915ed808029b0f792b634ac1261c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ReproNim/containers/bids-broccoli--1.0.1/2021-03-19-697f419c-fcd1915e/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-broccoli--1.0.1/2021-03-19-697f419c-fcd1915e/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-broccoli--1.0.1

```bash
$ singularity pull shub://ReproNim/containers:bids-broccoli--1.0.1
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/broccoli:v1.0.1

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

