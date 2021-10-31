---
id: 2077
name: "JohnLangford/vowpal_wabbit"
branch: "master"
tag: "debian-unstable-amd64"
commit: "5dfd8a1f860b981a721d4e8026840d8ceaad4877"
version: "b4c0c71982a0d0cc72640a2686dc2a10"
build_date: "2018-07-03T21:25:27.017Z"
size_mb: 844
size: 297168927
sif: "https://datasets.datalad.org/shub/JohnLangford/vowpal_wabbit/debian-unstable-amd64/2018-07-03-5dfd8a1f-b4c0c719/b4c0c71982a0d0cc72640a2686dc2a10.simg"
url: https://datasets.datalad.org/shub/JohnLangford/vowpal_wabbit/debian-unstable-amd64/2018-07-03-5dfd8a1f-b4c0c719/
recipe: https://datasets.datalad.org/shub/JohnLangford/vowpal_wabbit/debian-unstable-amd64/2018-07-03-5dfd8a1f-b4c0c719/Singularity
collection: JohnLangford/vowpal_wabbit
---

# JohnLangford/vowpal_wabbit:debian-unstable-amd64

```bash
$ singularity pull shub://JohnLangford/vowpal_wabbit:debian-unstable-amd64
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
    # some external depends might have not been needed then
    eatmydata apt-get -y install markdown html2text rapidjson-dev libboost-python-dev  git
    chmod a+rX -R /etc/apt/sources.list.d
    rm -rf /var/lib/apt/lists/*
    apt-get clean
```

## Collection

 - Name: [JohnLangford/vowpal_wabbit](https://github.com/JohnLangford/vowpal_wabbit)
 - License: [Other](None)

