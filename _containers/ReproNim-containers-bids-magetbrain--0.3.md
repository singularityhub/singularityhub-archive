---
id: 8876
name: "ReproNim/containers"
branch: "master"
tag: "bids-magetbrain--0.3"
commit: "f46580a54610b922fde9bb21b7c1074a2c3577b5"
version: "3eff65fd1d6d10886c6cc8f843065643"
build_date: "2021-03-19T23:51:54.068Z"
size_mb: 5918
size: 4551880735
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-magetbrain--0.3/2021-03-19-f46580a5-3eff65fd/3eff65fd1d6d10886c6cc8f843065643.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ReproNim/containers/bids-magetbrain--0.3/2021-03-19-f46580a5-3eff65fd/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-magetbrain--0.3/2021-03-19-f46580a5-3eff65fd/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-magetbrain--0.3

```bash
$ singularity pull shub://ReproNim/containers:bids-magetbrain--0.3
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/magetbrain:v0.3

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

