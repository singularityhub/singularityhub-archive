---
id: 8874
name: "ReproNim/containers"
branch: "master"
tag: "bids-fibredensityandcrosssection--0.0.1"
commit: "2b6f83c739d62636d186ac4dabefde54026c8f81"
version: "32e70abdb50f6946e2b00c631a098ca5"
build_date: "2021-03-19T23:51:52.390Z"
size_mb: 1445
size: 572895263
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-fibredensityandcrosssection--0.0.1/2021-03-19-2b6f83c7-32e70abd/32e70abdb50f6946e2b00c631a098ca5.simg"
url: https://datasets.datalad.org/shub/ReproNim/containers/bids-fibredensityandcrosssection--0.0.1/2021-03-19-2b6f83c7-32e70abd/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-fibredensityandcrosssection--0.0.1/2021-03-19-2b6f83c7-32e70abd/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-fibredensityandcrosssection--0.0.1

```bash
$ singularity pull shub://ReproNim/containers:bids-fibredensityandcrosssection--0.0.1
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/fibredensityandcrosssection:v0.0.1

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

