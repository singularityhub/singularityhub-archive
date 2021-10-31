---
id: 4860
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "plink_1.07"
commit: "4914df063caaddb810df74c10008c14109db077a"
version: "9af4df420948e1e5881dd991e0bb5ba8"
build_date: "2018-09-18T03:28:17.941Z"
size_mb: 120
size: 60915743
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/plink_1.07/2018-09-18-4914df06-9af4df42/9af4df420948e1e5881dd991e0bb5ba8.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/plink_1.07/2018-09-18-4914df06-9af4df42/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/plink_1.07/2018-09-18-4914df06-9af4df42/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:plink_1.07

```bash
$ singularity pull shub://TomHarrop/singularity-containers:plink_1.07
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%help

    plink 1.07
    http://zzz.bwh.harvard.edu/plink

%labels

    MAINTAINER "Tom Harrop"
    VERSION "plink 1.07"

%post

    # install plink
    apt-get update
    apt-get install -y \
        plink

    # run as plink
    ln -s /usr/bin/plink1 /usr/bin/plink

%runscript

    exec /usr/bin/plink "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

