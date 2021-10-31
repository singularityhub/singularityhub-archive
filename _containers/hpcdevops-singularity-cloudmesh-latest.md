---
id: 3725
name: "hpcdevops/singularity-cloudmesh"
branch: "master"
tag: "latest"
commit: "8381fb1adc5d606252c5ae862d194580ab2039e1"
version: "cbb87316bfbd1d1214659ea7e3690a60"
build_date: "2018-07-28T02:46:38.750Z"
size_mb: 754
size: 273322015
sif: "https://datasets.datalad.org/shub/hpcdevops/singularity-cloudmesh/latest/2018-07-28-8381fb1a-cbb87316/cbb87316bfbd1d1214659ea7e3690a60.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/hpcdevops/singularity-cloudmesh/latest/2018-07-28-8381fb1a-cbb87316/
recipe: https://datasets.datalad.org/shub/hpcdevops/singularity-cloudmesh/latest/2018-07-28-8381fb1a-cbb87316/Singularity
collection: hpcdevops/singularity-cloudmesh
---

# hpcdevops/singularity-cloudmesh:latest

```bash
$ singularity pull shub://hpcdevops/singularity-cloudmesh:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: python:2.7.14

%labels
    SDSC_IMG_MAINTAINER hpcdevops
    SDSC_IMG_NAME cloudmesh.client
    SDSC_IMG_DESC Python 2.7.14 Base Image w/ Cloudmesh CMD5 Client for Comet
    SDSC_IMG_VENDOR SDSC HPC Group

%runscript
    exec /usr/local/bin/cms "$@"

%test
    cms version

%post

    # Add cloudmesh tool...
    pip install cloudmesh.comet

    # build info
    echo "Timestamp:" `date --utc` | tee /image-build-info.txt
```

## Collection

 - Name: [hpcdevops/singularity-cloudmesh](https://github.com/hpcdevops/singularity-cloudmesh)
 - License: [Other](None)

