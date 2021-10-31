---
id: 8878
name: "ReproNim/containers"
branch: "master"
tag: "bids-ndmg--0.1.0"
commit: "fb5d9a6495ba517c3c71891237883a702d0bd553"
version: "8b1993e9f90a89976ca2f10a5f1d76d5"
build_date: "2021-03-19T23:51:54.652Z"
size_mb: 1988
size: 906280991
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-ndmg--0.1.0/2021-03-19-fb5d9a64-8b1993e9/8b1993e9f90a89976ca2f10a5f1d76d5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ReproNim/containers/bids-ndmg--0.1.0/2021-03-19-fb5d9a64-8b1993e9/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-ndmg--0.1.0/2021-03-19-fb5d9a64-8b1993e9/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-ndmg--0.1.0

```bash
$ singularity pull shub://ReproNim/containers:bids-ndmg--0.1.0
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/ndmg:v0.1.0

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

