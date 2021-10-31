---
id: 8710
name: "ReproNim/containers"
branch: "master"
tag: "bids-mrtrix3-connectome--0.4.1"
commit: "dc6dedfd480a31550fc8907731af7eac11335ca6"
version: "4f140f2e916a265572669554817c090f"
build_date: "2019-05-03T16:30:47.534Z"
size_mb: 17936
size: 7570726943
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-mrtrix3-connectome--0.4.1/2019-05-03-dc6dedfd-4f140f2e/4f140f2e916a265572669554817c090f.simg"
url: https://datasets.datalad.org/shub/ReproNim/containers/bids-mrtrix3-connectome--0.4.1/2019-05-03-dc6dedfd-4f140f2e/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-mrtrix3-connectome--0.4.1/2019-05-03-dc6dedfd-4f140f2e/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-mrtrix3-connectome--0.4.1

```bash
$ singularity pull shub://ReproNim/containers:bids-mrtrix3-connectome--0.4.1
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/mrtrix3_connectome:0.4.1

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

