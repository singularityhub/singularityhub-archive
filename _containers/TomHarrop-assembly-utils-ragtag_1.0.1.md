---
id: 13997
name: "TomHarrop/assembly-utils"
branch: "master"
tag: "ragtag_1.0.1"
commit: "09a7062d92df99c1b9c46edb32d685d66a8dc1fc"
version: "03f8d321e1faaf71469f6297baf4405420385049cbbe4eb5c0ddebc1d4da1f9e"
build_date: "2020-10-08T03:15:29.297Z"
size_mb: 200.4453125
size: 210182144
sif: "https://datasets.datalad.org/shub/TomHarrop/assembly-utils/ragtag_1.0.1/2020-10-08-09a7062d-03f8d321/03f8d321e1faaf71469f6297baf4405420385049cbbe4eb5c0ddebc1d4da1f9e.sif"
url: https://datasets.datalad.org/shub/TomHarrop/assembly-utils/ragtag_1.0.1/2020-10-08-09a7062d-03f8d321/
recipe: https://datasets.datalad.org/shub/TomHarrop/assembly-utils/ragtag_1.0.1/2020-10-08-09a7062d-03f8d321/Singularity
collection: TomHarrop/assembly-utils
---

# TomHarrop/assembly-utils:ragtag_1.0.1

```bash
$ singularity pull shub://TomHarrop/assembly-utils:ragtag_1.0.1
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: TomHarrop/align-utils:minimap2_2.17r941

# Bootstrap: localimage
# From: /home/tom/Containers/align-utils/img/minimap2_2.17r941.sif

%help
    ragtag 1.0.1
    https://github.com/malonge/RagTag
    
%labels
    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "ragtag 1.0.1"

%post
    apt-get update
    apt-get install -y \
        git \
        python3 \
        python3-pip

    pip3 install git+git://github.com/malonge/RagTag@v1.0.1

%runscript
    exec /usr/local/bin/ragtag.py "$@"
```

## Collection

 - Name: [TomHarrop/assembly-utils](https://github.com/TomHarrop/assembly-utils)
 - License: None

