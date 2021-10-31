---
id: 11674
name: "TomHarrop/assemblers"
branch: "master"
tag: "canu_1.9"
commit: "b40799da63462ba5d76fcc3cfe158053e81af736"
version: "21ef05edd3a0996a29721ba1e9c9c0eef16ececbbac58976112c7a6c44a76b57"
build_date: "2019-11-21T00:19:31.675Z"
size_mb: 341.140625
size: 357711872
sif: "https://datasets.datalad.org/shub/TomHarrop/assemblers/canu_1.9/2019-11-21-b40799da-21ef05ed/21ef05edd3a0996a29721ba1e9c9c0eef16ececbbac58976112c7a6c44a76b57.sif"
url: https://datasets.datalad.org/shub/TomHarrop/assemblers/canu_1.9/2019-11-21-b40799da-21ef05ed/
recipe: https://datasets.datalad.org/shub/TomHarrop/assemblers/canu_1.9/2019-11-21-b40799da-21ef05ed/Singularity
collection: TomHarrop/assemblers
---

# TomHarrop/assemblers:canu_1.9

```bash
$ singularity pull shub://TomHarrop/assemblers:canu_1.9
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.10 

%help

    Container for Canu 1.9
    https://github.com/marbl/canu

%labels

    VERSION "Canu 1.9"

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

    # dependencies
    apt-get update
    apt-get install -y \
        build-essential \
        language-pack-en \
        openjdk-8-jre-headless \
        perl \
        wget
    apt-get install -y \
        --no-install-recommends \
        gnuplot

    # install Canu
    wget -O "canu.tar.gz" \
        --no-check-certificate \
        https://github.com/marbl/canu/archive/v1.9.tar.gz
    mkdir canu
    tar -zxf canu.tar.gz \
        -C canu \
        --strip-components 1
    cd canu/src || exit 1
    make
    cd ../.. || exit 1
    rm -rf canu.tar.gz

%environment

    export PATH="${PATH}:/canu/Linux-amd64/bin"

%runscript

    exec /canu/Linux-amd64/bin/canu "$@"
```

## Collection

 - Name: [TomHarrop/assemblers](https://github.com/TomHarrop/assemblers)
 - License: None

