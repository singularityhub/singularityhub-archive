---
id: 12438
name: "TomHarrop/align-utils"
branch: "master"
tag: "samblaster_0.1.24"
commit: "d5b3fe67cbe1d39829d521e76bc139ed8d4a3894"
version: "1159bb9ac9fb4c541d0486cb66790ef5c576c88b3623471394865db022a3d94e"
build_date: "2020-03-05T20:22:22.976Z"
size_mb: 114.94140625
size: 120524800
sif: "https://datasets.datalad.org/shub/TomHarrop/align-utils/samblaster_0.1.24/2020-03-05-d5b3fe67-1159bb9a/1159bb9ac9fb4c541d0486cb66790ef5c576c88b3623471394865db022a3d94e.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/align-utils/samblaster_0.1.24/2020-03-05-d5b3fe67-1159bb9a/
recipe: https://datasets.datalad.org/shub/TomHarrop/align-utils/samblaster_0.1.24/2020-03-05-d5b3fe67-1159bb9a/Singularity
collection: TomHarrop/align-utils
---

# TomHarrop/align-utils:samblaster_0.1.24

```bash
$ singularity pull shub://TomHarrop/align-utils:samblaster_0.1.24
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%help
    SAMBLASTER 0.1.24
    https://github.com/GregoryFaust/samblaster

%labels
    VERSION "SAMBLASTER 0.1.24"

%post
    # faster apt downloads
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C
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

    # apt dependencies
    apt-get update
    apt-get install -y \
        build-essential \
        wget

    # install samblaster
    wget \
        -O "samblaster.tar.gz" \
        https://github.com/GregoryFaust/samblaster/releases/download/v.0.1.24/samblaster-v.0.1.24.tar.gz
    mkdir /samblaster
    tar -zxf samblaster.tar.gz \
        -C /samblaster \
        --strip-components 1
    rm samblaster.tar.gz
    (
    cd /samblaster || exit 1
    make
    mv samblaster /usr/local/bin/
    )
    rm -r /samblaster

%runscript
    exec /usr/local/bin/samblaster "$@"
```

## Collection

 - Name: [TomHarrop/align-utils](https://github.com/TomHarrop/align-utils)
 - License: None

