---
id: 8695
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "bbmap_38.45"
commit: "97f58c68895c1646e59f007b21da4c9fbf417de0"
version: "c091a4a66dd7a7f7cb091ae6c039d556"
build_date: "2019-04-29T05:02:43.986Z"
size_mb: 360
size: 161673247
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/bbmap_38.45/2019-04-29-97f58c68-c091a4a6/c091a4a66dd7a7f7cb091ae6c039d556.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/bbmap_38.45/2019-04-29-97f58c68-c091a4a6/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/bbmap_38.45/2019-04-29-97f58c68-c091a4a6/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:bbmap_38.45

```bash
$ singularity pull shub://TomHarrop/singularity-containers:bbmap_38.45
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: TomHarrop/singularity-containers:samtools_1.9

%help
    Container for BBMap 38.45
    https://jgi.doe.gov/data-and-tools/bbtools/

%labels
    MAINTAINER "Tom Harrop"
    VERSION "BBMap 38.45"

%post
    apk add --update \
        gawk \
        openjdk8

    wget -O "bbmap.tar.gz" \
        "https://sourceforge.net/projects/bbmap/files/BBMap_38.45.tar.gz"
    mkdir bbmap-install
    tar -zxf bbmap.tar.gz \
        -C bbmap-install \
        --strip-components 1
    cp -r bbmap-install/resources/* /
    cp -r bbmap-install/* /usr/local/bin/
    rm -rf bbmap.tar.gz bbmap-install
```

## Collection

 - Name: [TomHarrop/singularity-containers](https://github.com/TomHarrop/singularity-containers)
 - License: None

