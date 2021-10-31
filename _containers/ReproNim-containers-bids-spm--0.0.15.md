---
id: 8884
name: "ReproNim/containers"
branch: "master"
tag: "bids-spm--0.0.15"
commit: "697f419c659db6088f9fb810afdf14b3cf0d3ac2"
version: "a9d074bf4b8e0ddc2e550449a41b881e"
build_date: "2019-05-08T15:10:10.257Z"
size_mb: 4791
size: 2063417375
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-spm--0.0.15/2019-05-08-697f419c-a9d074bf/a9d074bf4b8e0ddc2e550449a41b881e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ReproNim/containers/bids-spm--0.0.15/2019-05-08-697f419c-a9d074bf/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-spm--0.0.15/2019-05-08-697f419c-a9d074bf/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-spm--0.0.15

```bash
$ singularity pull shub://ReproNim/containers:bids-spm--0.0.15
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/spm:v0.0.15

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

