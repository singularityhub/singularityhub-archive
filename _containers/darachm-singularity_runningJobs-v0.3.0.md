---
id: 9413
name: "darachm/singularity_runningJobs"
branch: "master"
tag: "v0.3.0"
commit: "d69ee41efed4383e296bd84d46d1ebe899686247"
version: "82e66fd1b59db835ae496fcd21077ee0"
build_date: "2019-12-18T01:15:49.502Z"
size_mb: 1096
size: 531288095
sif: "https://datasets.datalad.org/shub/darachm/singularity_runningJobs/v0.3.0/2019-12-18-d69ee41e-82e66fd1/82e66fd1b59db835ae496fcd21077ee0.simg"
url: https://datasets.datalad.org/shub/darachm/singularity_runningJobs/v0.3.0/2019-12-18-d69ee41e-82e66fd1/
recipe: https://datasets.datalad.org/shub/darachm/singularity_runningJobs/v0.3.0/2019-12-18-d69ee41e-82e66fd1/Singularity
collection: darachm/singularity_runningJobs
---

# darachm/singularity_runningJobs:v0.3.0

```bash
$ singularity pull shub://darachm/singularity_runningJobs:v0.3.0
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
# perl ! Some times you just need a one-liner
    apt-get -y install perl

    cd / 
    curl -s https://get.nextflow.io | bash
    chmod a+rx /nextflow

%test

    # ?
```

## Collection

 - Name: [darachm/singularity_runningJobs](https://github.com/darachm/singularity_runningJobs)
 - License: None

