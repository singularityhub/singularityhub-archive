---
id: 8865
name: "ReproNim/containers"
branch: "master"
tag: "bids-aa--0.2.0"
commit: "697f419c659db6088f9fb810afdf14b3cf0d3ac2"
version: "22f80818c7431bd3ec6959e1a9fc6314"
build_date: "2021-03-19T23:51:52.831Z"
size_mb: 13135
size: 6596276255
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-aa--0.2.0/2021-03-19-697f419c-22f80818/22f80818c7431bd3ec6959e1a9fc6314.simg"
url: https://datasets.datalad.org/shub/ReproNim/containers/bids-aa--0.2.0/2021-03-19-697f419c-22f80818/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-aa--0.2.0/2021-03-19-697f419c-22f80818/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-aa--0.2.0

```bash
$ singularity pull shub://ReproNim/containers:bids-aa--0.2.0
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/aa:v0.2.0

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

