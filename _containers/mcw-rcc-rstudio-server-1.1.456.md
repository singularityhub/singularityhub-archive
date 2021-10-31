---
id: 4715
name: "mcw-rcc/rstudio-server"
branch: "1.1.456"
tag: "1.1.456"
commit: "45825f1b6274569f1850dc71283aced6197e53ba"
version: "89351ea23afd56ef25480c6f09de34be"
build_date: "2018-09-10T20:28:06.758Z"
size_mb: 2487
size: 927313951
sif: "https://datasets.datalad.org/shub/mcw-rcc/rstudio-server/1.1.456/2018-09-10-45825f1b-89351ea2/89351ea23afd56ef25480c6f09de34be.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mcw-rcc/rstudio-server/1.1.456/2018-09-10-45825f1b-89351ea2/
recipe: https://datasets.datalad.org/shub/mcw-rcc/rstudio-server/1.1.456/2018-09-10-45825f1b-89351ea2/Singularity
collection: mcw-rcc/rstudio-server
---

# mcw-rcc/rstudio-server:1.1.456

```bash
$ singularity pull shub://mcw-rcc/rstudio-server:1.1.456
```

## Singularity Recipe

```singularity
BootStrap: shub
From: mcw-rcc/r-base:3.5.0

%help
    This container runs RStudio-Server.

%labels
    Maintainer Matthew Flister
    Version 09.07.18
    RStudio_Version 1.1.456
    R_Version 3.5.0

%apprun rserver
    exec rserver "${@}"

%runscript
    exec rserver "${@}"

%environment
    export QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb
    export PATH=/usr/lib/rstudio-server/bin:${PATH}

%setup
    install -Dv \
    pam_help.sh \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/pam_help
    install -Dv \
    rserver.conf \
    ${SINGULARITY_ROOTFS}/etc/rstudio/rserver.conf

%post
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
    wget https://download2.rstudio.org/rstudio-server-1.1.456-amd64.deb
    gdebi --n rstudio-server-1.1.456-amd64.deb
    rm rstudio-server-1.1.456-amd64.deb
    echo "R_LIBS=/extR/library1:/extR/library2" > /usr/local/lib/R/etc/Renviron.site
%test
    rstudio-server verify-installation
```

## Collection

 - Name: [mcw-rcc/rstudio-server](https://github.com/mcw-rcc/rstudio-server)
 - License: [MIT License](https://api.github.com/licenses/mit)

