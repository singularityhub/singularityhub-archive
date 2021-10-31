---
id: 8513
name: "ReproNim/containers"
branch: "master"
tag: "bids-fmriprep--1.3.2"
commit: "454cda36e79c544a44d7b3b7b24e29eba22819bb"
version: "8fdcd10913a9c7109f28e0065d84fdce"
build_date: "2019-07-25T17:32:06.607Z"
size_mb: 12187
size: 4811120671
sif: "https://datasets.datalad.org/shub/ReproNim/containers/bids-fmriprep--1.3.2/2019-07-25-454cda36-8fdcd109/8fdcd10913a9c7109f28e0065d84fdce.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ReproNim/containers/bids-fmriprep--1.3.2/2019-07-25-454cda36-8fdcd109/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/bids-fmriprep--1.3.2/2019-07-25-454cda36-8fdcd109/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:bids-fmriprep--1.3.2

```bash
$ singularity pull shub://ReproNim/containers:bids-fmriprep--1.3.2
```

## Singularity Recipe

```singularity
#
# Automagically prepared for ReproNim/containers distribution.
# See http://github.com/ReproNim/containers for more info
#
Bootstrap: docker
From: poldracklab/fmriprep:1.3.2

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

