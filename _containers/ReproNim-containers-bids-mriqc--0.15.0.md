---
id: 8591
name: "ReproNim/containers"
branch: "master"
tag: "bids-mriqc--0.15.0"
commit: "585d6728cfe632f0c118cfd92687b928e43ab7be"
version: "b76d4d850bf94dbea13d0a3331451842"
build_date: "2019-05-03T16:23:22.418Z"
size_mb: 7589
size: 2928967711
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-mriqc--0.15.0/2019-05-03-585d6728-b76d4d85/b76d4d850bf94dbea13d0a3331451842.simg"
url: https://datasets.datalad.org/shub/ReproNim/containers/bids-mriqc--0.15.0/2019-05-03-585d6728-b76d4d85/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-mriqc--0.15.0/2019-05-03-585d6728-b76d4d85/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-mriqc--0.15.0

```bash
$ singularity pull shub://ReproNim/containers:bids-mriqc--0.15.0
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: poldracklab/mriqc:0.15.0

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

