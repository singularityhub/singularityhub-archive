---
id: 8885
name: "ReproNim/containers"
branch: "master"
tag: "bids-tracula--6.0.0.beta-0"
commit: "697f419c659db6088f9fb810afdf14b3cf0d3ac2"
version: "0e42ad98d8b068b9810344713e652fc9"
build_date: "2021-03-19T23:51:54.434Z"
size_mb: 7568
size: 3461136415
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-tracula--6.0.0.beta-0/2021-03-19-697f419c-0e42ad98/0e42ad98d8b068b9810344713e652fc9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ReproNim/containers/bids-tracula--6.0.0.beta-0/2021-03-19-697f419c-0e42ad98/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-tracula--6.0.0.beta-0/2021-03-19-697f419c-0e42ad98/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-tracula--6.0.0.beta-0

```bash
$ singularity pull shub://ReproNim/containers:bids-tracula--6.0.0.beta-0
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/tracula:v6.0.0.beta-0

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

