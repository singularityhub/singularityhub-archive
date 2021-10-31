---
id: 9238
name: "ReproNim/containers"
branch: "master"
tag: "bids-fmriprep--1.4.0"
commit: "afafc7eb3a9ab52cc731012bab69d6f6638ae335"
version: "d091547aa4518e7475b97756be18a511"
build_date: "2019-08-26T16:14:48.002Z"
size_mb: 12142
size: 4780552223
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-fmriprep--1.4.0/2019-08-26-afafc7eb-d091547a/d091547aa4518e7475b97756be18a511.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ReproNim/containers/bids-fmriprep--1.4.0/2019-08-26-afafc7eb-d091547a/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-fmriprep--1.4.0/2019-08-26-afafc7eb-d091547a/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-fmriprep--1.4.0

```bash
$ singularity pull shub://ReproNim/containers:bids-fmriprep--1.4.0
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: poldracklab/fmriprep:1.4.0

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

