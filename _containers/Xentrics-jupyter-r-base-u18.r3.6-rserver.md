---
id: 13188
name: "Xentrics/jupyter-r-base"
branch: "master"
tag: "u18.r3.6-rserver"
commit: "e97e7c55c0ac02597f3f38ed1c5b112943ec17c7"
version: "da3d84d428dc85bac173120da65792dfc1b9b6e864d16dda1a499d02f3c56c1c"
build_date: "2020-11-13T13:42:08.978Z"
size_mb: 505.18359375
size: 529723392
sif: "https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/u18.r3.6-rserver/2020-11-13-e97e7c55-da3d84d4/da3d84d428dc85bac173120da65792dfc1b9b6e864d16dda1a499d02f3c56c1c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/Xentrics/jupyter-r-base/u18.r3.6-rserver/2020-11-13-e97e7c55-da3d84d4/
recipe: https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/u18.r3.6-rserver/2020-11-13-e97e7c55-da3d84d4/Singularity
collection: Xentrics/jupyter-r-base
---

# Xentrics/jupyter-r-base:u18.r3.6-rserver

```bash
$ singularity pull shub://Xentrics/jupyter-r-base:u18.r3.6-rserver
```

## Singularity Recipe

```singularity
BootStrap: shub
From: Xentrics/jupyter-r-base:r3.6.3


%labels

  LICENSE Copyright 2018 Jeremy Nicklas, Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), 
                                         to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
                                         and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above
                                         copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. 
  Maintainer Bastian Seelbinder
  RStudio_Version 1.2.5019

%help
  This will run RStudio Server

%apprun rserver
  exec rserver "${@}"

%runscript
  exec rserver "${@}"

%environment
  export PATH=/usr/lib/rstudio-server/bin:${PATH}

%post

  # to solve the "locale.Error: unsupported locale setting" error [https://stackoverflow.com/questions/14547631/python-locale-error-unsupported-locale-setting ]
  export LC_ALL=C

  # first install the following packages
  apt-get -y update && apt-get -y dist-upgrade
  apt-get install -y python3
  apt-get install -y debootstrap libarchive-dev squashfs-tools
  apt-get install -y libtool m4 automake && apt-get install -y python3-pip
  apt-get install -y nano git cmake gfortran curl wget autoconf bzip2 libtool libtool-bin sudo             # "sudo" is not installed by default in containers like docker, singularity

  # Software versions
  export RSTUDIO_VERSION=1.2.5019

  # Install RStudio Server
  apt-get update
  apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    gdebi-core \
    python3-pip
  wget \
    --no-verbose \
    -O rstudio-server.deb \
    "https://download2.rstudio.org/server/bionic/amd64/rstudio-server-${RSTUDIO_VERSION}-amd64.deb"
  gdebi -n rstudio-server.deb
  rm -f rstudio-server.deb

  # R package specific libraries
  apt-get install -y libcurl4-gnutls-dev libgit2-dev libopenblas-dev r-base-core libfontconfig1-dev libcairo2-dev
  apt-get install -y openssh-client openssh-server libssh-dev wget vim git gfortran autoconf pandoc qpdf libssh2-1-dev

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [Xentrics/jupyter-r-base](https://github.com/Xentrics/jupyter-r-base)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

