---
id: 8873
name: "ReproNim/containers"
branch: "master"
tag: "bids-example--0.0.7"
commit: "697f419c659db6088f9fb810afdf14b3cf0d3ac2"
version: "4ac13905d51c1e5d48558da8a160fa12"
build_date: "2021-03-19T23:51:53.486Z"
size_mb: 1120
size: 439799839
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-example--0.0.7/2021-03-19-697f419c-4ac13905/4ac13905d51c1e5d48558da8a160fa12.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ReproNim/containers/bids-example--0.0.7/2021-03-19-697f419c-4ac13905/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-example--0.0.7/2021-03-19-697f419c-4ac13905/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-example--0.0.7

```bash
$ singularity pull shub://ReproNim/containers:bids-example--0.0.7
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/example:0.0.7

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

