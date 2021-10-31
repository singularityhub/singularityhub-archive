---
id: 11673
name: "TomHarrop/seq-utils"
branch: "master"
tag: "pysam_0.15.3"
commit: "eb6e9de51b8f2178675729a29fc96201cf4edb17"
version: "973c3acc1e56e609ac9b594151ddff1a3591b8794a1382221bc835289e66242f"
build_date: "2019-12-16T20:45:47.875Z"
size_mb: 352.53125
size: 369655808
sif: "https://datasets.datalad.org/shub/TomHarrop/seq-utils/pysam_0.15.3/2019-12-16-eb6e9de5-973c3acc/973c3acc1e56e609ac9b594151ddff1a3591b8794a1382221bc835289e66242f.sif"
url: https://datasets.datalad.org/shub/TomHarrop/seq-utils/pysam_0.15.3/2019-12-16-eb6e9de5-973c3acc/
recipe: https://datasets.datalad.org/shub/TomHarrop/seq-utils/pysam_0.15.3/2019-12-16-eb6e9de5-973c3acc/Singularity
collection: TomHarrop/seq-utils
---

# TomHarrop/seq-utils:pysam_0.15.3

```bash
$ singularity pull shub://TomHarrop/seq-utils:pysam_0.15.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.7.5-buster

%help
    pysam 0.15.3
    https://pysam.readthedocs.io

%labels
    MAINTAINER "Tom Harrop"
    VERSION "pysam 0.15.3"

%post
    # install dependencies
    apt-get update
    apt-get install -y \
        build-essential \
        libcrypto++-dev

    # install porechop 
    /usr/local/bin/pip3 install \
        pysam==0.15.3

%runscript
    exec /usr/local/bin/python3 "$@"
```

## Collection

 - Name: [TomHarrop/seq-utils](https://github.com/TomHarrop/seq-utils)
 - License: None

