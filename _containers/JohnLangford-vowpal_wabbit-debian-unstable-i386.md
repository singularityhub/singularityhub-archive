---
id: 3410
name: "JohnLangford/vowpal_wabbit"
branch: "master"
tag: "debian-unstable-i386"
commit: "ae732d5ceb5dc18c294d80582dd6e5e3774e0b03"
version: "54c5f58360521b182056244f6a4a034c"
build_date: "2018-07-05T12:20:14.255Z"
size_mb: 845
size: 304201759
sif: "https://datasets.datalad.org/shub/JohnLangford/vowpal_wabbit/debian-unstable-i386/2018-07-05-ae732d5c-54c5f583/54c5f58360521b182056244f6a4a034c.simg"
url: https://datasets.datalad.org/shub/JohnLangford/vowpal_wabbit/debian-unstable-i386/2018-07-05-ae732d5c-54c5f583/
recipe: https://datasets.datalad.org/shub/JohnLangford/vowpal_wabbit/debian-unstable-i386/2018-07-05-ae732d5c-54c5f583/Singularity
collection: JohnLangford/vowpal_wabbit
---

# JohnLangford/vowpal_wabbit:debian-unstable-i386

```bash
$ singularity pull shub://JohnLangford/vowpal_wabbit:debian-unstable-i386
```

## Singularity Recipe

```singularity
BootStrap: docker
From: i386/debian:unstable

# so if image is executed we just enter the environment
%runscript
    echo "Welcome to the Debian unstable VW devel env. (Architecture: i386)"
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

