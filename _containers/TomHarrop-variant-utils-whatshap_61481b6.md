---
id: 12870
name: "TomHarrop/variant-utils"
branch: "master"
tag: "whatshap_61481b6"
commit: "ec060a55081b03f5a09f13245432f3d9a20ad1f9"
version: "d6eb0d221e86b06392b77f33d00dde89d1b601d2771b8dd0d44ce27539965b8a"
build_date: "2020-05-04T21:03:19.406Z"
size_mb: 467.80859375
size: 490532864
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/whatshap_61481b6/2020-05-04-ec060a55-d6eb0d22/d6eb0d221e86b06392b77f33d00dde89d1b601d2771b8dd0d44ce27539965b8a.sif"
url: https://datasets.datalad.org/shub/TomHarrop/variant-utils/whatshap_61481b6/2020-05-04-ec060a55-d6eb0d22/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/whatshap_61481b6/2020-05-04-ec060a55-d6eb0d22/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:whatshap_61481b6

```bash
$ singularity pull shub://TomHarrop/variant-utils:whatshap_61481b6
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.8.2-buster

%help
    Container for whatshap 61481b6

%labels
    VERSION "whatshap 61481b6"

%post
    apt-get update
    apt-get install -y \
        build-essential \
        libcrypto++-dev

    # /usr/local/bin/pip3 install whatshap==0.19

    /usr/local/bin/pip3 install \
    	git+https://bitbucket.org/whatshap/whatshap.git@61481b6

%runscript
    exec /usr/local/bin/whatshap "$@"
```

## Collection

 - Name: [TomHarrop/variant-utils](https://github.com/TomHarrop/variant-utils)
 - License: None

