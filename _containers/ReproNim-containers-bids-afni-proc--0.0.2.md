---
id: 8866
name: "ReproNim/containers"
branch: "master"
tag: "bids-afni-proc--0.0.2"
commit: "697f419c659db6088f9fb810afdf14b3cf0d3ac2"
version: "d4f8b69a4154ff0185912bfddae066bf"
build_date: "2021-03-19T23:51:53.119Z"
size_mb: 3440
size: 1492447263
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-afni-proc--0.0.2/2021-03-19-697f419c-d4f8b69a/d4f8b69a4154ff0185912bfddae066bf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ReproNim/containers/bids-afni-proc--0.0.2/2021-03-19-697f419c-d4f8b69a/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-afni-proc--0.0.2/2021-03-19-697f419c-d4f8b69a/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-afni-proc--0.0.2

```bash
$ singularity pull shub://ReproNim/containers:bids-afni-proc--0.0.2
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/afni_proc:v0.0.2

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

