---
id: 12853
name: "TomHarrop/variant-utils"
branch: "master"
tag: "shapeit_v2.r904"
commit: "60cc6c4d5f20650560472d0628ed1a41507ff981"
version: "41e0cc9175832dfc4028a831f71441cc63fa4024b14ea6b03ef6a9bedc5cc010"
build_date: "2020-05-03T21:31:32.253Z"
size_mb: 57.9296875
size: 60743680
sif: "https://datasets.datalad.org/shub/TomHarrop/variant-utils/shapeit_v2.r904/2020-05-03-60cc6c4d-41e0cc91/41e0cc9175832dfc4028a831f71441cc63fa4024b14ea6b03ef6a9bedc5cc010.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/variant-utils/shapeit_v2.r904/2020-05-03-60cc6c4d-41e0cc91/
recipe: https://datasets.datalad.org/shub/TomHarrop/variant-utils/shapeit_v2.r904/2020-05-03-60cc6c4d-41e0cc91/Singularity
collection: TomHarrop/variant-utils
---

# TomHarrop/variant-utils:shapeit_v2.r904

```bash
$ singularity pull shub://TomHarrop/variant-utils:shapeit_v2.r904
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help
    Container for shapeit v2.r904

%labels
    VERSION "shapeit v2.r904"

%environment
    export PATH="${PATH}:/shapeit/bin"

%post
    # faster apt downloads
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
        wget

    wget \
        -O /shapeit.tar.gz \
        https://mathgen.stats.ox.ac.uk/genetics_software/shapeit/shapeit.v2.r904.glibcv2.12.linux.tar.gz
    mkdir /shapeit
    tar -zxf /shapeit.tar.gz \
        -C /shapeit \
        --strip-components 1        
    rm /shapeit.tar.gz
```

## Collection

 - Name: [TomHarrop/variant-utils](https://github.com/TomHarrop/variant-utils)
 - License: None

