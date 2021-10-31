---
id: 9147
name: "ReproNim/containers"
branch: "master"
tag: "repronim-simple-workflow--1.1.0"
commit: "d4108e95f8ea4621bd491e07e5a9505059576d53"
version: "14888c9ed120ad0244f5e15ab635bcc2"
build_date: "2021-03-19T23:51:52.313Z"
size_mb: 2961
size: 1727082527
sif: "https://datasets.datalad.org/shub/ReproNim/containers/repronim-simple-workflow--1.1.0/2021-03-19-d4108e95-14888c9e/14888c9ed120ad0244f5e15ab635bcc2.simg"
url: https://datasets.datalad.org/shub/ReproNim/containers/repronim-simple-workflow--1.1.0/2021-03-19-d4108e95-14888c9e/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/repronim-simple-workflow--1.1.0/2021-03-19-d4108e95-14888c9e/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:repronim-simple-workflow--1.1.0

```bash
$ singularity pull shub://ReproNim/containers:repronim-simple-workflow--1.1.0
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: repronim/simple_workflow:1.1.0

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

