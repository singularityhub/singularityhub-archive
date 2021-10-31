---
id: 8743
name: "VowpalWabbit/vowpal_wabbit"
branch: "master"
tag: "debian-unstable-amd64"
commit: "cfef09c53f0dd6941bf783a4b707e26b924e5806"
version: "1c518452891ffff7c0851b560bbe9c72"
build_date: "2019-05-01T22:22:20.552Z"
size_mb: 941
size: 328572959
sif: "https://datasets.datalad.org/shub/VowpalWabbit/vowpal_wabbit/debian-unstable-amd64/2019-05-01-cfef09c5-1c518452/1c518452891ffff7c0851b560bbe9c72.simg"
url: https://datasets.datalad.org/shub/VowpalWabbit/vowpal_wabbit/debian-unstable-amd64/2019-05-01-cfef09c5-1c518452/
recipe: https://datasets.datalad.org/shub/VowpalWabbit/vowpal_wabbit/debian-unstable-amd64/2019-05-01-cfef09c5-1c518452/Singularity
collection: JohnLangford/vowpal_wabbit
---

# VowpalWabbit/vowpal_wabbit:debian-unstable-amd64

```bash
$ singularity pull shub://VowpalWabbit/vowpal_wabbit:debian-unstable-amd64
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:unstable

# so if image is executed we just enter the environment
%runscript
    echo "Welcome to the Debian unstable VW devel env. (Architecture: amd64)"
    echo "Just cd to your vw sources or"
    echo " git clone git://github.com/JohnLangford/vowpal_wabbit"
    /bin/bash


%post
    echo "Configuring the environment"
    sed -e  's,^deb ,deb-src ,g' /etc/apt/sources.list > /etc/apt/sources.list.d/sources.list
    apt-get update
    apt-get -y install eatmydata
    # just useful little tools
    eatmydata apt-get -y install vim wget strace time ncdu gnupg curl procps netcat
    eatmydata apt-get -y build-dep vowpal-wabbit
    # new dependencies which didn't make it into a Debian release yet
    eatmydata apt-get -y install cmake
    # some external depends might have not been needed then
    eatmydata apt-get -y install markdown html2text rapidjson-dev libboost-python-dev  git
    chmod a+rX -R /etc/apt/sources.list.d
    rm -rf /var/lib/apt/lists/*
    apt-get clean
```

## Collection

 - Name: [VowpalWabbit/vowpal_wabbit](https://github.com/VowpalWabbit/vowpal_wabbit)
 - License: [Other](None)

