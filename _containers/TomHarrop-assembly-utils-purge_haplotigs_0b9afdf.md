---
id: 11941
name: "TomHarrop/assembly-utils"
branch: "master"
tag: "purge_haplotigs_0b9afdf"
commit: "ad516825fc3d222c63acdb393daf2a68bf6ce136"
version: "232155e0d28b07cc3db7d5dc18fd9644b060dcb36902c549918f47c87ddb46e5"
build_date: "2020-06-17T07:27:02.051Z"
size_mb: 284.3125
size: 298123264
sif: "https://datasets.datalad.org/shub/TomHarrop/assembly-utils/purge_haplotigs_0b9afdf/2020-06-17-ad516825-232155e0/232155e0d28b07cc3db7d5dc18fd9644b060dcb36902c549918f47c87ddb46e5.sif"
url: https://datasets.datalad.org/shub/TomHarrop/assembly-utils/purge_haplotigs_0b9afdf/2020-06-17-ad516825-232155e0/
recipe: https://datasets.datalad.org/shub/TomHarrop/assembly-utils/purge_haplotigs_0b9afdf/2020-06-17-ad516825-232155e0/Singularity
collection: TomHarrop/assembly-utils
---

# TomHarrop/assembly-utils:purge_haplotigs_0b9afdf

```bash
$ singularity pull shub://TomHarrop/assembly-utils:purge_haplotigs_0b9afdf
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10 

%help
    Container for purge_haplotigs
    https://bitbucket.org/mroachawri/purge_haplotigs

%labels
    VERSION "purge_haplotigs 0b9afdf"

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

    # dependencies
    apt-get update
    apt-get install -y \
        bedtools \
        build-essential \
        git \
        minimap2 \
        samtools \
        wget

    # install r separately to prevent X11 installation
    apt install --no-install-recommends -y \
        r-cran-ggplot2

    # install mummer
    # wget -O "mummer.tar.gz" \
    #     --no-check-certificate \
    #     https://github.com/mummer4/mummer/releases/download/v4.0.0beta2/mummer-4.0.0beta2.tar.gz
    # mkdir mummer-install
    # tar -zxf mummer.tar.gz \
    #     -C mummer-install \
    #     --strip-components 1
    # cd mummer-install || exit 1
    # ./configure && make && make install
    # cd .. || exit 1
    # rm -rf mummer.tar.gz mummer-install
    # ldconfig

    # clone
    git clone https://bitbucket.org/mroachawri/purge_haplotigs.git
    cd purge_haplotigs || exit 1
    git checkout -f 0b9afdf
    git submodule update --init --recursive

%environment
    export LC_ALL=C
    export PATH="${PATH}:/purge_haplotigs/bin"

%runscript
    exec /purge_haplotigs/bin/purge_haplotigs "$@"
```

## Collection

 - Name: [TomHarrop/assembly-utils](https://github.com/TomHarrop/assembly-utils)
 - License: None

