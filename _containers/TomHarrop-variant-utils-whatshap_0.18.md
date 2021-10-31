---
id: 11721
name: "TomHarrop/variant-utils"
branch: "master"
tag: "whatshap_0.18"
commit: "bef2084677bdf39dba2d1358ad8e750bc1d5571b"
version: "d8c4e886ff1c904ad2c0b487d5e89c7eb1d08871d539dbe11d6b8f39dd71538b"
build_date: "2020-05-04T20:48:25.018Z"
size_mb: 403.07421875
size: 422653952
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/whatshap_0.18/2020-05-04-bef20846-d8c4e886/d8c4e886ff1c904ad2c0b487d5e89c7eb1d08871d539dbe11d6b8f39dd71538b.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/variant-utils/whatshap_0.18/2020-05-04-bef20846-d8c4e886/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/whatshap_0.18/2020-05-04-bef20846-d8c4e886/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:whatshap_0.18

```bash
$ singularity pull shub://TomHarrop/variant-utils:whatshap_0.18
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.7.5-buster

%help
    Container for whatshap 0.18

%labels
    VERSION "whatshap 0.18"

%post
    apt-get update
    apt-get install -y \
        build-essential \
        libcrypto++-dev

    /usr/local/bin/pip3 install whatshap==0.18

%runscript
    exec /usr/local/bin/whatshap "$@"
```

## Collection

 - Name: [TomHarrop/variant-utils](https://github.com/TomHarrop/variant-utils)
 - License: None

