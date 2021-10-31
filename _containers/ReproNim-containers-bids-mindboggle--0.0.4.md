---
id: 8877
name: "ReproNim/containers"
branch: "master"
tag: "bids-mindboggle--0.0.4"
commit: "2280a99a1873ad340b8700dc98fa0f9206cb67aa"
version: "056a8fe5c67822243c78aa40a8127b01"
build_date: "2021-03-19T23:51:53.414Z"
size_mb: 6112
size: 2017742879
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-mindboggle--0.0.4/2021-03-19-2280a99a-056a8fe5/056a8fe5c67822243c78aa40a8127b01.simg"
url: https://datasets.datalad.org/shub/ReproNim/containers/bids-mindboggle--0.0.4/2021-03-19-2280a99a-056a8fe5/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-mindboggle--0.0.4/2021-03-19-2280a99a-056a8fe5/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-mindboggle--0.0.4

```bash
$ singularity pull shub://ReproNim/containers:bids-mindboggle--0.0.4
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/mindboggle:0.0.4

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

