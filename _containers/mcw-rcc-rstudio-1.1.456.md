---
id: 4879
name: "mcw-rcc/rstudio"
branch: "1.1.456-R_3.5.1"
tag: "1.1.456"
commit: "bba32d066addf060cda2e510fe50b073f34269f2"
version: "826ee2d6fe5dc353616af503df54c673"
build_date: "2020-09-22T17:05:11.509Z"
size_mb: 2835
size: 1040232479
sif: "https://datasets.datalad.org/shub/mcw-rcc/rstudio/1.1.456/2020-09-22-bba32d06-826ee2d6/826ee2d6fe5dc353616af503df54c673.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mcw-rcc/rstudio/1.1.456/2020-09-22-bba32d06-826ee2d6/
recipe: https://datasets.datalad.org/shub/mcw-rcc/rstudio/1.1.456/2020-09-22-bba32d06-826ee2d6/Singularity
collection: mcw-rcc/rstudio
---

# mcw-rcc/rstudio:1.1.456

```bash
$ singularity pull shub://mcw-rcc/rstudio:1.1.456
```

## Singularity Recipe

```singularity
BootStrap: shub
From: mcw-rcc/r-base:3.5.1

%help
    This container runs RStudio.

%labels
    Maintainer Matthew Flister
    Version 09.18.18
    Rstudio_Version 1.1.456
    R_Version 3.5.1

%environment
    export QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb
    export R_LIBS=$R_LIBS:/extR/library

%post
    mkdir -p /extR/library
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
        libssl1.0.0 \
        libssl-dev \
        gdebi-core
    apt-get clean
    wget https://download1.rstudio.org/rstudio-xenial-1.1.456-amd64.deb
    gdebi --n rstudio-xenial-1.1.456-amd64.deb
    rm rstudio-xenial-1.1.456-amd64.deb
    R -e 'source("https://bioconductor.org/biocLite.R"); biocLite("rtracklayer", lib="/usr/local/lib/R/library"); biocLite("openssl", lib="/usr/local/lib/R/library")'
```

## Collection

 - Name: [mcw-rcc/rstudio](https://github.com/mcw-rcc/rstudio)
 - License: [MIT License](https://api.github.com/licenses/mit)

