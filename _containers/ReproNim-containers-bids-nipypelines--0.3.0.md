---
id: 8880
name: "ReproNim/containers"
branch: "master"
tag: "bids-nipypelines--0.3.0"
commit: "2b6f83c739d62636d186ac4dabefde54026c8f81"
version: "486cfe25ad376bcadb769fc3df3b876a"
build_date: "2021-03-19T23:51:54.142Z"
size_mb: 1447
size: 499011615
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-nipypelines--0.3.0/2021-03-19-2b6f83c7-486cfe25/486cfe25ad376bcadb769fc3df3b876a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ReproNim/containers/bids-nipypelines--0.3.0/2021-03-19-2b6f83c7-486cfe25/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-nipypelines--0.3.0/2021-03-19-2b6f83c7-486cfe25/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-nipypelines--0.3.0

```bash
$ singularity pull shub://ReproNim/containers:bids-nipypelines--0.3.0
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/nipypelines:0.3.0

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

