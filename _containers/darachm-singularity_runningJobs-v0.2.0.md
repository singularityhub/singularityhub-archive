---
id: 8356
name: "darachm/singularity_runningJobs"
branch: "master"
tag: "v0.2.0"
commit: "1ef3344a65d7aa262fb9d0671ec10a40bec1e024"
version: "252ac35b95eeedf3cb3dd3a0cb3eeb74"
build_date: "2019-12-18T01:15:49.251Z"
size_mb: 1016
size: 427696159
sif: "https://datasets.datalad.org/shub/darachm/singularity_runningJobs/v0.2.0/2019-12-18-1ef3344a-252ac35b/252ac35b95eeedf3cb3dd3a0cb3eeb74.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/darachm/singularity_runningJobs/v0.2.0/2019-12-18-1ef3344a-252ac35b/
recipe: https://datasets.datalad.org/shub/darachm/singularity_runningJobs/v0.2.0/2019-12-18-1ef3344a-252ac35b/Singularity
collection: darachm/singularity_runningJobs
---

# darachm/singularity_runningJobs:v0.2.0

```bash
$ singularity pull shub://darachm/singularity_runningJobs:v0.2.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic-20190307

%labels
MAINTAINER darachm
DATE 190410

%help

    This is a base for running things, general stuff.
    It includes nextflow
    
%post

    apt-get -y update
    apt-get -y upgrade
# to install nextflow
    apt-get -y install default-jdk graphviz curl 
# to install singularity
    apt-get -y install singularity-container
# general stuff
    apt-get -y install gzip git wget g++ gcc-4.8 gawk
# for additional repos
    apt-get -y install gnupg2 software-properties-common 

    cd / 
    curl -s https://get.nextflow.io | bash
    chmod a+rx /nextflow

%test

    # ?
```

## Collection

 - Name: [darachm/singularity_runningJobs](https://github.com/darachm/singularity_runningJobs)
 - License: None

