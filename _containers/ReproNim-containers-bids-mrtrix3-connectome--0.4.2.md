---
id: 9192
name: "ReproNim/containers"
branch: "master"
tag: "bids-mrtrix3-connectome--0.4.2"
commit: "03dd8e277b4a947ef20959fcc1c6bea5467a6470"
version: "fb8569b1e9005c944c50a8e0452e4835"
build_date: "2021-03-19T23:51:54.578Z"
size_mb: 17936
size: 7570726943
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-mrtrix3-connectome--0.4.2/2021-03-19-03dd8e27-fb8569b1/fb8569b1e9005c944c50a8e0452e4835.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ReproNim/containers/bids-mrtrix3-connectome--0.4.2/2021-03-19-03dd8e27-fb8569b1/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-mrtrix3-connectome--0.4.2/2021-03-19-03dd8e27-fb8569b1/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-mrtrix3-connectome--0.4.2

```bash
$ singularity pull shub://ReproNim/containers:bids-mrtrix3-connectome--0.4.2
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/mrtrix3_connectome:0.4.2

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

