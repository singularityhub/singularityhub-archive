---
id: 7300
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "bwa_0.7.17"
commit: "3c62cd682cafcac61867e6d8361bb413d67e6f37"
version: "eb49586488ed8fa5ba71da34f2fabc1a"
build_date: "2021-03-15T10:24:27.516Z"
size_mb: 101
size: 45821983
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/bwa_0.7.17/2021-03-15-3c62cd68-eb495864/eb49586488ed8fa5ba71da34f2fabc1a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/bwa_0.7.17/2021-03-15-3c62cd68-eb495864/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/bwa_0.7.17/2021-03-15-3c62cd68-eb495864/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:bwa_0.7.17

```bash
$ singularity pull shub://TomHarrop/singularity-containers:bwa_0.7.17
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.10

%help

    Container for BWA 0.7.17
    http://bio-bwa.sourceforge.net/

%labels

    VERSION "BWA 0.7.17"


%post

    # install dependencies via apt
    apt update
    apt install -y \
        bwa

%runscript

    exec /usr/bin/bwa "$@"
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

