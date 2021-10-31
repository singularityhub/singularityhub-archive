---
id: 2814
name: "TomHarrop/singularity-containers"
branch: "master"
tag: "bbmap_38.00"
commit: "5e102f3a75454795ffbb73c487c38430aa0caca5"
version: "a773baa8cc025cc5b5cbee20e507fef7"
build_date: "2021-03-15T21:25:56.436Z"
size_mb: 637
size: 295428127
sif: "https://datasets.datalad.org/shub/TomHarrop/singularity-containers/bbmap_38.00/2021-03-15-5e102f3a-a773baa8/a773baa8cc025cc5b5cbee20e507fef7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/singularity-containers/bbmap_38.00/2021-03-15-5e102f3a-a773baa8/
recipe: https://datasets.datalad.org/shub/TomHarrop/singularity-containers/bbmap_38.00/2021-03-15-5e102f3a-a773baa8/Singularity
collection: TomHarrop/singularity-containers
---

# TomHarrop/singularity-containers:bbmap_38.00

```bash
$ singularity pull shub://TomHarrop/singularity-containers:bbmap_38.00
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: default-jre wget

%help

    Container for BBMap 38.00
    https://jgi.doe.gov/data-and-tools/bbtools/

%labels

    MAINTAINER "Tom Harrop"
    VERSION "BBMap 38.00"

%post

    wget -O "bbmap.tar.gz" \
        "https://sourceforge.net/projects/bbmap/files/BBMap_38.00.tar.gz"
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

