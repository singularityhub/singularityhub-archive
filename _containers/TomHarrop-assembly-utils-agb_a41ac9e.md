---
id: 11944
name: "TomHarrop/assembly-utils"
branch: "master"
tag: "agb_a41ac9e"
commit: "5b93de9aed49e774b2c74c05717b06a4aed40f26"
version: "bef51300ada63f4fc887cd27145a646378f19151d6c729141823c6fb5304c24e"
build_date: "2020-01-06T23:27:32.600Z"
size_mb: 1181.85546875
size: 1239265280
sif: "https://datasets.datalad.org/shub/TomHarrop/assembly-utils/agb_a41ac9e/2020-01-06-5b93de9a-bef51300/bef51300ada63f4fc887cd27145a646378f19151d6c729141823c6fb5304c24e.sif"
url: https://datasets.datalad.org/shub/TomHarrop/assembly-utils/agb_a41ac9e/2020-01-06-5b93de9a-bef51300/
recipe: https://datasets.datalad.org/shub/TomHarrop/assembly-utils/agb_a41ac9e/2020-01-06-5b93de9a-bef51300/Singularity
collection: TomHarrop/assembly-utils
---

# TomHarrop/assembly-utils:agb_a41ac9e

```bash
$ singularity pull shub://TomHarrop/assembly-utils:agb_a41ac9e
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
    VERSION "AGB a41ac9e"

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
         git+git://github.com/almiheenko/AGB.git@a41ac9e

%runscript
    exec /usr/local/bin/agb.py "$@"
```

## Collection

 - Name: [TomHarrop/assembly-utils](https://github.com/TomHarrop/assembly-utils)
 - License: None

