---
id: 8507
name: "ReproNim/containers"
branch: "master"
tag: "bids-freesurfer--6.0.1-5"
commit: "cd44927429b222f6a667d63c3b01e2ca7d2dfca0"
version: "cdda1256b8ae28043a187926319b80a4"
build_date: "2019-09-04T17:31:46.070Z"
size_mb: 6453
size: 2735378463
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-freesurfer--6.0.1-5/2019-09-04-cd449274-cdda1256/cdda1256b8ae28043a187926319b80a4.simg"
url: https://datasets.datalad.org/shub/ReproNim/containers/bids-freesurfer--6.0.1-5/2019-09-04-cd449274-cdda1256/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-freesurfer--6.0.1-5/2019-09-04-cd449274-cdda1256/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-freesurfer--6.0.1-5

```bash
$ singularity pull shub://ReproNim/containers:bids-freesurfer--6.0.1-5
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: bids/freesurfer:v6.0.1-5

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

