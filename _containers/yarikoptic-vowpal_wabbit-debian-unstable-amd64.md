---
id: 1872
name: "yarikoptic/vowpal_wabbit"
branch: "master"
tag: "debian-unstable-amd64"
commit: "5dfd8a1f860b981a721d4e8026840d8ceaad4877"
version: "466026f63528556e94fef6818c733c25"
build_date: "2018-07-29T13:43:58.672Z"
size_mb: 851
size: 299819039
sif: "https://datasets.datalad.org/shub/yarikoptic/vowpal_wabbit/debian-unstable-amd64/2018-07-29-5dfd8a1f-466026f6/466026f63528556e94fef6818c733c25.simg"
url: https://datasets.datalad.org/shub/yarikoptic/vowpal_wabbit/debian-unstable-amd64/2018-07-29-5dfd8a1f-466026f6/
recipe: https://datasets.datalad.org/shub/yarikoptic/vowpal_wabbit/debian-unstable-amd64/2018-07-29-5dfd8a1f-466026f6/Singularity
collection: yarikoptic/vowpal_wabbit
---

# yarikoptic/vowpal_wabbit:debian-unstable-amd64

```bash
$ singularity pull shub://yarikoptic/vowpal_wabbit:debian-unstable-amd64
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

 - Name: [yarikoptic/vowpal_wabbit](https://github.com/yarikoptic/vowpal_wabbit)
 - License: [Other](None)

