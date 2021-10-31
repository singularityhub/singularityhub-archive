---
id: 3527
name: "mcw-rcc/rstudio-server"
branch: "master"
tag: "1.1.442"
commit: "bde36e3c668c7eb9aeb255366aa03875ec40fcd3"
version: "2b382390d161b245f3690324829069c1"
build_date: "2020-04-07T06:01:11.008Z"
size_mb: 2486
size: 927088671
sif: "https://datasets.datalad.org/shub/mcw-rcc/rstudio-server/1.1.442/2020-04-07-bde36e3c-2b382390/2b382390d161b245f3690324829069c1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mcw-rcc/rstudio-server/1.1.442/2020-04-07-bde36e3c-2b382390/
recipe: https://datasets.datalad.org/shub/mcw-rcc/rstudio-server/1.1.442/2020-04-07-bde36e3c-2b382390/Singularity
collection: mcw-rcc/rstudio-server
---

# mcw-rcc/rstudio-server:1.1.442

```bash
$ singularity pull shub://mcw-rcc/rstudio-server:1.1.442
```

## Singularity Recipe

```singularity
BootStrap: shub
From: mcw-rcc/r-base:3.5.0

%help
    This container runs RStudio-Server.

%labels
    Maintainer Matthew Flister
    Version 07.02.18
    RStudio_Version 1.1.442
    R_Version 3.5.0

%apprun rserver
    exec rserver "${@}"

%runscript
    exec rserver "${@}"

%environment
    export QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb
    export PATH=/usr/lib/rstudio-server/bin:${PATH}
    export R_LIBS=/extR/library

%setup
    install -Dv \
    pam_help.sh \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/pam_help

%post
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts /extR/library1 /extR/library2
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
    wget https://download2.rstudio.org/rstudio-server-1.1.442-amd64.deb
    gdebi --n rstudio-server-1.1.442-amd64.deb
    rm rstudio-server-1.1.442-amd64.deb
%test
    rstudio-server verify-installation
```

## Collection

 - Name: [mcw-rcc/rstudio-server](https://github.com/mcw-rcc/rstudio-server)
 - License: [MIT License](https://api.github.com/licenses/mit)

