---
id: 8879
name: "ReproNim/containers"
branch: "master"
tag: "bids-niak--latest"
commit: "697f419c659db6088f9fb810afdf14b3cf0d3ac2"
version: "0fab8ab172e488289e4712f9c8a7d400"
build_date: "2021-03-19T23:51:53.630Z"
size_mb: 4602
size: 1885401119
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-niak--latest/2021-03-19-697f419c-0fab8ab1/0fab8ab172e488289e4712f9c8a7d400.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ReproNim/containers/bids-niak--latest/2021-03-19-697f419c-0fab8ab1/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-niak--latest/2021-03-19-697f419c-0fab8ab1/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-niak--latest

```bash
$ singularity pull shub://ReproNim/containers:bids-niak--latest
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/niak:latest

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

