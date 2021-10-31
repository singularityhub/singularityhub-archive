---
id: 9545
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "bbmap_38.50b"
commit: "09d882ad834d388c91f282bafaffbabb875204ad"
version: "0b928c58d46bf1e558b4020708896240"
build_date: "2020-02-17T02:57:05.062Z"
size_mb: 360
size: 161767455
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/bbmap_38.50b/2020-02-17-09d882ad-0b928c58/0b928c58d46bf1e558b4020708896240.simg"
url: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/bbmap_38.50b/2020-02-17-09d882ad-0b928c58/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/bbmap_38.50b/2020-02-17-09d882ad-0b928c58/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:bbmap_38.50b

```bash
$ singularity pull shub://TomHarrop/singularity-containers:bbmap_38.50b
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: TomHarrop/singularity-containers:samtools_1.9

%help
    Container for BBMap 38.50b
    https://jgi.doe.gov/data-and-tools/bbtools/

%labels
    MAINTAINER "Tom Harrop"
    VERSION "BBMap 38.50b"

%post
    apk add --update \
        gawk \
        openjdk8

    wget -O "bbmap.tar.gz" \
        "https://sourceforge.net/projects/bbmap/files/BBMap_38.50b.tar.gz"
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

