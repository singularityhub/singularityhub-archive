---
id: 3528
name: "mcw-rcc/rstudio"
branch: "master"
tag: "1.1.442"
commit: "281fa24b5227468f9b163b9b982ec538a5d58c03"
version: "c8c5910d45d7e9b59c397f8be98e4268"
build_date: "2019-11-12T09:55:42.021Z"
size_mb: 2587
size: 966656031
sif: "https://datasets.datalad.org/shub/mcw-rcc/rstudio/1.1.442/2019-11-12-281fa24b-c8c5910d/c8c5910d45d7e9b59c397f8be98e4268.simg"
url: https://datasets.datalad.org/shub/mcw-rcc/rstudio/1.1.442/2019-11-12-281fa24b-c8c5910d/
recipe: https://datasets.datalad.org/shub/mcw-rcc/rstudio/1.1.442/2019-11-12-281fa24b-c8c5910d/Singularity
collection: mcw-rcc/rstudio
---

# mcw-rcc/rstudio:1.1.442

```bash
$ singularity pull shub://mcw-rcc/rstudio:1.1.442
```

## Singularity Recipe

```singularity
BootStrap: shub
From: mcw-rcc/r-base:3.5.0

%help
    This container runs RStudio.

%labels
    Maintainer Matthew Flister
    Version 07.26.18
    Rstudio_Version 1.1.442
    R_Version 3.5.0

%environment
    export QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb

%post
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts
    apt-get update
    apt-get -y install \
        software-properties-common \
        apt-transport-https \
        gstreamer1.0-plugins-base \
        libcdparanoia0 \
        libgstreamer-plugins-base1.0-0 \
        libgstreamer1.0-0 \
        libjpeg62 \
        libogg0 \
        libopus0 \
        liborc-0.4-0 \
        libtheora0 \
        libvisual-0.4-0 \
        libvorbis0a \
        libvorbisenc2 \
        libxslt-dev \
        locales \
        texlive-fonts-extra \
        wget \
        gdebi-core
    apt-get clean
    wget https://download1.rstudio.org/rstudio-xenial-1.1.442-amd64.deb
    gdebi --n rstudio-xenial-1.1.442-amd64.deb
    rm rstudio-xenial-1.1.442-amd64.deb
```

## Collection

 - Name: [mcw-rcc/rstudio](https://github.com/mcw-rcc/rstudio)
 - License: [MIT License](https://api.github.com/licenses/mit)

