---
id: 8869
name: "ReproNim/containers"
branch: "master"
tag: "bids-brainiak-srm--latest"
commit: "697f419c659db6088f9fb810afdf14b3cf0d3ac2"
version: "3a7f511ce694905d6197081c2d5d4dc5"
build_date: "2021-03-19T23:51:54.725Z"
size_mb: 1183
size: 558317599
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-brainiak-srm--latest/2021-03-19-697f419c-3a7f511c/3a7f511ce694905d6197081c2d5d4dc5.simg"
url: https://datasets.datalad.org/shub/ReproNim/containers/bids-brainiak-srm--latest/2021-03-19-697f419c-3a7f511c/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-brainiak-srm--latest/2021-03-19-697f419c-3a7f511c/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-brainiak-srm--latest

```bash
$ singularity pull shub://ReproNim/containers:bids-brainiak-srm--latest
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/brainiak-srm:latest

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

