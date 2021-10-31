---
id: 8872
name: "ReproNim/containers"
branch: "master"
tag: "bids-dparsf--4.3.12"
commit: "697f419c659db6088f9fb810afdf14b3cf0d3ac2"
version: "3f470abe52c945441ef853ba5a09d04c"
build_date: "2021-03-19T23:51:54.506Z"
size_mb: 3337
size: 1521623071
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-dparsf--4.3.12/2021-03-19-697f419c-3f470abe/3f470abe52c945441ef853ba5a09d04c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ReproNim/containers/bids-dparsf--4.3.12/2021-03-19-697f419c-3f470abe/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-dparsf--4.3.12/2021-03-19-697f419c-3f470abe/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-dparsf--4.3.12

```bash
$ singularity pull shub://ReproNim/containers:bids-dparsf--4.3.12
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/dparsf:v4.3.12

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

