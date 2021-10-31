---
id: 8875
name: "ReproNim/containers"
branch: "master"
tag: "bids-hcppipelines--3.17.0-18"
commit: "2b6f83c739d62636d186ac4dabefde54026c8f81"
version: "0cd37732b4be4a152fb5727df6836847"
build_date: "2021-03-19T23:51:52.974Z"
size_mb: 8762
size: 4150747167
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-hcppipelines--3.17.0-18/2021-03-19-2b6f83c7-0cd37732/0cd37732b4be4a152fb5727df6836847.simg"
url: https://datasets.datalad.org/shub/ReproNim/containers/bids-hcppipelines--3.17.0-18/2021-03-19-2b6f83c7-0cd37732/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-hcppipelines--3.17.0-18/2021-03-19-2b6f83c7-0cd37732/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-hcppipelines--3.17.0-18

```bash
$ singularity pull shub://ReproNim/containers:bids-hcppipelines--3.17.0-18
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/hcppipelines:v3.17.0-18

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

