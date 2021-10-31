---
id: 14949
name: "TomHarrop/variant-utils"
branch: "master"
tag: "whatshap_491ec8e"
commit: "44309438f43c60bc92ddc5a0e51bc717486cb628"
version: "95bbf81f84771c4e5905c893ab81d58e467fe6f5a9d2377a7d00b47418188f23"
build_date: "2020-12-02T22:04:41.810Z"
size_mb: 442.25
size: 463732736
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/whatshap_491ec8e/2020-12-02-44309438-95bbf81f/95bbf81f84771c4e5905c893ab81d58e467fe6f5a9d2377a7d00b47418188f23.sif"
url: https://datasets.datalad.org/shub/TomHarrop/variant-utils/whatshap_491ec8e/2020-12-02-44309438-95bbf81f/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/whatshap_491ec8e/2020-12-02-44309438-95bbf81f/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:whatshap_491ec8e

```bash
$ singularity pull shub://TomHarrop/variant-utils:whatshap_491ec8e
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.8.6-buster

%help
    Container for whatshap 491ec8e

%labels
    VERSION "whatshap 491ec8e"

%post
    apt-get update
    apt-get install -y \
        build-essential \
        libcrypto++-dev

    # /usr/local/bin/pip3 install whatshap==0.19

    /usr/local/bin/pip3 install \
    	git+https://github.com/whatshap/whatshap@491ec8e

%runscript
    exec /usr/local/bin/whatshap "$@"
```

## Collection

 - Name: [TomHarrop/variant-utils](https://github.com/TomHarrop/variant-utils)
 - License: None

