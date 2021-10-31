---
id: 8883
name: "ReproNim/containers"
branch: "master"
tag: "bids-rshrf--1.0.0"
commit: "697f419c659db6088f9fb810afdf14b3cf0d3ac2"
version: "982994fa815402a45497c28a0c7eaecb"
build_date: "2019-05-08T15:10:10.252Z"
size_mb: 220
size: 65863711
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-rshrf--1.0.0/2019-05-08-697f419c-982994fa/982994fa815402a45497c28a0c7eaecb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ReproNim/containers/bids-rshrf--1.0.0/2019-05-08-697f419c-982994fa/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-rshrf--1.0.0/2019-05-08-697f419c-982994fa/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-rshrf--1.0.0

```bash
$ singularity pull shub://ReproNim/containers:bids-rshrf--1.0.0
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/rshrf:1.0.0

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

