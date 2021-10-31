---
id: 11570
name: "TomHarrop/assembly-utils"
branch: "master"
tag: "agb_9c1b39c"
commit: "e2644127f4df84725ba3dfa9c28d278e4db55b40"
version: "8a6e4b5e5dabb98848486a1b9bbb2904ca12deea67ae762a6363a9354cb561f4"
build_date: "2019-11-13T05:19:55.305Z"
size_mb: 1181.85546875
size: 1239265280
sif: "https://datasets.datalad.org/shub/TomHarrop/assembly-utils/agb_9c1b39c/2019-11-13-e2644127-8a6e4b5e/8a6e4b5e5dabb98848486a1b9bbb2904ca12deea67ae762a6363a9354cb561f4.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/assembly-utils/agb_9c1b39c/2019-11-13-e2644127-8a6e4b5e/
recipe: https://datasets.datalad.org/shub/TomHarrop/assembly-utils/agb_9c1b39c/2019-11-13-e2644127-8a6e4b5e/Singularity
collection: TomHarrop/assembly-utils
---

# TomHarrop/assembly-utils:agb_9c1b39c

```bash
$ singularity pull shub://TomHarrop/assembly-utils:agb_9c1b39c
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: TomHarrop/assembly-utils:quast_5.0.2

%help
    Assembly Genome Browser (AGB)
    https://almiheenko.github.io/AGB

%labels
    MAINTAINER "Tom Harrop"
    VERSION "AGB 9c1b39c"

%post
    # faster apt downloads, will it break?
    export DEBIAN_FRONTEND=noninteractive
    (
        . /etc/os-release
        cat << _EOF_ > mirror.txt
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME} main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-updates main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-backports main restricted universe multiverse
deb mirror://mirrors.ubuntu.com/mirrors.txt ${UBUNTU_CODENAME}-security main restricted universe multiverse

_EOF_
        mv /etc/apt/sources.list /etc/apt/sources.list.bak
        cat mirror.txt /etc/apt/sources.list.bak > /etc/apt/sources.list
    )

    apt-get update
    apt-get install -y \
        cython3 \
        git \
        python3-gfapy \
        python3-networkx \
        python3-pip

    # python3 dependencies
    /usr/bin/pip3 install \
        git+git://github.com/networkx/networkx-metis@34398b7

    # agb
    /usr/bin/pip3 install \
        git+git://github.com/almiheenko/AGB.git@9c1b39c

%runscript
    exec /usr/local/bin/agb.py "$@"
```

## Collection

 - Name: [TomHarrop/assembly-utils](https://github.com/TomHarrop/assembly-utils)
 - License: None

