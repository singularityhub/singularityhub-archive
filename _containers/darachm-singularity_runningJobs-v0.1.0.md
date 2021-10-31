---
id: 8357
name: "darachm/singularity_runningJobs"
branch: "master"
tag: "v0.1.0"
commit: "d9099f6e04c944d088869b5ec17998aad128885f"
version: "bb855ba4bbf4abb72f0df0a3ff6072ee"
build_date: "2019-04-10T23:02:52.388Z"
size_mb: 481
size: 175124511
sif: "https://datasets.datalad.org/shub/darachm/singularity_runningJobs/v0.1.0/2019-04-10-d9099f6e-bb855ba4/bb855ba4bbf4abb72f0df0a3ff6072ee.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/darachm/singularity_runningJobs/v0.1.0/2019-04-10-d9099f6e-bb855ba4/
recipe: https://datasets.datalad.org/shub/darachm/singularity_runningJobs/v0.1.0/2019-04-10-d9099f6e-bb855ba4/Singularity
collection: darachm/singularity_runningJobs
---

# darachm/singularity_runningJobs:v0.1.0

```bash
$ singularity pull shub://darachm/singularity_runningJobs:v0.1.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
MAINTAINER darachm
DATE 190410

%help

    This is a base for general purpose stuff.
    
%post

    apt-get -y update
    apt-get -y upgrade
    apt-get -y install gzip git wget g++ gcc-4.8 curl 
    apt-get -y install gnupg2 software-properties-common

%test

    # ?
```

## Collection

 - Name: [darachm/singularity_runningJobs](https://github.com/darachm/singularity_runningJobs)
 - License: None

