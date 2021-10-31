---
id: 4954
name: "MarissaLL/singularity-containers"
branch: "master"
tag: "bbmap_37.92"
commit: "5e9f442dc50fb9ad8be139d721ce33a0fe9b2fa7"
version: "fa973c37883055c243c5e37f82f68f4d"
build_date: "2020-12-03T09:29:30.388Z"
size_mb: 637
size: 295137311
sif: "https://datasets.datalad.org/shub/MarissaLL/singularity-containers/bbmap_37.92/2020-12-03-5e9f442d-fa973c37/fa973c37883055c243c5e37f82f68f4d.simg"
url: https://datasets.datalad.org/shub/MarissaLL/singularity-containers/bbmap_37.92/2020-12-03-5e9f442d-fa973c37/
recipe: https://datasets.datalad.org/shub/MarissaLL/singularity-containers/bbmap_37.92/2020-12-03-5e9f442d-fa973c37/Singularity
collection: MarissaLL/singularity-containers
---

# MarissaLL/singularity-containers:bbmap_37.92

```bash
$ singularity pull shub://MarissaLL/singularity-containers:bbmap_37.92
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/
Include: default-jre wget

%labels

    MAINTAINER "Marissa Le Lec"
    VERSION "BBMap 37.92"

%post

    wget -O "bbmap.tar.gz" \
        "https://sourceforge.net/projects/bbmap/files/BBMap_37.92.tar.gz/download"
    mkdir bbmap-install
    tar -zxf bbmap.tar.gz \
        -C bbmap-install \
        --strip-components 1
    cp -r bbmap-install/resources/* /
    cp -r bbmap-install/* /usr/local/bin/
    rm -rf bbmap.tar.gz bbmap-install
```

## Collection

 - Name: [MarissaLL/singularity-containers](https://github.com/MarissaLL/singularity-containers)
 - License: None

